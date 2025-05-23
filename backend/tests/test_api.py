import requests
import pytest

@pytest.fixture
def rqData():
    return {
        "@moeda":"'USD'",
        "@dataInicial":"'11-11-2024'",
        "@dataFinalCotacao":"'11-16-2024'",
        "$format":"json",
        "$select":"cotacaoCompra,cotacaoVenda,dataHoraCotacao",
        "$skip": "0",
        "$top": "100",
    }
    
@pytest.fixture
def toString(rqData):
    string = ""
    cotVar = ""

    for key, value in rqData.items():
        if key.startswith("@"):
            cotVar += f"{key[1:]}={key},"
        string += f"{key}={value}&"

    if len(cotVar)>1:
        cotVar = "(" + cotVar[:-1] 
        cotVar += ")"
    
    string = f"?{string}"

    return cotVar + string


@pytest.fixture
def url(toString): 
    return f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo{toString}"[:-1]


@pytest.fixture
def rq(url):
    response = requests.get(url)
    yield response


def test_api(rq):

    assert rq.status_code == 200 and rq.ok
    json = rq.json()
    assert json is not None



