from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import io
import base64
from datetime import datetime

matplotlib.use("Agg")


def generate_data(coin):

    now = datetime.now()
    sevendaysAgo = datetime.fromtimestamp(now.timestamp() - 60*60*24*7)
    parser = "%m-%d-%Y"

    print(now.strftime(parser), sevendaysAgo.strftime(parser))

    data = {
        "@moeda":f"'{coin}'",
        "@dataInicial":f"'{sevendaysAgo.strftime(parser)}'",
        "@dataFinalCotacao":f"'{now.strftime(parser)}'",
        "$format":"json",
        "$select":"cotacaoCompra,cotacaoVenda,dataHoraCotacao",
        "$skip": "0",
        "$top": "100",
    }

    return data


def generate_url(data):
    string = ""
    cotVar = "("

    for key, value in data.items():
        if key.startswith("@"):
            cotVar += f"{key[1:]}={key},"
        string += f"{key}={value}&"

    if len(cotVar)>1:
        cotVar = cotVar[:-1] 
        cotVar += ")"
    
    string = f"?{string}"

    string = cotVar + string

    return f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo{string}"[:-1]



@api_view(["GET"])
def get(request,coin):

    data = generate_data(coin)

    url = generate_url(data)
    print(url)

    try:

        response = requests.get(url)

        print(response)

        data = response.json()

        data = data.get("value")

        lows = []
        highs = []

        xpoints = []

        for dt in data:

            hora = dt.get("dataHoraCotacao")
            print(hora, "oi")
            parser = "%Y-%m-%d %H:%M:%S.%f"
            time = datetime.strptime(hora, parser)
            timestr = time.strftime("%d/%m")

            print(dt)

            if xpoints.count(timestr) > 0: 
                continue
                
            xpoints.append(timestr)
            lows.append(float(dt.get("cotacaoCompra")))
            highs.append(float(dt.get("cotacaoVenda")))

        xpoints= np.array(xpoints)

        fig, ax = plt.subplots()

        ax.plot(xpoints,np.array(lows), marker = "o", color="orange", label="Compra")
        ax.plot(xpoints,np.array(highs), marker = "o", color="green", label="Venda")

        
        ax.set_ylabel(f"{coin}/BRL")
        ax.set_title(f"Last 7 days {coin}/BRL")
        ax.grid()
        ax.legend()

        buffer = io.BytesIO()

        plt.savefig(buffer, format="png")

        buffer.seek(0)

        img = base64.b64encode(buffer.getvalue()).decode("utf-8")

        plt.close(fig)

        buffer.close()

        return Response({"image":f'data:image/png;base64,{img}'})

    except Exception as e:
        print(e)

    return Response(None)