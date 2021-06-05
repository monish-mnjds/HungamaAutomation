"""
Automation Script for Hungama music
"""
from Library.config import Config
from Library.web_utilities import CommonUtility
from Library.file_library import ReadJson

read_json = ReadJson()
com_util = CommonUtility()
element = read_json.read_locators(Config.OBJECT_JSON)


class BasePage:
    """
    Creating methods which are common to all the page
    """
    def __init__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password

    def open_login_page(self):
        """
        clicking on the at sign for log-in
        """
        com_util.tap_on(self.driver, element['clickOnAtSign'])

    def set_user_inputs(self):
        """
        Enter email and password, then click on login btn
        """
        com_util.send_to(self.driver, element['clickOnEmail'], self.email)
        com_util.send_to(self.driver, element['clickOnPassword'], self.password)
        com_util.tap_on(self.driver, element['clickOnLogin'])

    def open_home_page(self):
        """
        waiting for the element to get loaded and click continue btn
        """
        com_util.wait_for(self.driver, element['waitToLoad'])
        com_util.tap_on(self.driver, element['clickOnContinue'])
