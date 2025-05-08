from django.test.client import Client
from urllib.parse import quote
from dotenv import load_dotenv
import logging
import pytest
import os
os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")

@pytest.fixture
def email():
    load_dotenv()
    oauth_test_user = os.getenv("OAUTH_TEST_USER")
    assert oauth_test_user
    return oauth_test_user

@pytest.fixture
def path():
    return "/auth/oauth/"


@pytest.fixture
def url(client:Client, path):
    response = client.get(path)

    assert response.status_code==200
    json = response.json()
    redirect_uri = json.get("authorization_url")
    authorization_url = redirect_uri

    if 'testserver' in redirect_uri:
        enconded_test_server = quote("http://testserver",safe='')
        encoded_desired_server = quote("http://localhost:8000",safe='')
        authorization_url = redirect_uri.replace(enconded_test_server, encoded_desired_server)
    
    logging.debug(f"Modified Authorization url:{authorization_url}")

    return authorization_url

