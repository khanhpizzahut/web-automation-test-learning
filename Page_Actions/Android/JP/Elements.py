from appium.webdriver.common.mobileby import MobileBy

class Onboard_Screen():
    op_language = (MobileBy.ID,"clLanguageSelector")
    op_language_jpanese = (MobileBy.XPATH,"//android.view.ViewGroup[@index = 0]")
    op_language_english = (MobileBy.XPATH, "//android.view.ViewGroup[@index = 1]")
    txtview_start = (MobileBy.ID,"tvUseYourAccountToGetStarted") #Use your account to get started
    btn_signin = (MobileBy.ID,"btnSignInSignUp")
    btn_gotoMenu = (MobileBy.ID,"btnMenu")
    btn_getCoupon = (MobileBy.ID,"btnGetCoupon")

class Home_Screen(): # Not localise yet
    txt_account_name = (MobileBy.ID, "tvWelcome")
    op_delivery = (MobileBy.ID,"selection_left")
    op_collection = (MobileBy.ID, "selection_right")
    btn_viewCoupons = (MobileBy.ID,"btnViewCoupons")
    btn_viewMenu = (MobileBy.ID,"btnViewPromotions")
    #Localised Delivery
    txtview_address_info = (MobileBy.ID,"tvAddress")
    btn_change_localise = (MobileBy.ID,"btnChange")
    btn_SeeAllMenu = (MobileBy.ID,"btnOrderNow")

    # General element
    txt_titleOnNavigationBar = (MobileBy.ID, "toolbar_title")
    icon_backOnNavigationBar = (MobileBy.ID,"toolbar_back")

class Left_Menu():
    #SalesForce Banner
    txtview_sf_name = (MobileBy.ID, "lbYouHave")
    txtview_sf_Slice_No = (MobileBy.ID, "lbSliceValue")
    txtview_sf_level_description = (MobileBy.ID, "txtLevelDescription")

    icon_leftMenu = (MobileBy.ID,"ivLeftMenu")
    icon_leftMenu_onNavigationBar = (MobileBy.ID,"toolbar_back")

    op_home =(MobileBy.XPATH,"//android.widget.TextView[@text='Home']")
    op_signin = (MobileBy.XPATH, "//android.widget.TextView[@text='Sign In']")
    op_language = (MobileBy.XPATH, "//android.widget.TextView[@text='Language/言語']")
    op_language_2 = (MobileBy.XPATH, "//android.widget.TextView[@text='言語/Language']")
    op_language_JP = (MobileBy.XPATH,"//android.view.ViewGroup[@index=0]/android.widget.CheckBox[@index=0]")
    op_language_EN = (MobileBy.XPATH, "//android.view.ViewGroup[@index=1]/android.widget.CheckBox[@index=0]")
    op_FAQ = (MobileBy.XPATH, '//android.widget.TextView[@text="FAQ\'s"]')
    op_CustomerService = (MobileBy.XPATH, "//android.widget.TextView[@text='Customer service']")
    op_sub_PrivacyPolicy =(MobileBy.XPATH,"//android.widget.TextView[@text='Privacy Policy']")
    op_sub_Membership = (MobileBy.XPATH,"//android.widget.TextView[@text='Membership T&C']")

    op_MyAccount = (MobileBy.XPATH,"//android.widget.TextView[@text='My Account']")
    op_MyAccount_jp = (MobileBy.XPATH,"//android.widget.TextView[@text='マイページ']")
    op_MyCoupon = (MobileBy.XPATH,"//android.widget.TextView[@text='My Coupons']")
    op_Notifications = (MobileBy.XPATH, "//android.widget.TextView[@text='Notifications']")
    op_Coupon_Lottery = (MobileBy.XPATH, "//android.widget.TextView[@text='Coupon Lottery']")

class Localise_Delivery():
    tab_Zipcode = (MobileBy.ID,"clTabZipCode")
    txtfield_PostCode = (MobileBy.ID,"etSearchZipCode") # 231 0041
    btn_searchZipcode = (MobileBy.ID,"llBtnSearch")

    tab_Address = (MobileBy.ID,"clTabAddress")
    txtfield_Address = (MobileBy.ID, "etSearchAddress")

    result_search_1 = (MobileBy.XPATH,"//android.widget.TextView[@index = 0]")
    result_search_2 = (MobileBy.XPATH, "//android.widget.TextView[@index = 1]")

class Localise_Collection():
    icon_back = (MobileBy.ID,"ivBtnBack")
    icon_currentLocation = (MobileBy.ID,"ivMyLocation")

    txtview_messageForCollection = (MobileBy.ID,"tvPickYourPizzaTitle") #Where will you pick up your pizza
    txtview_address = (MobileBy.ID,"tvAddress")
    icon_search = (MobileBy.ID,"ivSearch")

    btn_StartOrder = (MobileBy.ID,"tvStartMyOrder")

    # Search address for collection
    txtview_TitleSearch_Collection = (MobileBy.ID,"tvPickYourPizzaTitle") #Where will you pick up your pizza
    txtfield_address = (MobileBy.ID,"etSearchAddress")
    txtlink_NearByHut = (MobileBy.ID,"tvNearestHut")

    result_1 = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=2]/android.view.ViewGroup[@index=0]")
    result_1_name = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=2]/android.view.ViewGroup[@index=0]/android.widget.TextView[@index=1]")
    result_1_address = (MobileBy.XPATH,
                     "//androidx.recyclerview.widget.RecyclerView[@index=2]/android.view.ViewGroup[@index=0]/android.widget.TextView[@index=2]")

    txtview_Hut_name = (MobileBy.ID,"tvOutletName")
    txtview_Hut_status = (MobileBy.ID, "tvOutletStatus")
    txtview_Hut_address = (MobileBy.ID, "tvOutletLocation") #1-39-4 Arai, Nakano-ku, Tokyo


class Select_TimeOrder_Screen():
    txtview_title = (MobileBy.ID,"tvTitle") #What time would you like your order?
    icon_close = (MobileBy.ID,"btnClose")
    btn_select = (MobileBy.ID,"btnSetTime")


class Warning_Popup_Require_Login():
    txtview_message = (MobileBy.ID,"tvMessage") #Please login to continue
    btn_cancel = (MobileBy.ID,"btnLeft")
    btn_confirm = (MobileBy.ID,"btnRight")

class Warning_Popup_Remove_Localization():
    txtview_message = (MobileBy.ID,"subtitle") #Changing your disposition will refresh your cart. Are you sure to want to proceed?
    btn_No = (MobileBy.ID,"dialogButtonNO")
    btn_Yes = (MobileBy.ID,"dialogButtonOK")

class Warning_Popup_Oops():
    txtview_message = (MobileBy.ID, "subtitle") #Coupon not found.
    btn_Yes = (MobileBy.ID,"dialogButtonOK")
    btn_No = (MobileBy.ID,"dialogButtonNO")

class Login_Screen():
    icon_back = (MobileBy.ID,"ivBack")
    txtviewSigin = (MobileBy.ID,"tvSignin") #Sign in
    txtfield_email = (MobileBy.XPATH,"//android.widget.EditText[@text = 'Your email']")
    txtfield_pass = (MobileBy.XPATH,"//android.widget.EditText[@text = 'Your password']")
    btn_login = (MobileBy.ID,"btnLogin")

class Menu_Screen(): #not localise yet
    icon_LeftMenu = (MobileBy.ID,"toolbar_back")

    icon_Cart = (MobileBy.ID,"ivRightToolbar")
    btn_viewCart = (MobileBy.ID,"tvCheckout")

    tab_Deal = (MobileBy.XPATH,"//android.widget.TextView[@text = 'Hot Deal']")
    tab_Pizza = (MobileBy.XPATH, "//android.widget.TextView[@text = 'Pizza']")
    tab_MyBox = (MobileBy.XPATH, "//android.widget.TextView[@text = 'MY BOX']")
    tab_HutParty = (MobileBy.XPATH, "//android.widget.TextView[@text = 'HUT PARTY']")
    tab_Side = (MobileBy.XPATH, "//android.widget.TextView[@text = 'Side']")
    tab_WingStreet = (MobileBy.XPATH, "//android.widget.TextView[@text = 'WING STREET']")
    tab_DrinksDessert = (MobileBy.XPATH, "//android.widget.TextView[@text = 'Drink&Dessert']")
    tab_OriginalPricePizza = (MobileBy.XPATH, "//android.widget.TextView[@text = 'Original Price Pizza']")


class Coupon_Screen():
    # Not login yet, when User tap on "View Coupons" on Home Screen
    txtview_warningRequireLogin = (MobileBy.ID,"tvMessage") #Please log in or create a new account to enjoy coupon(s)
    btn_login = (MobileBy.ID,"btnSignIn")
    btn_createAccount = (MobileBy.ID,"btnCreateAccount")
    btn_doItLater = (MobileBy.ID,"tvClose")

    # Logined
    txtview_message = (MobileBy.ID,"tvAddingTitle") #Enter external coupon code here
    txtfield_coupon_code = (MobileBy.ID,"etAddingCouponCode")
    btn_add_coupon = (MobileBy.ID,"tvAdding")
    coupon_1_name = (MobileBy.ID, "tvCouponName")
    coupon_1_code = (MobileBy.ID,"tvCode")
    coupon_1_valid = (MobileBy.ID,"tvValidUntil")

    # Coupon Detail
    txtview_couponDetail_name = (MobileBy.ID,"tvCouponName")
    txtview_couponDetail_valid = (MobileBy.ID,"tvValidUntil")
    txtview_couponDetail_description = (MobileBy.ID,"tvCouponContent")
    btn_couponDetail_Redeem = (MobileBy.ID,"tvRedeem")

class Menu_Deal_Screen():
    item_1_hafthaft = (MobileBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@index=0]/android.widget.FrameLayout[@index = 0]")
    item_2 = (MobileBy.XPATH, "//androidx.recyclerview.widget.RecyclerView[@index=0]/android.view.ViewGroup[@index = 1]")

    item_2_name = (MobileBy.XPATH,     "//androidx.recyclerview.widget.RecyclerView[@index=0]/android.view.ViewGroup[@index=1]/android.widget.FrameLayout[@index=0]/android.view.ViewGroup[@index=0]/android.widget.LinearLayout[@index=1]/android.widget.TextView[@index=0]")
    item_2_price = (MobileBy.XPATH,
                   "//androidx.recyclerview.widget.RecyclerView[@index=0]/android.view.ViewGroup[@index=1]/android.widget.FrameLayout[@index=0]/android.view.ViewGroup[@index=0]/android.widget.TextView[@index=4]")
    # Deal Detail
    txtview_deal_name = (MobileBy.ID,"tvMenuName")
    txtview_deal_description = (MobileBy.ID,"tvMarketingDescription")
    txtlink_viewDetail = (MobileBy.ID,"btnViewDetailDescription")
    txtview_detail_content = (MobileBy.ID,"tvContent")
    txtview_comboName = (MobileBy.ID,"tvChooseComboItem") #Please choose your pizza
    icon_add = (MobileBy.ID,"btnAddComboItem")
    # Deal detail after added a pizza
    txtview_added_item_name = (MobileBy.ID,"tvComboItemName")
    txtview_added_item_name_subname = (MobileBy.ID,"tvName")
    txtview_added_item_name_price = (MobileBy.ID, "tvPrice")
    btn_plus = (MobileBy.ID,"btnPlus")
    btn_minus = (MobileBy.ID,"btnMinus")
    txtview_quatity = (MobileBy.ID,"tvQuantity")
    txtview_total_price = (MobileBy.ID,"tvButtonTotalPrice")

    # item pizza
    txtview_custom_pizza_1_name = (MobileBy.ID,"tvMenuName")
    txtview_custom_pizza_1_price = (MobileBy.ID, "tvPriceLeftButton")
    btn_add_custom_pizza_1 =  (MobileBy.ID, "tvAddLeft")

class Item_Detail_Screen():
    txtview_name = (MobileBy.ID, "tvMenuName")
    txtview_description = (MobileBy.ID, "tvMarketingDescription")
    txtlink_viewDetail = (MobileBy.ID, "btnViewDetailDescription")
    txtview_detail_content = (MobileBy.ID, "tvContent")

    btn_plus = (MobileBy.ID, "btnPlus")
    btn_minus = (MobileBy.ID, "btnMinus")
    txtview_quatity = (MobileBy.ID, "tvQuantity")
    txtview_total_price = (MobileBy.ID, "tvButtonTotalPrice")

    btn_addMoreToDeal = (MobileBy.ID,"btnAddMore")

class Menu_Pizza_Screen():
    # Pizza detail
    txtview_added_topping_name = (MobileBy.ID,"tvToppingAdded")
    txtview_removed_topping_name = (MobileBy.ID, "tvToppingRemoved")

    txt_curent_size = (MobileBy.ID,"tvPizzaName")
    btn_change_Size = (MobileBy.ID,"btnChangeSize")
    op_Topping_Default = (MobileBy.XPATH,"//android.widget.TextView[@text='Your Topping']")
    icon_remove_default_Topping =(MobileBy.ID,"ivAddTopping")
    op_AddMoreTopping = (MobileBy.XPATH, "//android.widget.TextView[@text='Add something extra']")

class Menu_MyBox_Screen():
    item_1 = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=0]/android.view.ViewGroup[@index=1]")

class Menu_HutParty_Screen():
    icon_add_product = (MobileBy.ID,"btnAddComboItem")

class Menu_Side_Screen():
    item_1 = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=0]/android.view.ViewGroup[@index=0]")

class Menu_WingStreet_Screen():
    item_1 = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=0]/android.view.ViewGroup[@index=0]")

class Menu_DrinkDessert_Screen():
    item_1 = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=0]/android.view.ViewGroup[@index=0]")

class Menu_OriginalPricePizza_Screen():
    item_1 = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=0]/android.view.ViewGroup[@index=1]")


class Require_Localise_Popup():
    txtview_message = (MobileBy.ID, "tvSelectDisposition")  # Please select the disposition method first
    op_Delivery = (MobileBy.ID, "selection_left")
    op_Collection = (MobileBy.ID, "selection_right")

class System_Permission_Localtion_Popup():
     op_allow = (MobileBy.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")

class Cart_Screen():
    btn_menu = (MobileBy.ID,"tvLeftText")
    txtview_CartEmpty = (MobileBy.ID,"tvCartEmptyDescription") #Looks like you haven't added any items to your cart yet

    #Added item to Cart
    icon_menu_navigationbar = (MobileBy.ID,"tvLeftText")
    txtview_title_localise = (MobileBy,"tvTitle")
    txtview_Address = (MobileBy.ID,"tvAddressName")
    btn_change_address = (MobileBy.ID,"tvChangeAddress")
    txtview_orderTime = (MobileBy.ID,"tvTime")
    btn_change_orderTime = (MobileBy.ID, "tvChangeTime")




class Account_Screen():
    #Banner SalesForce
    txtview_sf_name = (MobileBy.ID,"tv_user_name")
    txtview_sf_slice_no = (MobileBy.ID,"tv_slices_count")
    btn_sf_viewReward_Bennefit =(MobileBy.ID,"tv_view_rewards_benefits")

    txtview_myAccount = (MobileBy.ID,"tv_my_account") #My Account
    op_myProfile = (MobileBy.XPATH,"//android.widget.TextView[@text='My Profile']")
    op_orderHistory = (MobileBy.XPATH, "//android.widget.TextView[@text='Order History']")
    op_savedLocation = (MobileBy.XPATH, "//android.widget.TextView[@text='Saved Locations']")
    op_languageChange = (MobileBy.XPATH, "//android.widget.TextView[@text='Language/言語']")
    btn_logout = (MobileBy.ID,"btn_logout")

    # Profile
    txt_Edit_Save_Navigationbar = (MobileBy.ID,"tvRightText")
    txtfield_firstname = (MobileBy.ID,"etInput")
    txtfield_dob = (MobileBy.ID,"tvBirthDate")
    txtview_delete_account  = (MobileBy.ID,"tvDeleteAccount")

class Notification_Screen():
    txt_Notification1_title = (MobileBy.ID,"tvTitle")
    txt_Notification1_content = (MobileBy.ID, "tvContent")
    txt_Notification1_time = (MobileBy.ID, "tvTime")

class OrderHistory_Screen():
    btn_latest_order = (MobileBy.ID,"clRecentOrder")
    txtview_order_ID = (MobileBy.ID,"tvOrderId")
    txtview_address = (MobileBy.ID,"tvAddress")
    txtview_subAddress = (MobileBy.ID,"tvSubAddress")
    txtview_order_time =(MobileBy.ID,"tvTime")
    txtview_order_price = (MobileBy.ID,"tvTotalPrice")
    btn_order_detail = (MobileBy.XPATH,"//android.widget.TextView[@text='View Detail']")

class Latest_Order_Screen():
    txtview_estimateTime = (MobileBy.ID,"tvEstimateTime")
    txtview_order_ID = (MobileBy.ID,"tvOrderId")
    txtview_earn_slices_from_this_order = (MobileBy.ID,"tv_you_will_earn_slices_from_this_order")
    btn_backtoHome =(MobileBy.ID,"btnBackToHome")

class OrderDetail_Screen():
    txtview_order_ID = (MobileBy.ID,"tvOrderId")
    txtview_earn_slices_from_this_order = (MobileBy.ID, "tv_you_will_earn_slices_from_this_order")

class SavedAddress_Screen():
    #Looks like you haven't any saved address yet. Let's order and your address will be saved here.
    txtview_empltymessage = (MobileBy.ID,"tvEmptyMessage")

    txtview_address_1 = (MobileBy.ID,"tvAddress")
    icon_favourite_2 = (MobileBy.XPATH,"//android.view.ViewGroup[@index=1]/android.view.ViewGroup[@index=0]/android.widget.ImageView[@index=0]")
    icon_delete_1 = (MobileBy.ID,'ivDeleteLocation')

class SalesForce_Screen():
    tab_Rewards = (MobileBy.XPATH,"//android.widget.TextView[@text='Rewards']")
    btn_viewAllReward = (MobileBy.ID, "ll_view_all_available_rewards")
    btn_Slice_History = (MobileBy.ID,"btn_slices_history")
    txtview_item_1_name = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=1]/android.widget.FrameLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=1]")
    txtview_item_1_slice = (MobileBy.XPATH,
                           "//androidx.recyclerview.widget.RecyclerView[@index=1]/android.widget.FrameLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=2]")
    btn_item_1_redeem = (MobileBy.XPATH,
                           "//androidx.recyclerview.widget.RecyclerView[@index=1]/android.widget.FrameLayout[@index=0]/android.widget.LinearLayout[@index=0]/android.widget.TextView[@index=3]")
    tab_Tier_Benefits = (MobileBy.XPATH, "//android.widget.TextView[@text='Tier Benefits']")

    txtview_history_title = (MobileBy.ID,"tv_title") #Slices History
    txtview_history_name_1 = (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=2]/android.view.ViewGroup[@index=1]/android.widget.TextView[@index=0]")
    txtview_history_date_1= (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=2]/android.view.ViewGroup[@index=1]/android.widget.TextView[@index=1]")
    txtview_history_slice_no_1= (MobileBy.XPATH,"//androidx.recyclerview.widget.RecyclerView[@index=2]/android.view.ViewGroup[@index=1]/android.widget.TextView[@index=2]")

    # Tier benefit
    tab_Regular = (MobileBy.XPATH,"//android.widget.TextView[@text='  REGULAR']")
    tab_Silver = (MobileBy.XPATH, "//android.widget.TextView[@text='  SILVER']")
    tab_Gold = (MobileBy.XPATH, "//android.widget.TextView[@text='  GOLD']")
    tab_VIP = (MobileBy.XPATH, "//android.widget.TextView[@text='  VIP']")

    txtview_benefit_1_name =(MobileBy.ID,"tv_title")
    txtview_benefit_1_des = (MobileBy.ID,"tv_description")

