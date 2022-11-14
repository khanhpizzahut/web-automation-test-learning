from appium.webdriver.common.mobileby import MobileBy

class Home_Page():
    txtview_cart = (MobileBy.XPATH,"/html/body/div[1]/div[2]/div[1]/div/nav/div/div/div[1]/div/span[2]")
    icon_hut_reward = (MobileBy.XPATH,"/html/body/div[1]/div[2]/div[1]/div/nav/div/div/div[2]")
    op_language_english = (MobileBy.XPATH,"/html/body/div[1]/div[2]/div[1]/div/nav/div/div/div[2]/div/div/ul/li[4]/div/div/button[2]")
    op_login =(MobileBy.XPATH,"/html/body/div[1]/div[2]/div[1]/div/nav/div/div/div[2]/div/div/ul/li[2]/a")

    # post code
    txtfield_post_code = (MobileBy.XPATH,'//*[@id="delivery"]/div[1]/div[2]/div[5]/div/div/div[1]/input[1]')
    btn_order_now = (MobileBy.XPATH,'//*[@id="delivery"]/div[1]/div[2]/div[5]/div/div/div[2]/a')
    op_result_search_address_1 = (MobileBy.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/ul/li")

class Login_Page():
    txtfield_email = (MobileBy.ID,"emailAddress")
    txtfield_pass = (MobileBy.ID,"password")
    btn_login =(MobileBy.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div[2]/form/input")

class Menu_Page():
    txtview_Side = (MobileBy.XPATH,'//*[@id="nav"]/div/ul/li[5]/a')
    txtview_drinkdessert = (MobileBy.XPATH,'//*[@id="nav"]/div/ul/li[7]/a')
    btn_add_item_Coca = (MobileBy.XPATH,'//*[@id="main-layout"]/div[3]/div/div/div[1]/div[2]/div[2]/div/div[2]/div[4]/div')

class Cart_Page():
    txtview_quantity = (MobileBy.XPATH,'//*[@id="basket"]/div/div/div[4]/div[1]/div[1]/span/div/div/div[1]/div[1]')
    btn_addMoreQuantity = (MobileBy.XPATH,'//*[@id="modals-container"]/div/div/div[2]/div/div[1]/button[2]')
    bnt_save_changequantity = (MobileBy.XPATH,'//*[@id="modals-container"]/div/div/div[2]/div/div[2]/button[2]')
    btn_Checkout = (MobileBy.XPATH,'/html/body/div[1]/div[2]/div[4]/div[2]/div/div/button')






