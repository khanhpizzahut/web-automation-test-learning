from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *


class CartScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def checkCartEmpty(self):
        self.verifyTextview(Cart_Screen.txtview_CartEmpty,"Looks like you haven't added any items \nto your cart yet")
        self.click(Cart_Screen.btn_menu)

    def changeHutAndOrderTime(self):
        pass
