from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *


class CouponScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def backToHome(self):
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)

    def checkCoupon_NotLoginYet_OnBoardScreen(self):
        self.verifyTextview(Coupon_Screen.txtview_warningRequireLogin,
                            "Please log in or create a new account to enjoy coupon(s)")
        self.click(Coupon_Screen.btn_login)
        self.verifyTextview(Login_Screen.txtviewSigin, "Sign in")
        self.click(Login_Screen.icon_back)

        self.click(Coupon_Screen.btn_createAccount)
        self.verifyTextview(Login_Screen.txtviewSigin, "Sign in")
        self.click(Login_Screen.icon_back)
        self.click(Home_Screen.icon_backOnNavigationBar)

    def checkCoupon_Logined_NotLocalise(self):
        self.verifyTextview(Coupon_Screen.txtview_message,"Enter external coupon code here")
        self.getText(Coupon_Screen.coupon_1_name)
        self.getText(Coupon_Screen.coupon_1_code)
        self.getText(Coupon_Screen.coupon_1_valid)

        self.input(Coupon_Screen.txtfield_coupon_code, "test 12345")
        self.click(Coupon_Screen.btn_add_coupon)
        self.verifyTextview(Warning_Popup_Oops.txtview_message, "Coupon not found.")
        self.click(Warning_Popup_Oops.btn_Yes)

        self.click(Coupon_Screen.coupon_1_name)

    def checkCoupon_ViewMoreDetail_NotLocalise(self):
        self.getText(Coupon_Screen.txtview_couponDetail_name)
        self.getText(Coupon_Screen.txtview_couponDetail_valid)
        self.getText(Coupon_Screen.txtview_couponDetail_description)
        self.click(Coupon_Screen.btn_couponDetail_Redeem)
        # popup require localise
        self.verifyTextview(Require_Localise_Popup.txtview_message, "Please select the disposition method first")
        self.click(Require_Localise_Popup.txtview_message)
        # back to home
        self.click(Home_Screen.icon_backOnNavigationBar)
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)









