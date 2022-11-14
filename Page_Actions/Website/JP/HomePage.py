import time

from Page_Actions.BasePageForWebsite import BasePageForWebsite
from Page_Actions.Website.JP.Elements import *

class HomePage(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def changelaguage(self):
        self.getText(Home_Page.txtview_cart)
        self.click(Home_Page.icon_hut_reward)
        self.click(Home_Page.op_language_english)
        self.getText(Home_Page.txtview_cart)

    def gotologin(self):
        self.click(Home_Page.icon_hut_reward)
        self.click(Home_Page.op_login)

    def localise_delivery_postcode(self, postcode):
        self.input(Home_Page.txtfield_post_code,postcode)
        self.click(Home_Page.btn_order_now)
        self.click(Home_Page.op_result_search_address_1)









