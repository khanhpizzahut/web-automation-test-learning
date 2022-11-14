from pathlib import Path


class Consts:
    # Project structure
    PROJECT_ROOT = str(Path(__file__).parent.parent)
    PROJECT_NAME = PROJECT_ROOT.split("/")[-1]
    LOG_FILE = PROJECT_ROOT + "/Logs/"
    DATA_CONFIG_DIR = PROJECT_ROOT + "/ConfigurationData/conf.ini"
    # DATA_FILE = PROJECT_ROOT + "/data/%s/%s.properties"
    SCREENSHOT_DIR = PROJECT_ROOT + "/Screenshots/"
    REPORT_DIR = PROJECT_ROOT + "/reports/"
    Excel_DATA = PROJECT_ROOT + "/Excel/Data.xlsx"


print(Consts.PROJECT_ROOT)

# pytest test_01_NotLocalise_NotLogin.py --alluredir="/Users/phdvqc/Documents/GitHub/python-automation-test-pom/allureReport"
#pytest --alluredir="/Users/phdvqc/Documents/GitHub/python-automation-test-pom/allureReport"
#allure serve /Users/phdvqc/Documents/GitHub/python-automation-test-pom/allureReport