from time import sleep
from playwright.sync_api import Page, expect
import pytest
import logging

@pytest.mark.django_db
def test_flow(email, url, page:Page):
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