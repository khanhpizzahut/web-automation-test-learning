import time

import pytest

from Page_Actions.Website.JP.HomePage import HomePage
from Page_Actions.Website.JP.LoginPage import LoginPage
from Page_Actions.Website.JP.MenuPage import MenuPage
from TestCases.BaseTest import BaseTest


class Demo(BaseTest):

    def test_001_ChangeLanguageToEnglish(self):
        homepage = HomePage(self.driver)
        homepage.changelaguage()

    @pytest.mark.skip
    def test_002_loginViaEmail(self):
        homepage = HomePage(self.driver)
        homepage.gotologin()

        login = LoginPage(self.driver)
        login.signInviaEmail()

    #@pytest.mark.skip
    def test_003_localise_delivery_postcode(self):
        homepage = HomePage(self.driver)
        homepage.localise_delivery_postcode("2310041")

    def test_004_add_DrinkDesser(self):
        menu = MenuPage(self.driver)
        menu.add_drinkdessert()



