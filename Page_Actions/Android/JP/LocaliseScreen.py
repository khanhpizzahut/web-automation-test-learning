from Page_Actions.Android.JP.MenuScreen import MenuScreen
from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *
from Utilities.ExcelReader import getCellData


class LocaliseScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def localiseDelivery_WithPostCode(self):
        self.input(Localise_Delivery.txtfield_PostCode, getCellData("Localise Info",1,4))
        self.click(Localise_Delivery.btn_searchZipcode)
        self.verifyTextview(Localise_Delivery.result_search_1,getCellData("Localise Info",2,4))
        self.click(Localise_Delivery.result_search_1)
        self.verifyTextview(Select_TimeOrder_Screen.txtview_title,"What time would you like your order?")
        self.click(Select_TimeOrder_Screen.icon_close)
        self.click(Localise_Delivery.result_search_1)
        self.click(Select_TimeOrder_Screen.btn_select)

        return MenuScreen(self.driver)

    def localiseCollection(self):
        self.click(System_Permission_Localtion_Popup.op_allow)
        self.verifyTextview(Localise_Collection.txtview_messageForCollection, "Where will you pick up your pizza")
        self.getText(Localise_Collection.txtview_address)
        self.click(Localise_Collection.icon_back)

        self.click(Home_Screen.op_collection)
        self.click(Localise_Collection.icon_currentLocation)

        self.click(Localise_Collection.icon_search)
        self.verifyTextview(Localise_Collection.txtview_TitleSearch_Collection,"Where will you pick up your pizza")
        self.click(Localise_Collection.txtlink_NearByHut)
        self.input(Localise_Collection.txtfield_address,getCellData("Localise Info",9,4))
        self.verifyTextview(Localise_Collection.result_1_name,getCellData("Localise Info",10,4))
        self.verifyTextview(Localise_Collection.result_1_address, getCellData("Localise Info",11,4))
        self.click(Localise_Collection.result_1)

        self.verifyTextview(Localise_Collection.txtview_Hut_name,getCellData("Localise Info",12,4))
        self.verifyTextview(Localise_Collection.txtview_Hut_address,getCellData("Localise Info",13,4))
        self.getText(Localise_Collection.txtview_Hut_status)

        self.click(Localise_Collection.btn_StartOrder)
        self.verifyTextview(Select_TimeOrder_Screen.txtview_title, "What time would you like your order?")
        self.click(Select_TimeOrder_Screen.icon_close)
        self.click(Localise_Collection.btn_StartOrder)
        self.click(Select_TimeOrder_Screen.btn_select)

        return MenuScreen(self.driver)


