
import time


from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)


class BasePageForWebsite:

    def __init__(self, driver):
        self.driver = driver

    def isID(self, element):
        if (element[0] == "id"):
            return True
        else:
            return False

    def waiting(self, element):
        # delay(0.5)
        log.logger.info("[WAITING] showed element: " + element[1])
        try:
            wait = WebDriverWait(self.driver, 20)
            if self.isID(element):
                currently_waiting_for = wait.until(EC.element_to_be_clickable((By.ID, element[1])))
            else:
                currently_waiting_for = wait.until(EC.element_to_be_clickable((By.XPATH, element[1])))
        except():
            log.logger.info("[WATING] error element: " + element[1])

    def click(self, element):
        self.waiting(element)
        log.logger.info("[CLICK] " + element[1])
        if self.isID(element):
            self.driver.find_element_by_id(element[1]).click()
        else:
            self.driver.find_element_by_xpath(element[1]).click()

    def input(self, element, value):
        self.waiting(element)
        log.logger.info("[INPUT] " + element[1])
        if self.isID(element):
            self.driver.find_element_by_id(element[1]).send_keys(value)
        else:
            self.driver.find_element_by_xpath(element[1]).send_keys(value)
        log.logger.info("[INPUT] with value: " + value)

    def getText(self, element):
        self.waiting(element)
        log.logger.info("[GETTEXT] " + element[1])
        if self.isID(element):
            text = self.driver.find_element_by_id(element[1]).text
        else:
            text = self.driver.find_element_by_xpath(element[1]).text
        log.logger.info("[GETTEXT] text is: " + text)
        return text

    def verifyTextview(self, element, expected_text):
        text = self.getText(element)
        log.logger.info("[VERIFY] expected is: " + expected_text)
        assert text == expected_text

    def scrollToText(self, text):
        log.logger.info("[ScrollDownToText] text: " + text)
        i = 1
        while i < 10:
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath("//android.widget.TextView[@text='"+text+"']")
                log.logger.info("[ScrollDownToText] text: " + text+" - showed")
                break
            except:
                self.scroll_down()
            i += 1
    def scrollToTextAndClick(self, text):
        log.logger.info("[ScrollDownToText] text: " + text)
        i = 1
        while i < 10:
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath("//android.widget.TextView[@text='" + text + "']").click()
                log.logger.info("[ScrollDownToText and Click] text: " + text+" - showed")
                break
            except:
                self.scroll_down()
            i += 1


    def scroll_down(self):
        log.logger.info("[SCROLL DOW]")
        width_device = self.driver.get_window_size()['width']
        hight_device = self.driver.get_window_size()['height']
        # scroll a to b
        start_x = width_device / 2
        start_y = hight_device * 3 / 4
        end_x = width_device / 2
        end_y = hight_device * 1 / 5
        # end_y = 0
        action = TouchAction(self.driver)
        action.long_press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    # def clickIndex(self, locator, index):
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_elements_by_xpath(configReader.readConfig("locators", locator))[index].click()
    #     elif str(locator).endswith("_ACCESSIBILITYID"):
    #         self.driver.find_elements_by_accessibility_id(configReader.readConfig("locators", locator))[index].click()
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_elements_by_id(configReader.readConfig("locators", locator))[index].click()
    #     log.logger.info("Clicking on an Element "+ str(locator) + "with index : " + str(index))

    def scroll_half_down(self):
        time.sleep(1)
        log.logger.info("[SCROLL HALF DOW]")
        width_device = self.driver.get_window_size()['width']
        hight_device = self.driver.get_window_size()['height']
        # scroll a to b
        start_x = width_device / 2
        start_y = hight_device * 2 / 3
        end_x = width_device / 2
        end_y = hight_device * 9 / 10
        # end_y = 0
        action = TouchAction(self.driver)
        action.long_press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()


    def scroll_up(self):
        log.logger.info("[SCROLL UP]")
        width_device = self.driver.get_window_size()['width']
        hight_device = self.driver.get_window_size()['height']
        # scroll a to b
        start_x = width_device / 2
        start_y = hight_device * 1 / 5
        end_x = width_device / 2
        end_y = hight_device * 3 / 4
        # end_y = 0
        action = TouchAction(self.driver)
        action.long_press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()