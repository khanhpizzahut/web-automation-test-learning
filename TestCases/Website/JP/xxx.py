import pytest

import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)

log.logger.info("-------------------------------------------------")

def setup_module(module):
    log.logger.info("-------------------------------------------------")
    log.logger.info("------------Start test new feature---------------")
    log.logger.info("-------------------------------------------------")

def teardown_module(module):
    log.logger.info("-------------------------------------------------")
    log.logger.info("---------------------END-------------------------")
    log.logger.info("-------------------------------------------------")

def setup_function(function):
    log.logger.info("-- bat dau moi test case-")

def teardown_function(function):
    log.logger.info("--- ket thuc moi test case---")

def test_001_3107_ChangeLanguageToEnglish():
    log.logger.info(" run tc 01")

@pytest.mark.skip
def test_002_loginViaEmail():
    log.logger.info(" run tc 02")

# @pytest.mark.skip
def test_003_localise_delivery_postcode():
    log.logger.info(" run tc 03")

def test_004_add_DrinkDesser():
    log.logger.info(" run tc 04")
