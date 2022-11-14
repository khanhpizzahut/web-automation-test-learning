from Page_Actions.Android.JP.CouponScreen import CouponScreen
from Page_Actions.Android.JP.HomeScreen import HomeScreen
from Page_Actions.Android.JP.LoginScreen import LoginScreen
from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *


class OnboardScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def changeLanguageToEnglish(self):
        #change EN -> JP -> EN
        if self.getText(Onboard_Screen.txtview_start) == "Use your account to get started":
            self.click(Onboard_Screen.op_language)
            self.click(Onboard_Screen.op_language_jpanese)
            self.verifyTextview(Onboard_Screen.txtview_start,"アカウントを使って始めましょう")
            self.click(Onboard_Screen.op_language)
            self.click(Onboard_Screen.op_language_english)
            self.verifyTextview(Onboard_Screen.txtview_start, "Use your account to get started")
        else:
        # JP -> EN
            self.verifyTextview(Onboard_Screen.txtview_start, "アカウントを使って始めましょう")
            self.click(Onboard_Screen.op_language)
            self.click(Onboard_Screen.op_language_english)
            self.verifyTextview(Onboard_Screen.txtview_start, "Use your account to get started")

    def changelanguage_JP(self):
        self.click(Onboard_Screen.op_language)
        self.click(Onboard_Screen.op_language_jpanese)

    def login(self):
        self.click(Onboard_Screen.btn_signin)
        return LoginScreen(self.driver)

    def goto_menu(self):
        self.click(Onboard_Screen.btn_gotoMenu)
        return HomeScreen(self.driver)

    def get_coupon(self):
        self.click(Onboard_Screen.btn_getCoupon)
        return CouponScreen(self.driver)