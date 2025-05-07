from time import sleep
from playwright.sync_api import Page, expect
import pytest
import logging

@pytest.mark.django_db
def test_flow(email, url, page:Page):
    logging.debug("Starting")
    page.goto(url)

    logging.debug("Get email input")
    email_input = page.locator('xpath=//*[@id="identifierId"]')
    assert email_input.is_enabled() and email_input.is_editable()
    email_input.fill(email, timeout=1000)
    expect(email_input).to_have_text(email)
    logging.debug("Email inserted")

    logging.debug("Get next button")
    next_button = page.locator('xpath=//*[@id="identifierNext"]/div/button')
    logging.debug("Click on the button")
    next_button.click()
    logging.debug("Wait login")
    sleep(10)

    expect(page.locator('xpath=//*[@id="password"]/div[1]/div/div[1]/input')).to_be_empty()