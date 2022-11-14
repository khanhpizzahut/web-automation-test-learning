import time

from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *


class AccountScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)
        self.verifyTextview(Account_Screen.txtview_myAccount, "My Account")

    def backToHome(self):
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)

    def myProfile_InfoAndEdit(self):
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_MyAccount)
        self.click(Account_Screen.op_myProfile)

        self.verifyTextview(Home_Screen.txt_titleOnNavigationBar,"My Profile")
        self.getText(Account_Screen.txtfield_firstname)
        #self.getText(Account_Screen.txtfield_dob)
        self.click(Account_Screen.txt_Edit_Save_Navigationbar)
        self.input(Account_Screen.txtfield_firstname, self.getText(Account_Screen.txtfield_firstname)+" 1")
        self.click(Account_Screen.txt_Edit_Save_Navigationbar)
        self.verifyTextview(Warning_Popup_Oops.txtview_message,"Update profile successfully")
        self.click(Warning_Popup_Oops.btn_Yes)
        self.click(Home_Screen.icon_backOnNavigationBar)
        self.backToHome()

    def OrderHistory(self):
        self.click(Account_Screen.op_orderHistory)
        self.verifyTextview(Home_Screen.txt_titleOnNavigationBar,"Order History")
        try:
            orderid_outside = self.getText(OrderHistory_Screen.txtview_order_ID)
            self.getText(OrderHistory_Screen.txtview_address)
            self.getText(OrderHistory_Screen.txtview_subAddress)
            self.getText(OrderHistory_Screen.txtview_order_price)
            self.getText(OrderHistory_Screen.txtview_order_time)
            # check order detail
            self.click(OrderHistory_Screen.btn_order_detail)
            time.sleep(2)
            self.verifyTextview(Home_Screen.txt_titleOnNavigationBar, "Order Details")
            orderid_inside = self.getText(OrderDetail_Screen.txtview_order_ID)
            self.getText(OrderDetail_Screen.txtview_earn_slices_from_this_order)
            assert orderid_outside == orderid_inside
            self.click(Home_Screen.icon_backOnNavigationBar)

            # check latest order
            self.click(OrderHistory_Screen.btn_latest_order)
            self.getText(Latest_Order_Screen.txtview_estimateTime)
            self.getText(Latest_Order_Screen.txtview_order_ID)
            self.scroll_down()
            self.getText(Latest_Order_Screen.txtview_earn_slices_from_this_order)

            self.click(Latest_Order_Screen.btn_backtoHome)

        except: # emplty history - Pro env
            self.click(Home_Screen.icon_backOnNavigationBar)
            self.backToHome()


    def Saved_Address(self):
        self.click(Account_Screen.op_savedLocation)
        self.verifyTextview(Home_Screen.txt_titleOnNavigationBar, "Saved Address")
        try:
            name_1 = self.getText(SavedAddress_Screen.txtview_address_1)
            self.click(SavedAddress_Screen.icon_favourite_2)
            time.sleep(2)
            name_2 = self.getText(SavedAddress_Screen.txtview_address_1)
            assert name_1 != name_2
            self.click(SavedAddress_Screen.icon_delete_1)
            self.verifyTextview(Warning_Popup_Oops.txtview_message,"Are you sure you want to delete this address?")
            self.click(Warning_Popup_Oops.btn_No)
            self.click(SavedAddress_Screen.icon_delete_1)
            self.click(Warning_Popup_Oops.btn_Yes)
            self.click(Home_Screen.icon_backOnNavigationBar)
            self.backToHome()

        except:
            self.verifyTextview(SavedAddress_Screen.txtview_empltymessage,
                                "Looks like you haven't any saved address yet. Let's order and your address will be saved here.")
            self.click(Home_Screen.icon_backOnNavigationBar)
            self.backToHome()


    def changeLanguage(self):
        self.click(Account_Screen.op_languageChange)
        self.click(Left_Menu.op_language_JP)
        self.verifyTextview(Home_Screen.btn_viewMenu, "ピザメニューを見る")
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_MyAccount_jp)
        self.click(Left_Menu.op_language_2)
        self.click(Left_Menu.op_language_EN)
        self.verifyTextview(Home_Screen.btn_viewMenu, "View Pizza Menu")

