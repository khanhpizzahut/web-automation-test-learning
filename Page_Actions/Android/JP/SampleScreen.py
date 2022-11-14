from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *


class xxx(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def test_01(self):
        self.click(Home_Screen.op_delivery)

