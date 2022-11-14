from Page_Actions.Android.JP.HomeScreen import HomeScreen
from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *


class LoginScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)
        self.verifyTextview(Login_Screen.txtviewSigin,"Sign in")

    def backToPreviousScreen(self):
        self.click(Login_Screen.icon_back)

    def lognIn_AccountQC(self):
        self.input(Login_Screen.txtfield_email,"qc.phdv@gmail.com")
        self.input(Login_Screen.txtfield_pass, "pizza@1234")
        self.click(Login_Screen.btn_login)
        self.getText(Home_Screen.txt_account_name)
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_home)

        return HomeScreen(self.driver)