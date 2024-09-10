from django.shortcuts import render, redirect
from django.http import JsonResponse
from requests import request as rq
from matplotlib import pyplot as plt
import numpy as np
import io
import base64


def get(request,coin):

    days = 7

    try:

        response = rq("GET",f"https://economia.awesomeapi.com.br/json/daily/{coin}/{days}")

        data = response.json()
        code = data[0].get("code")
        codein = data[0].get("codein")

        lows = []
        highs = []

        for dt in data:
            lows.append(float(dt.get("low")))
            highs.append(float(dt.get("high")))

        xpoints= np.array(list(range(1,days+1)))

        plt.plot(xpoints,np.array(lows), marker = "o")
        plt.plot(xpoints,np.array(highs), marker = "o")

        plt.xlabel("Last 7 days")
        plt.ylabel(f"{code}/{codein}")

        buffer = io.BytesIO()

        plt.savefig(buffer, format="png")
        plt.close()

        buffer.seek(0)

        img = base64.b64encode(buffer.getvalue()).decode("utf-8")

        buffer.close()


        return JsonResponse({"image":f'data:image/png;base64,{img}'})

    except: pass


	
    return render(request, 'routes/home.html')