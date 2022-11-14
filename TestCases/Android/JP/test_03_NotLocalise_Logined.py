import pytest

from Page_Actions.Android.JP.AccountScreen import AccountScreen
from Page_Actions.Android.JP.LeftMenuScreen import LeftMenuScreen
from Page_Actions.Android.JP.MenuScreen import MenuScreen
from Page_Actions.Android.JP.SalesForceScreen import SalesForceScreen
from TestCases.BaseTest import BaseTest
from Page_Actions.Android.JP.OnboardScreen import *


class Users_Already_Logined(BaseTest):

    def test_001_3256_Login(self):
        onboard = OnboardScreen(self.driver)
        onboard.changeLanguageToEnglish()
        onboard.login().lognIn_AccountQC()
        home = HomeScreen(self.driver)
        home.checkAccont_info()

    #@pytest.mark.skip
    def test_002_3257_VerifyCoupon(self):
        home = HomeScreen(self.driver)
        home.viewCoupons()
        coupon = CouponScreen(self.driver)
        coupon.checkCoupon_Logined_NotLocalise()
        coupon.checkCoupon_ViewMoreDetail_NotLocalise()

    #@pytest.mark.skip
    def test_003_3258_VerifyAddItem_Pizza(self):
        home = HomeScreen(self.driver)
        # 1 Pizza
        home.viewMenu().pizza_AddItem().checkPopupRequireLocalise_Close_MenuScreen()

        menu = MenuScreen(self.driver)
        menu.pizza_AddItem().checkPopupRequireLocalise_Delivery_MenuScreen()
        menu.pizza_AddItem().checkPopupRequireLocalise_Collection_MenuScreen()
        menu.backtoHome()

    #@pytest.mark.skip
    def test_004_3259_verify_Cart(self):
        home = HomeScreen(self.driver)
        home.viewMenu()
        menu = MenuScreen(self.driver)
        menu.viewCart().checkCartEmpty()
        menu.backtoHome()

    #@pytest.mark.skip
    def test_005_3280_verify_LeftMenu(self):
        leftmenu = LeftMenuScreen(self.driver)
        leftmenu.goToHome()
        leftmenu.myAccount().backToHome()
        leftmenu.myCoupons().backToHome()

        leftmenu.notification().backToHome()

    #@pytest.mark.skip
    def test_006_3260_verity_Notification(self):
        leftmenu = LeftMenuScreen(self.driver)
        leftmenu.notification().detailNotification()

    #@pytest.mark.skip
    def test_007_3262_verify_Account_info(self):
        leftmenu = LeftMenuScreen(self.driver)
        leftmenu.myAccount()
        account = AccountScreen(self.driver)
        account.myProfile_InfoAndEdit()

    #@pytest.mark.skip
    def test_008_3265_verify_OrderHistory(self):
        leftmenu = LeftMenuScreen(self.driver)
        leftmenu.myAccount().OrderHistory()

    #@pytest.mark.skip
    def test_009_3267_Saved_Address(self):
        leftmenu = LeftMenuScreen(self.driver)
        leftmenu.myAccount().Saved_Address()

    #@pytest.mark.skip
    def test_010_3268_changeLanguage(self):
        leftmenu = LeftMenuScreen(self.driver)
        leftmenu.myAccount().changeLanguage()

    #@pytest.mark.skip
    def test_011_3270_salesforce_check_Banner_info(self):
        sf = SalesForceScreen(self.driver)
        sf.Banner_Info()
    def test_012_3273_salesforce_check_Tier_Benefit(self):
        sf = SalesForceScreen(self.driver)
        sf.tier_Benefit()

    def test_013_3274_salesforce_check_viewAllReward(self):
        sf = SalesForceScreen(self.driver)
        sf.HutReward_viewAllAvaliableRewards()

    def test_014_3275_salesforce_check_Redeem(self):
        sf = SalesForceScreen(self.driver)
        sf.HutReward_Redeem()

    def test_015_3278_salesforce_check_History(self):
        sf = SalesForceScreen(self.driver)
        sf.HutReward_History()

    def test_016_3266_check_OrderHistory_latest(self):
        pass # covered by def test_008_3265_verify_OrderHistory(self)

