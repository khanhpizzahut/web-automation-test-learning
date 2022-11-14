import time

import pytest

from Page_Actions.Android.JP.MenuScreen import MenuScreen
from Page_Actions.Android.JP.OnboardScreen import *
from TestCases.BaseTest import BaseTest


class MakeOrder_Delivery(BaseTest):
    #@pytest.Mark.smoketest
    def test_001_sample_login(self):
        onboard = OnboardScreen(self.driver)
        onboard.changeLanguageToEnglish()
        onboard.login().lognIn_AccountQC()
    def test_002_sample_localise_delivery(self):
        home = HomeScreen(self.driver)
        home.localize_Delivery().localiseDelivery_WithPostCode().backtoHome()

    @pytest.mark.skip
    def test_003_sample_Add_HotDeal(self):
        home = HomeScreen(self.driver)
        home.viewMenu()
        menu = MenuScreen(self.driver)
        menu.deal_AddItemToCart("Delivery")
        time.sleep(5)

    #@pytest.mark.skip
    def test_004_sample_Add_Pizza(self):
        home = HomeScreen(self.driver)
        home.viewMenu()
        menu = MenuScreen(self.driver)
        menu.pizza_AddItemToCart("Delivery","Pizza")


    @pytest.mark.skip
    def test_005_sample_Add_MyBox(self):
        home = HomeScreen(self.driver)
        home.viewMenu()
        menu = MenuScreen(self.driver)
        menu.myBox_AddItemToCart("Delivery")
        time.sleep(15)

    @pytest.mark.skip # Chua lam
    def test_006_sample_Add_HutParty(self):
        home = HomeScreen(self.driver)
        home.viewMenu()
        menu = MenuScreen(self.driver)
        menu.HutParty_AddItemToCart("Delivery")
        time.sleep(15)

    @pytest.mark.skip
    def test_007_sample_Add_Side(self):
        home = HomeScreen(self.driver)
        home.viewMenu()
        menu = MenuScreen(self.driver)
        menu.addItemToCart("Delivery","Side")

    @pytest.mark.skip
    def test_008_sample_Add_WingStreet(self):
        home = HomeScreen(self.driver)
        home.viewMenu()
        menu = MenuScreen(self.driver)
        menu.addItemToCart("Delivery","WingStreet")

    @pytest.mark.skip
    def test_009_sample_Add_DrinkDessert(self):
        home = HomeScreen(self.driver)
        home.viewMenu()
        menu = MenuScreen(self.driver)
        menu.addItemToCart("Delivery","DrinkDessert")

    #@pytest.mark.skip
    def test_010_sample_Add_OriginalPricePizza(self):
        home = HomeScreen(self.driver)
        home.viewMenu()
        menu = MenuScreen(self.driver)
        menu.pizza_AddItemToCart("Delivery","Original Price Pizza")

