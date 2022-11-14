import time

import pytest

from Page_Actions.Android.JP.LeftMenuScreen import *
from Page_Actions.Android.JP.MenuScreen import MenuScreen
from TestCases.BaseTest import BaseTest
from Page_Actions.Android.JP.OnboardScreen import *


class Users_Are_Not_Login_And_Localise_Yet(BaseTest):

    def test_001_3249_verifyChangeLanguage(self):
        onboard = OnboardScreen(self.driver)
        onboard.changeLanguageToEnglish()

    def test_002_3250_verifyButtonSigin(self):
        onboard = OnboardScreen(self.driver)
        onboard.login().backToPreviousScreen()

    def test_003_3251_verifyGetCoupon(self):
        onboard = OnboardScreen(self.driver)
        onboard.get_coupon().checkCoupon_NotLoginYet_OnBoardScreen()

    def test_004_3252_verifyGoToMenu(self):
        onboard = OnboardScreen(self.driver)
        onboard.goto_menu()
# Go To Home Screen------
    def test_005_3253_verifyLeftMenu(self):
        leftmenu = LeftMenuScreen(self.driver)
        leftmenu.goToHome()
        leftmenu.signIn().backToPreviousScreen()
        leftmenu.changeLanguage()
        leftmenu.viewDetailFAQ()
        leftmenu.viewCustomerService()

    def test_006_3254_verifyViewCoupon(self):
        home = HomeScreen(self.driver)
        home.viewCoupons().checkPopupRequireLogin_CouponScreen()

    def test_007_3255_verifyAddItem_Pizza(self):
        home = HomeScreen(self.driver)
        # 1 Pizza
        home.viewMenu().pizza_AddItem().checkPopupRequireLocalise_Close_MenuScreen()
        menu = MenuScreen(self.driver)
        menu.pizza_AddItem().checkPopupRequireLocalise_Delivery_MenuScreen()
        menu.pizza_AddItem().checkPopupRequireLocalise_Collection_MenuScreen()

        # 2 My Box
        menu.myBox_AddItem().checkPopupRequireLocalise_Close_MenuScreen()
        # 3 Hut Party
        menu.hutParty_AddItem().checkPopupRequireLocalise_Close_MenuScreen()
        # 4 Side
        menu.side_AddItem().checkPopupRequireLocalise_Close_MenuScreen()
        # 5 WingStreet
        menu.wingStreet_AddItem().checkPopupRequireLocalise_Close_MenuScreen()
        # 6 Drink Dessert
        menu.drinkDessert_AddItem().checkPopupRequireLocalise_Close_MenuScreen()
        # 7 Original Price Pizza
        menu.originalPricePizza_AddItem().checkPopupRequireLocalise_Close_MenuScreen()
