from Page_Actions.Android.JP.AccountScreen import AccountScreen
from Page_Actions.Android.JP.CouponScreen import CouponScreen
from Page_Actions.Android.JP.HomeScreen import HomeScreen
from Page_Actions.Android.JP.LoginScreen import LoginScreen
from Page_Actions.Android.JP.NotificationScreen import NotificationScreen
from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *


class LeftMenuScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def goToHome(self):
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_home)

    def signIn(self):
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_signin)
        return LoginScreen(self.driver)

    def changeLanguage(self):
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_language)
        self.click(Left_Menu.op_language_JP)
        self.verifyTextview(Home_Screen.btn_viewMenu,"ピザメニューを見る")
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_language_2)
        self.click(Left_Menu.op_language_EN)
        self.verifyTextview(Home_Screen.btn_viewMenu,"View Pizza Menu")

    def viewDetailFAQ(self):
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_FAQ)
        self.verifyTextview(Home_Screen.txt_titleOnNavigationBar, "FAQ's")
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)

    def viewCustomerService(self):
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_CustomerService)
        self.click(Left_Menu.op_sub_PrivacyPolicy)
        self.verifyTextview(Home_Screen.txt_titleOnNavigationBar, "Privacy Policy")
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_sub_Membership)
        self.verifyTextview(Home_Screen.txt_titleOnNavigationBar, "Membership T&C")
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)

    def myAccount(self):
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_MyAccount)
        return AccountScreen(self.driver)

    def myCoupons(self):
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_MyCoupon)
        self.verifyTextview(Coupon_Screen.txtview_message, "Enter external coupon code here")
        return CouponScreen(self.driver)

    def notification(self):
        self.click(Left_Menu.icon_leftMenu)
        #Check coupone lottery
        self.verifyTextview(Left_Menu.op_Coupon_Lottery, "Coupon Lottery")
        self.click(Left_Menu.op_Notifications)
        self.verifyTextview(Home_Screen.txt_titleOnNavigationBar, "Notifications")
        return NotificationScreen(self.driver)








