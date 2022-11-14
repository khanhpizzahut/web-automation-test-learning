import time

from Page_Actions.BasePageForWebsite import BasePageForWebsite
from Page_Actions.Website.JP.Elements import *

class MenuPage(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def add_drinkdessert(self):
        self.click(Menu_Page.txtview_drinkdessert)
        self.click(Menu_Page.btn_add_item_Coca)
        self.click(Cart_Page.txtview_quantity)
        self.click(Cart_Page.btn_addMoreQuantity)
        self.click(Cart_Page.btn_addMoreQuantity)
        self.click(Cart_Page.btn_addMoreQuantity)
        self.click(Cart_Page.btn_addMoreQuantity)
        self.click(Cart_Page.btn_addMoreQuantity)
        self.click(Cart_Page.btn_addMoreQuantity)
        self.click(Cart_Page.btn_addMoreQuantity)
        self.click(Cart_Page.btn_addMoreQuantity)
        self.click(Cart_Page.btn_addMoreQuantity)

        self.click(Cart_Page.bnt_save_changequantity)
        time.sleep(2)
        self.click(Cart_Page.btn_Checkout)
        time.sleep(2)
        self.scroll_down_website_1()
        time.sleep(2)
        self.scroll_down_website_2()
        time.sleep(2)
        self.scroll_down_website_3()
        time.sleep(2)
        self.scroll_down_website_4()
        time.sleep(2)










