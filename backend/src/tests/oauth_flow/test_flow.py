from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.mark.django_db
def test_flow(url, browser, email):
    browser.get(url)

    email_input = browser.find_element(By.XPATH, "//*[@id='identifierId']")
    sleep(1)
    email_input.click()
    email_input.send_keys(email)

    next_button = browser.find_element(By.XPATH, "//*[@id='identifierNext']/div/button")
    next_button.click()
    sleep(10)