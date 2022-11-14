from Page_Actions.Android.JP.WarningPopup import WarningPopup
from Page_Actions.BasePage import BasePageForWebsite
from Page_Actions.Android.JP.Elements import *
import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)

class SalesForceScreen(BasePageForWebsite):

    def __init__(self, driver):
        super().__init__(driver)

    def Banner_Info(self):
        self.click(Left_Menu.icon_leftMenu)

        log.logger.info("Check banner on LeftMenu")
        name_leftnemu = self.getText(Left_Menu.txtview_sf_name)
        slice_no_leftmenu = self.getText(Left_Menu.txtview_sf_Slice_No)
        des_leftmenu = self.getText(Left_Menu.txtview_sf_level_description)
        self.click(Left_Menu.op_MyAccount)

        log.logger.info("Check banner on Account Screen")
        self.getText(Account_Screen.txtview_sf_name)
        self.getText(Account_Screen.txtview_sf_slice_no)
        self.click(Account_Screen.btn_sf_viewReward_Bennefit)

        log.logger.info("Check banner on Reward and Benefit")
        name_benefit = self.getText(Left_Menu.txtview_sf_name)
        slice_no_benefit = self.getText(Left_Menu.txtview_sf_Slice_No)
        des_benefit = self.getText(Left_Menu.txtview_sf_level_description)
        assert name_leftnemu == name_benefit
        assert slice_no_leftmenu == slice_no_benefit
        assert des_leftmenu == des_benefit

        self.click(Home_Screen.icon_backOnNavigationBar)
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)
    def HutReward_viewAllAvaliableRewards(self):
        log.logger.info("Check Webview Reward")
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_MyAccount)
        self.click(Account_Screen.btn_sf_viewReward_Bennefit)

        self.click(SalesForce_Screen.btn_viewAllReward)
        self.verifyTextview(Home_Screen.txt_titleOnNavigationBar,"My Hut Rewards & Benefits")
        self.click(Home_Screen.icon_backOnNavigationBar)

        self.click(Home_Screen.icon_backOnNavigationBar)
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)

    def HutReward_Redeem(self):
        log.logger.info("Check Add item reward")
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_MyAccount)
        self.click(Account_Screen.btn_sf_viewReward_Bennefit)

        self.getText(SalesForce_Screen.txtview_item_1_name)
        self.getText(SalesForce_Screen.txtview_item_1_name)
        self.click(SalesForce_Screen.btn_item_1_redeem)
        warning = WarningPopup(self.driver)
        warning.checkPopupRequireLocalise_Delivery_MenuScreen()
        self.click(SalesForce_Screen.btn_item_1_redeem)
        warning.checkPopupRequireLocalise_Collection_MenuScreen()

        self.click(Home_Screen.icon_backOnNavigationBar)
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)

    def HutReward_History(self):
        log.logger.info("Check slice History")
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_MyAccount)
        self.click(Account_Screen.btn_sf_viewReward_Bennefit)

        self.click(SalesForce_Screen.btn_Slice_History)
        self.verifyTextview(SalesForce_Screen.txtview_history_title,"Slices History")
        self.getText(SalesForce_Screen.txtview_history_name_1)
        self.getText(SalesForce_Screen.txtview_history_slice_no_1)
        self.getText(SalesForce_Screen.txtview_history_date_1)
        self.click(Home_Screen.icon_backOnNavigationBar)

        self.click(Home_Screen.icon_backOnNavigationBar)
        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)

    def tier_Benefit(self):
        log.logger.info("Check Tier Benefits")
        self.click(Left_Menu.icon_leftMenu)
        self.click(Left_Menu.op_MyAccount)
        self.click(Account_Screen.btn_sf_viewReward_Bennefit)

        self.click(SalesForce_Screen.tab_Tier_Benefits)
        self.scroll_down()
        self.verifyTextview(SalesForce_Screen.txtview_benefit_1_name,"Signup reward")
        self.verifyTextview(SalesForce_Screen.txtview_benefit_1_des, "Get a FREE 1 Slice when you join Hut Rewards")

        self.click(SalesForce_Screen.tab_Silver)
        self.verifyTextview(SalesForce_Screen.txtview_benefit_1_name, "Rank-up reward")
        self.verifyTextview(SalesForce_Screen.txtview_benefit_1_des, "Get a FREE 1 Slice when you reach SILVER.")

        self.click(SalesForce_Screen.tab_Gold)
        self.verifyTextview(SalesForce_Screen.txtview_benefit_1_name, "Rank-up reward")
        self.verifyTextview(SalesForce_Screen.txtview_benefit_1_des, "Get a FREE 2 Slice when you reach GOLD.")

        self.click(SalesForce_Screen.tab_VIP)
        self.verifyTextview(SalesForce_Screen.txtview_benefit_1_name, "Rank-up reward")
        self.verifyTextview(SalesForce_Screen.txtview_benefit_1_des, "Get a FREE 3 Slice when you reach VIP.")

        self.click(Home_Screen.icon_backOnNavigationBar)

        self.click(Left_Menu.icon_leftMenu_onNavigationBar)
        self.click(Left_Menu.op_home)

