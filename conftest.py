import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service # Chrome
from data_tests.data import Urls

from selenium.webdriver.firefox.service import Service as FirefoxService
from data_tests.data import Urls

@pytest.fixture
def driver():
    service = FirefoxService()  # или FirefoxService(executable_path="C:\\path\\to\\geckodriver.exe")
    drv = webdriver.Firefox(service=service)
    drv.get(Urls.MAIN_PAGE_URL)
    yield drv
    drv.quit()
