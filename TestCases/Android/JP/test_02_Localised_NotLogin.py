import pytest

from Page_Actions.Android.JP.MenuScreen import MenuScreen
from TestCases.BaseTest import BaseTest

from Page_Actions.Android.JP.OnboardScreen import *


class Users_Already_Localised(BaseTest):

    def test_001_3122_localise_Delivery(self):
        onboard = OnboardScreen(self.driver)
        onboard.changeLanguageToEnglish()
        onboard.goto_menu().localize_Delivery().localiseDelivery_WithPostCode()
        menu = MenuScreen(self.driver)
        menu.backtoHome()
        home = HomeScreen(self.driver)
        home.checkLocaliseInfo_Delivery()

    def test_002_3123_verifyAddItem_Delivery_Deal(self):
        home = HomeScreen(self.driver)
        home.seeAllMenu_localised().deal_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu = MenuScreen(self.driver)
        menu.deal_AddItem().checkPopupRequireLogin_Confirm_MenuScreen()
        menu.backtoHome()

    def test_003_3341_verifyPopupRequireLogin_Delivery(self):
        home = HomeScreen(self.driver)
        home.seeAllMenu_localised()
        menu = MenuScreen(self.driver)
        menu.pizza_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.myBox_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.hutParty_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.side_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.wingStreet_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.drinkDessert_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.originalPricePizza_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.backtoHome()

    def test_004_3343_verifyRemoveLocalization(self):
        home = HomeScreen(self.driver)
        home.removeLocalization().checkRemoveLocalization()

    def test_005_3124_localise_Collection(self):
        home = HomeScreen(self.driver)
        home.localize_Collection().localiseCollection()
        menu = MenuScreen(self.driver)
        menu.backtoHome()
        home.checkLocaliseInfo_Collection()

    def test_006_3125_verifyAddItem_Collection_Deal(self):
        home = HomeScreen(self.driver)
        home.seeAllMenu_localised().deal_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu = MenuScreen(self.driver)
        menu.deal_AddItem().checkPopupRequireLogin_Confirm_MenuScreen()
        menu.pizza_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.backtoHome()

    def test_007_3342_verifyPopupRequireLogin_Collection(self):
        home = HomeScreen(self.driver)
        home.seeAllMenu_localised()
        menu = MenuScreen(self.driver)
        menu.myBox_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.hutParty_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.side_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.wingStreet_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.drinkDessert_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.originalPricePizza_AddItem().checkPopupRequireLogin_Close_MenuScreen()
        menu.backtoHome()




