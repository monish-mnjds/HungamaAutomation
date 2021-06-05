"""
Module for common functionalities
"""
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class CommonUtility:
    """
    for reusing mouse and keyboard actions
    """
    @staticmethod
    def send_and_enter(driver):
        """
        sending and pressing enter
        """
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER).perform()

    @staticmethod
    def send_to(driver, element, string):
        """
        to enter the text
        """
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value).send_keys(string)

    @staticmethod
    def wait_for(driver, element):
        """
        waiting for the page to load
        """
        loc_type, loc_value = element
        driver.find_element(loc_type, loc_value)

    @staticmethod
    def check_display(driver, element):
        """
        checking whether the element is displayed
        """
        loc_type, loc_value = element
        return driver.find_element(loc_type, loc_value).is_displayed()

    @staticmethod
    def find_text(driver, element):
        """
        Waiting for the page to load
        """
        loc_type, loc_value = element
        return driver.find_element(loc_type, loc_value).text

    @staticmethod
    def check_select(driver, element):
        """
        checking whether the element is displayed
        """
        loc_type, loc_value = element
        return driver.find_element(loc_type, loc_value).is_selected()

    @staticmethod
    def tap_on(driver, element):
        """
        tapping on the element
        """
        loc_type, loc_value = element
        actions = TouchAction(driver)
        actions.tap(driver.find_element(loc_type, loc_value)).perform()

    @staticmethod
    def swipe_it(driver, element1, element2):
        """
        swiping
        """
        loc_type1, loc_value1 = element1
        loc_type2, loc_value2 = element2
        actions = TouchAction(driver)
        actions.long_press(driver.find_element(loc_type1, loc_value1), 1000)
        actions.move_to(driver.find_element(loc_type2, loc_value2)).release().perform()
