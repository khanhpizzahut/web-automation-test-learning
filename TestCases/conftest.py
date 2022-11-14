import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest
import logging

from Consts.consts import Consts
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# @pytest.fixture(scope="function")
@pytest.fixture(scope="class")
def start_driver(request):
    market = str(request.cls).split(".")[2]
    log.logger.info("[DRIVER] --> Start market: "+ market)
    #driver = webdriver.Chrome(executable_path=r"/Users/phdvqc/Documents/GitHub/web-automation-test-learning/driver/chromedriver")
    driver = webdriver.Chrome(
        executable_path=Consts.Driver_website_chrome)
    driver.get("https://www.pizzahut.jp/")
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    log.logger.info("[DRIVER] --> Quit")
    driver.quit()


def pytest_addoption(parser):
    pass
    #parser.addoption("--name", action="store", default="default name")
    #print("name is: "+name)