import pytest
import requests
from utils.data import Generator
from utils.urls import Urls
from selenium import webdriver


@pytest.fixture(scope='function')
def driver_1():
    driver = webdriver.Chrome()
    driver.get(Urls.MAIN_URL)
    yield driver
    driver.quit()

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None
    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.fullscreen_window()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()

@pytest.fixture()
def create_user():
    while True:
        try:
            payload = Generator.generate_payload()
            response = requests.post(Urls.MAIN_URL + Urls.CREATE_USER, data=payload)
            user_token = response.json()["accessToken"]
            yield payload
            requests.delete(Urls.MAIN_URL + Urls.DELETE_USER, headers={'Authorization': user_token})
            break
        except KeyError:
            pytest.fail("Failed to create user: 'accessToken' not found in response JSON")
