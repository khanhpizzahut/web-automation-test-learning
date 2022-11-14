import time

from Page_Actions.BasePageForWebsite import BasePageForWebsite
from Page_Actions.Website.JP.Elements import *


class LoginPage(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def signInviaEmail(self):
        self.input(Login_Page.txtfield_email,"qc.phdv@gmail.com")
        self.input(Login_Page.txtfield_pass, "pizza@1234")
        self.click(Login_Page.btn_login)






