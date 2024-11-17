from django.test import TestCase, Client
import requests
import pytest

@pytest.fixture
def rqData():
    string = ""
    data = {
        "@dataCotacao":"'11-10-2023'",
        "$format":"json",
        "$select":"cotacaoCompra,cotacaoVenda",
        "$skip": "0",
        "$top": "10",
    }

    for key, value in data.items():
        string += f"{key}={value}&"

    return string

@pytest.fixture
def url(rqData): 
    return f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?{rqData}"[:-1]


@pytest.fixture
def rq(url):
    response = requests.get(url)
    yield response


def test_api(rq):

    assert rq.status_code == 200
    assert rq.content == {}

    with pytest.raises(Exception) as excinfo:
        rq.raise_for_status()

    
    assert excinfo.value == ""
