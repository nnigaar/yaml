import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def setup_teardown():
    service = Service(r"D:\chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://userinyerface.com/game.html")
    yield driver
    driver.close()

def test_color(setup_teardown):
    driver = setup_teardown
    eleCookiesDiv = driver.find_element(By.CSS_SELECTOR, 'div.cookies')
    assert eleCookiesDiv.value_of_css_property("background-color") == "rgba(255, 0, 0, 1)", "Test 1 fail"

def test_height(setup_teardown):
    driver = setup_teardown
    eleCookiesDiv = driver.find_element(By.CSS_SELECTOR, 'div.cookies')
    assert eleCookiesDiv.value_of_css_property("height") == "155.2px", "Test 2 fail"
