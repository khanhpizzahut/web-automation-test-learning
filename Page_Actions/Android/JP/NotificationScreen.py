from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *


class NotificationScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def backToHome(self):
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)

    def detailNotification(self):
        self.verifyTextview(Home_Screen.txt_titleOnNavigationBar, "Notifications")
        try:
            self.getText(Notification_Screen.txt_Notification1_title)
            self.getText(Notification_Screen.txt_Notification1_content)
            self.getText(Notification_Screen.txt_Notification1_time)
            self.click(Notification_Screen.txt_Notification1_content)
            self.verifyTextview(Home_Screen.txt_titleOnNavigationBar, "Notification Detail")

            self.click(Home_Screen.icon_backOnNavigationBar)
            self.click(Left_Menu.icon_leftMenu_onNavigationBar)
            self.click(Left_Menu.op_home)
        except:
            self.click(Left_Menu.icon_leftMenu_onNavigationBar)
            self.click(Left_Menu.op_home)


