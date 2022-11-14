from Page_Actions.Android.JP.CouponScreen import CouponScreen
from Page_Actions.Android.JP.LocaliseScreen import LocaliseScreen
from Page_Actions.Android.JP.MenuScreen import MenuScreen
from Page_Actions.Android.JP.WarningPopup import WarningPopup
from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *
from Utilities.ExcelReader import getCellData


class HomeScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)
        self.verifyTextview(Home_Screen.btn_viewMenu,"View Pizza Menu")

    def localize_Delivery(self):
        self.click(Home_Screen.op_delivery)
        return LocaliseScreen(self.driver)

    def localize_Collection(self):
        self.click(Home_Screen.op_collection)
        return LocaliseScreen(self.driver)

    def viewCoupons(self):
        self.click(Home_Screen.btn_viewCoupons)
        return WarningPopup(self.driver)

    def viewMenu(self):
        self.click(Home_Screen.btn_viewMenu)
        return MenuScreen(self.driver)

    def checkLocaliseInfo_Delivery(self):
        self.verifyTextview(Home_Screen.txtview_address_info,getCellData("Localise Info",6,4))

    def checkLocaliseInfo_Collection(self):
        self.verifyTextview(Home_Screen.txtview_address_info,getCellData("Localise Info",14,4))


    def seeAllMenu_localised(self):
        self.click(Home_Screen.btn_SeeAllMenu)
        return MenuScreen(self.driver)

    def removeLocalization(self):
        self.click(Home_Screen.btn_change_localise)
        return WarningPopup(self.driver)

    def checkAccont_info(self):
        name = self.getText(Home_Screen.txt_account_name)
        assert name != ""
