import time
import unittest
import pytest
import logging
from Utilities.LogUtil import Logger
from Utilities.testrail import *
from Utilities.configReader import *
from datetime import datetime

log = Logger(__name__, logging.INFO)


@pytest.mark.usefixtures("start_driver")
class BaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        log.logger.info("-------------------------------------------------")
        log.logger.info("------------Start test new feature---------------")
        log.logger.info("-------------------------------------------------")
        print(str(cls))
        market = str(cls).split(".")[2]
        log.logger.info("Market:  " + market)

        if readConfig("config", "is_create_test_run") == "1":
            now = datetime.now()
            # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            testRunname = "Regression Test for "+market+": " + dt_string
            create_test_run(testRunname, list(readConfig("config", "testcases_id").split(",")))
            time.sleep(2)
            log.logger.info("[Testrail] create new test run name: " + testRunname)
        testRun_id = get_latest_test_run_id()
        writeConfig("config", "latest_test_run_id", str(testRun_id))
        log.logger.info("[Testrail] create new test run ID: " + str(testRun_id))

    @classmethod
    def tearDownClass(cls) -> None:
        log.logger.info("---End test new feature---")
        # backtohome()

    def setUp(self) -> None:
        arr_path = self.id().split('.')
        tcname = arr_path[len(arr_path) - 1]
        log.logger.info("\n\n\nStart test new testcase-----> " + tcname)

    def tearDown(self) -> None:
        # get testcase id from test name
        arr_path = self.id().split('.')  # ['TestCases', 'test_phdv', 'Test_PHDV', 'test_tc1']
        tcname = arr_path[len(arr_path) - 1]  # test_001_345_tc0
        # device_os = arr_path[1]  # Android or iOS
        case_id = tcname.split("_")[2]
        log.logger.info("[Testrail] Case ID: " + case_id)

        # Get test result after run testcase
        if hasattr(self._outcome, 'errors'):
            # Python 3.4 - 3.10  (These two methods have no side effects)
            result = self.defaultTestResult()
            self._feedErrorsToResult(result, self._outcome.errors)
        else:
            # Python 3.11+
            result = self._outcome.result
        ok = all(test != self for test, text in result.errors + result.failures)
        # Get result testcase pass or failed
        testRunid = readConfig("config", "latest_test_run_id")
        testcase_id = get_testcaseid_ontestrun(testRunid, case_id)
        if ok:
            # When testcase Passed
            if (case_id != 'sample') and (readConfig("config", "is_upload_test_results_to_testrail") == "1"):
                post_result_baseon_testcase_id(testcase_id, "Passed", "")
            log.logger.info("[RESULT - PASSED]: testcase id: " + str(testcase_id))

        else:
            for typ, errors in (('ERROR', result.errors), ('FAIL', result.failures)):
                # When testcase FAILED, push error message to result
                for test, text in errors:
                    if test is self:
                        msg = [x for x in text.split('\n')[1:]
                               if not x.startswith(' ')][0]
                        if (case_id != 'sample') and (readConfig("config", "is_upload_test_results_to_testrail") == "1"):
                            post_result_baseon_testcase_id(testcase_id, "Failed", msg)
                        log.logger.info("[RESULT - FAILED]: testcase id: " + str(testcase_id) + " - reason: " + msg)
