from django.test.client import Client
from urllib.parse import quote
from decouple import config
from playwright.sync_api import Page, expect
from time import sleep
import logging
import pytest
import os

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")

@pytest.fixture
def email():
    oauth_test_user = config("OAUTH_TEST_USER", 'testuser@gmail.com')
    assert oauth_test_user
    return oauth_test_user

@pytest.fixture
def path():
    return "/api/v1/auth/google/redirect/"


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

@pytest.mark.django_db
class TestGoogleOAuthFlow:

    def test_flow(self, email, url, page:Page):
        logging.debug("Starting")
        page.goto(url)
        page.pause()

        logging.debug("Get email input")
        email_input = page.locator('xpath=//*[@id="identifierId"]')
        email_input.wait_for()
        email_input.fill(email)
        logging.debug(f"Email input content:{email_input.input_value()}")
        expect(email_input).to_have_value(email)
        logging.debug("Email inserted")

        logging.debug("Get next button")
        next_button = page.locator('xpath=//*[@id="identifierNext"]/div/button')
        next_button.wait_for()
        logging.debug(f"Next button text: {next_button.inner_text()}")
        logging.debug("Click on the button")
        next_button.click()
        logging.debug("Wait login")

        expect(page.locator('xpath=//*[@id="password"]/div[1]/div/div[1]/input')).to_be_empty()