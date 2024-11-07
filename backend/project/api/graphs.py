from rest_framework.decorators import api_view
from rest_framework.response import Response
from requests import request as rq
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import io
import base64
from datetime import datetime

matplotlib.use("Agg")

@api_view(["GET"])
def get(request,coin):

    days = 7

    try:

        response = rq("GET",f"https://economia.awesomeapi.com.br/json/daily/{coin}/{days}")

        data = response.json()
        code = data[0].get("code")
        codein = data[0].get("codein")

        lows = []
        highs = []

        xpoints = []

        for dt in data:
            timestamp = int(dt.get("timestamp"))
            time = datetime.fromtimestamp(timestamp)
            timestr = time.strftime("%d/%m")
            xpoints.append(timestr)
            lows.append(float(dt.get("low")))
            highs.append(float(dt.get("high")))

        xpoints= np.array(xpoints)

        fig, ax = plt.subplots()

        ax.plot(xpoints,np.array(lows), marker = "o", color="orange", label="Low Values")
        ax.plot(xpoints,np.array(highs), marker = "o", color="green", label="High Values")

        
        ax.set_ylabel(f"{code}/{codein}")
        ax.set_title(f"Last 7 days {coin}/{codein}")
        ax.grid()
        ax.legend()

        buffer = io.BytesIO()

        plt.savefig(buffer, format="png")

        buffer.seek(0)

        img = base64.b64encode(buffer.getvalue()).decode("utf-8")

        plt.close(fig)

        buffer.close()

        return Response({"image":f'data:image/png;base64,{img}'})

    except: pass

    return None