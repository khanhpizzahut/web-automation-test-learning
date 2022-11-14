from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *


class WarningPopup(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    # When User is not login yet, tap on "View coupons" on Home Screen
    def checkPopupRequireLogin_CouponScreen(self):
        self.verifyTextview(Coupon_Screen.txtview_warningRequireLogin,
                            "Please log in or create a new account to enjoy coupon(s)")
        self.click(Coupon_Screen.btn_login)
        self.verifyTextview(Login_Screen.txtviewSigin, "Sign in")
        self.click(Login_Screen.icon_back)

        self.click(Home_Screen.btn_viewCoupons)
        self.click(Coupon_Screen.btn_createAccount)
        self.verifyTextview(Login_Screen.txtviewSigin, "Sign in")
        self.click(Login_Screen.icon_back)

        self.click(Home_Screen.btn_viewCoupons)
        self.click(Coupon_Screen.btn_doItLater)

    def checkPopupRequireLocalise_Delivery_MenuScreen(self):
        self.verifyTextview(Require_Localise_Popup.txtview_message,"Please select the disposition method first")
        self.click(Require_Localise_Popup.op_Delivery)
        self.verifyTextview(Home_Screen.txt_titleOnNavigationBar, "Delivery")
        self.click(Home_Screen.icon_backOnNavigationBar)

    def checkPopupRequireLocalise_Collection_MenuScreen(self):
        self.verifyTextview(Require_Localise_Popup.txtview_message,"Please select the disposition method first")
        self.click(Require_Localise_Popup.op_Collection)
        try:
            self.click(System_Permission_Localtion_Popup.op_allow)
        except:
            pass
        self.verifyTextview(Localise_Collection.txtview_messageForCollection, "Where will you pick up your pizza")
        self.click(Localise_Collection.icon_back)
    def checkPopupRequireLocalise_Close_MenuScreen(self):
        self.verifyTextview(Require_Localise_Popup.txtview_message, "Please select the disposition method first")
        self.click(Require_Localise_Popup.txtview_message)

    def checkPopupRequireLogin_Close_MenuScreen(self):
        self.verifyTextview(Warning_Popup_Require_Login.txtview_message, "Please login to continue")
        self.click(Warning_Popup_Require_Login.btn_cancel)

    def checkPopupRequireLogin_Confirm_MenuScreen(self):
        self.verifyTextview(Warning_Popup_Require_Login.txtview_message, "Please login to continue")
        self.click(Warning_Popup_Require_Login.btn_confirm)
        self.verifyTextview(Login_Screen.txtviewSigin, "Sign in")
        self.click(Login_Screen.icon_back)

    def checkRemoveLocalization(self):
        self.verifyTextview(Warning_Popup_Remove_Localization.txtview_message,"Changing your disposition will refresh your cart. Are you sure to want to proceed?")
        self.click(Warning_Popup_Remove_Localization.btn_No)
        self.click(Home_Screen.btn_change_localise)
        self.click(Warning_Popup_Remove_Localization.btn_Yes)