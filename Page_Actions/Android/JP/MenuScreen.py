import time

from Page_Actions.Android.JP.CartScreen import CartScreen
from Page_Actions.Android.JP.WarningPopup import WarningPopup
from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *
from Utilities.ExcelReader import *

class MenuScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def backtoHome(self):
        self.click(Menu_Screen.icon_LeftMenu)
        self.click(Left_Menu.op_home)

    def deal_AddItem(self,ColectionOrDelivery):
        self.click(Menu_Screen.tab_Deal)
        if ColectionOrDelivery == "Delivery":
            self.scrollToTextAndClick(getCellData("Deals", 3, 3))
        else:
            self.scrollToTextAndClick(getCellData("Deals", 3, 4))
        return WarningPopup(self.driver)

    def deal_AddItemToCart(self,ColectionOrDelivery):
        i = 4  # i is column excel
        sheetname = "Deals"
        if ColectionOrDelivery == "Delivery":
            i = 3

        self.deal_AddItem(ColectionOrDelivery)
        self.click(Home_Screen.icon_backOnNavigationBar)
        self.deal_AddItem(ColectionOrDelivery)

        time.sleep(2)
        self.verifyTextview(Menu_Deal_Screen.txtview_deal_name,getCellData(sheetname,3,i))
        self.verifyTextview(Menu_Deal_Screen.txtview_deal_description,getCellData(sheetname,5,i))
        self.click(Menu_Deal_Screen.txtlink_viewDetail)
        self.verifyTextview(Menu_Deal_Screen.txtview_detail_content,getCellData(sheetname,6,i))
        self.scroll_half_down()
        self.click(Menu_Deal_Screen.icon_add)
        # Add pizza to deal
        self.scrollToTextAndClick(getCellData(sheetname,8,i))
        self.click(Item_Detail_Screen.btn_addMoreToDeal)

        self.verifyTextview(Menu_Deal_Screen.txtview_added_item_name,getCellData(sheetname,13,i))
        self.verifyTextview(Menu_Deal_Screen.txtview_added_item_name_subname,getCellData(sheetname,14,i))
        self.verifyTextview(Menu_Deal_Screen.txtview_added_item_name_price,getCellData(sheetname,15,i))
        self.verifyTextview(Menu_Deal_Screen.txtview_quatity,"1")
        self.verifyTextview(Menu_Deal_Screen.txtview_total_price,getCellData(sheetname,19,i))
        self.click(Menu_Deal_Screen.btn_plus)
        self.verifyTextview(Menu_Deal_Screen.txtview_quatity,"2")
        self.verifyTextview(Menu_Deal_Screen.txtview_total_price,getCellData(sheetname,20,i))
        self.click(Menu_Deal_Screen.btn_minus)
        self.verifyTextview(Menu_Deal_Screen.txtview_quatity,"1")
        self.verifyTextview(Menu_Deal_Screen.txtview_total_price,getCellData(sheetname,19,i))
        self.click(Menu_Deal_Screen.txtview_total_price)


    def pizza_AddItem(self,ColectionOrDelivery):
        self.click(Menu_Screen.tab_Pizza)
        if ColectionOrDelivery == "Delivery":
            self.scrollToTextAndClick(getCellData("Pizza", 3, 3))
        else:
            self.scrollToTextAndClick(getCellData("Pizza", 3, 4))
        return WarningPopup(self.driver)

    def pizza_AddItemToCart(self,ColectionOrDelivery, category):
        i = 4  # i is column excel
        sheetname = category
        if ColectionOrDelivery == "Delivery":
            i = 3
        # Category
        if category == "Pizza":
            self.click(Menu_Screen.tab_Pizza)
        elif category == "Original Price Pizza":
            self.click(Menu_Screen.tab_Side)
            self.click(Menu_Screen.tab_WingStreet)
            self.click(Menu_Screen.tab_DrinksDessert)
            self.click(Menu_Screen.tab_OriginalPricePizza)

        self.scrollToTextAndClick(getCellData(sheetname,3,i))
        self.click(Home_Screen.icon_backOnNavigationBar)
        self.scrollToTextAndClick(getCellData(sheetname,3,i))

        self.verifyTextview(Item_Detail_Screen.txtview_name,getCellData(sheetname,3,i))
        self.verifyTextview(Item_Detail_Screen.txtview_description,getCellData(sheetname,5,i))
        self.click(Item_Detail_Screen.txtlink_viewDetail)
        self.verifyTextview(Item_Detail_Screen.txtview_detail_content,getCellData(sheetname,6,i))
        self.scroll_half_down()
        self.scroll_down()
        # Change Size and Crust
        self.verifyTextview(Menu_Pizza_Screen.txt_curent_size,getCellData(sheetname,8,i))
        self.click(Menu_Pizza_Screen.btn_change_Size)
        self.scrollToTextAndClick(getCellData(sheetname,9,i))
        # Change Default topping
        self.click(Menu_Pizza_Screen.op_Topping_Default)
        self.click(Menu_Pizza_Screen.icon_remove_default_Topping)
        self.click(Menu_Pizza_Screen.op_Topping_Default)
        # Add more topping
        self.click(Menu_Pizza_Screen.op_AddMoreTopping)
        self.scrollToTextAndClick(getCellData(sheetname,10,i))
        #self.scroll_up()
        self.click(Menu_Pizza_Screen.op_AddMoreTopping)
        # Check add and remove topping info
        self.verifyTextview(Menu_Pizza_Screen.txtview_added_topping_name,getCellData(sheetname,10,i))
        self.verifyTextview(Menu_Pizza_Screen.txtview_removed_topping_name,getCellData(sheetname,11,i))
        # check change quantity
        self.verifyTextview(Item_Detail_Screen.txtview_total_price,getCellData(sheetname,13,i))
        self.verifyTextview(Item_Detail_Screen.txtview_quatity,"1")
        self.click(Item_Detail_Screen.btn_plus)
        self.click(Item_Detail_Screen.btn_plus)
        self.verifyTextview(Item_Detail_Screen.txtview_total_price,getCellData(sheetname,14,i))
        self.verifyTextview(Item_Detail_Screen.txtview_quatity,"3")
        self.click(Item_Detail_Screen.btn_minus)
        self.click(Item_Detail_Screen.btn_minus)

        self.verifyTextview(Item_Detail_Screen.txtview_total_price,getCellData(sheetname,13,i))
        self.click(Item_Detail_Screen.txtview_total_price)

        self.backtoHome()

    def myBox_AddItem(self,ColectionOrDelivery):
        self.click(Menu_Screen.tab_MyBox)
        if ColectionOrDelivery == "Delivery":
            self.scrollToTextAndClick(getCellData("MyBox", 3, 3))
        else:
            self.scrollToTextAndClick(getCellData("MyBox", 4, 3))
        return WarningPopup(self.driver)

    def myBox_AddItemToCart(self,ColectionOrDelivery):
        i = 4  # i is column excel
        sheetname = "MyBox"
        if ColectionOrDelivery == "Delivery":
            i = 3

        self.myBox_AddItem(ColectionOrDelivery)
        self.click(Home_Screen.icon_backOnNavigationBar)
        self.myBox_AddItem(ColectionOrDelivery)

        # Detail
        self.verifyTextview(Item_Detail_Screen.txtview_name, getCellData(sheetname, 3, i))
        self.verifyTextview(Item_Detail_Screen.txtview_description, getCellData(sheetname, 5, i))
        self.click(Item_Detail_Screen.txtlink_viewDetail)
        self.verifyTextview(Item_Detail_Screen.txtview_detail_content, getCellData(sheetname, 6, i))
        self.scroll_half_down()
        self.scroll_down()

        # check change quantity
        self.verifyTextview(Item_Detail_Screen.txtview_total_price, getCellData(sheetname, 8, i))
        self.verifyTextview(Item_Detail_Screen.txtview_quatity, "1")
        self.click(Item_Detail_Screen.btn_plus)
        self.click(Item_Detail_Screen.btn_plus)
        self.verifyTextview(Item_Detail_Screen.txtview_total_price, getCellData(sheetname, 9, i))
        self.verifyTextview(Item_Detail_Screen.txtview_quatity, "3")
        self.click(Item_Detail_Screen.btn_minus)
        self.click(Item_Detail_Screen.btn_minus)

        self.verifyTextview(Item_Detail_Screen.txtview_total_price, getCellData(sheetname, 8, i))
        self.click(Item_Detail_Screen.txtview_total_price)

    def addItemToCart(self,ColectionOrDelivery, category):
        i = 4  # i is column excel
        sheetname = category
        if ColectionOrDelivery == "Delivery":
            i = 3
        # Category
        if category == "Side":
            self.click(Menu_Screen.tab_Side)
        elif category == "WingStreet":
            self.click(Menu_Screen.tab_Side)
            self.click(Menu_Screen.tab_WingStreet)
        elif category == "DrinkDessert":
            self.click(Menu_Screen.tab_Side)
            self.click(Menu_Screen.tab_WingStreet)
            self.click(Menu_Screen.tab_DrinksDessert)
        elif category == "Original Price Pizza":
            self.click(Menu_Screen.tab_Side)
            self.click(Menu_Screen.tab_WingStreet)
            self.click(Menu_Screen.tab_DrinksDessert)
            self.click(Menu_Screen.tab_OriginalPricePizza)


        self.scrollToTextAndClick(getCellData(sheetname, 3, i))
        self.click(Home_Screen.icon_backOnNavigationBar)
        self.scrollToTextAndClick(getCellData(sheetname, 3, i))

        # Detail
        self.verifyTextview(Item_Detail_Screen.txtview_name, getCellData(sheetname, 3, i))
        self.verifyTextview(Item_Detail_Screen.txtview_description, getCellData(sheetname, 5, i))
        #self.click(Item_Detail_Screen.txtlink_viewDetail)
        #self.verifyTextview(Item_Detail_Screen.txtview_detail_content, getCellData(sheetname, 6, i))
        #self.scroll_half_down()
        #self.scroll_down()

        # check change quantity
        self.verifyTextview(Item_Detail_Screen.txtview_total_price, getCellData(sheetname, 8, i))
        self.verifyTextview(Item_Detail_Screen.txtview_quatity, "1")
        self.click(Item_Detail_Screen.btn_plus)
        self.click(Item_Detail_Screen.btn_plus)
        self.verifyTextview(Item_Detail_Screen.txtview_total_price, getCellData(sheetname, 9, i))
        self.verifyTextview(Item_Detail_Screen.txtview_quatity, "3")
        self.click(Item_Detail_Screen.btn_minus)
        self.click(Item_Detail_Screen.btn_minus)

        self.verifyTextview(Item_Detail_Screen.txtview_total_price, getCellData(sheetname, 8, i))
        self.click(Item_Detail_Screen.txtview_total_price)

        self.backtoHome()

    def hutParty_AddItem(self,ColectionOrDelivery):
        self.click(Menu_Screen.tab_HutParty)
        if ColectionOrDelivery == "Delivery":
            self.scrollToTextAndClick(getCellData("HutParty", 3, 3))
        else:
            self.scrollToTextAndClick(getCellData("HutParty", 3, 4))
        return WarningPopup(self.driver)

    def HutParty_AddItemToCart(self,ColectionOrDelivery):
        i = 4  # i is column excel
        sheetname = "HutParty"
        if ColectionOrDelivery == "Delivery":
            i = 3

        self.hutParty_AddItem(ColectionOrDelivery)
        self.click(Home_Screen.icon_backOnNavigationBar)
        self.hutParty_AddItem(ColectionOrDelivery)
        time.sleep(2)

        self.verifyTextview(Item_Detail_Screen.txtview_name,getCellData(sheetname,3,i))
        self.verifyTextview(Item_Detail_Screen.txtview_description,getCellData(sheetname,5,i))
        self.click(Item_Detail_Screen.txtlink_viewDetail)
        self.verifyTextview(Item_Detail_Screen.txtview_detail_content,getCellData(sheetname,6,i))
        self.scroll_half_down()
        self.scroll_down()

        # Add product 1
        self.click(Menu_HutParty_Screen.icon_add_product)
        self.scrollToTextAndClick(getCellData(sheetname, 8, i))
        self.click(Item_Detail_Screen.btn_addMoreToDeal)
        # Add product 2
        self.click(Menu_HutParty_Screen.icon_add_product)
        self.scrollToTextAndClick(getCellData(sheetname, 9, i))
        self.click(Item_Detail_Screen.btn_addMoreToDeal)
        # Add product 3
        self.click(Menu_HutParty_Screen.icon_add_product)
        self.scrollToTextAndClick(getCellData(sheetname, 10, i))
        self.click(Item_Detail_Screen.btn_addMoreToDeal)
        # Add product 4
        self.click(Menu_HutParty_Screen.icon_add_product)
        self.scrollToTextAndClick(getCellData(sheetname, 11, i))
        self.click(Item_Detail_Screen.btn_addMoreToDeal)
        # Change quantity
        self.verifyTextview(Menu_Deal_Screen.txtview_quatity, "1")
        self.verifyTextview(Menu_Deal_Screen.txtview_total_price, getCellData(sheetname, 15, i))
        self.click(Menu_Deal_Screen.btn_plus)
        self.click(Menu_Deal_Screen.btn_plus)
        self.verifyTextview(Menu_Deal_Screen.txtview_quatity, "3")
        self.verifyTextview(Menu_Deal_Screen.txtview_total_price, getCellData(sheetname, 16, i))
        self.click(Menu_Deal_Screen.btn_minus)
        self.click(Menu_Deal_Screen.btn_minus)
        self.verifyTextview(Menu_Deal_Screen.txtview_quatity, "1")
        self.verifyTextview(Menu_Deal_Screen.txtview_total_price, getCellData(sheetname, 15, i))
        self.click(Menu_Deal_Screen.txtview_total_price)
        self.backtoHome()

    def side_AddItem(self):
        self.click(Menu_Screen.tab_Side)
        self.scrollToTextAndClick(getCellData("Side", 2, 2))
        return WarningPopup(self.driver)

    def wingStreet_AddItem(self):
        self.click(Menu_Screen.tab_WingStreet)
        self.scrollToTextAndClick(getCellData("WingStreet", 2, 2))
        return WarningPopup(self.driver)

    def drinkDessert_AddItem(self):
        self.click(Menu_Screen.tab_DrinksDessert)
        self.scrollToTextAndClick(getCellData("DrinkDessert", 2, 2))
        return WarningPopup(self.driver)

    def originalPricePizza_AddItem(self):
        self.click(Menu_Screen.tab_OriginalPricePizza)
        self.scrollToTextAndClick(getCellData("Original Price Pizza", 2, 2))
        return WarningPopup(self.driver)

    def viewCart(self):
        self.click(Menu_Screen.icon_Cart)
        self.click(Cart_Screen.btn_menu)
        self.click(Menu_Screen.btn_viewCart)
        return CartScreen(self.driver)
