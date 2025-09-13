import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from data_tests.data import Urls


@allure.step('Открытие браузера, переход на страницу приложения, закрытие браузера')
@pytest.fixture
def driver():
    service = Service(executable_path="C:\\path\\to\\geckodriver.exe")
    driver = webdriver.Chrome()
    driver.get(Urls.MAIN_PAGE_URL)
    yield driver
    driver.quit()



def pytest_make_parametrize_id(val):
    return repr(val)


