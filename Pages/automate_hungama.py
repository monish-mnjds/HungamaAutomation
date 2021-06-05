"""
Automation Script for Hungama music
"""
from Library.config import Config
from Library.web_utilities import CommonUtility
from Library.file_library import ReadJson

read_json = ReadJson()
com_util = CommonUtility()
element = read_json.read_locators(Config.OBJECT_JSON)


class Hungama:
    """
    Test cases
    """
    def __init__(self, driver, email, password):
        self.driver = driver
        self.email = email
        self.password = password

    def click_on_at(self):
        """
        clicking on the at sign for log-in
        """
        com_util.tap_on(self.driver, element['clickOnAtSign'])

    def click_on_skip(self):
        """
        clicking on the skip button
        """
        com_util.tap_on(self.driver, element['Skip'])

    def enter_email(self):
        """
        entering email in the field
        """
        com_util.send_to(self.driver, element['clickOnEmail'], self.email)

    def enter_password(self):
        """
        entering the password in the field
        """
        com_util.send_to(self.driver, element['clickOnPassword'], self.password)

    def click_on_login(self):
        """
        clicking the login button
        """
        com_util.tap_on(self.driver, element['clickOnLogin'])

    def wait_to_load(self):
        """
        waiting for content to load
        """
        com_util.wait_for(self.driver, element['waitToLoad'])

    def click_on_continue(self):
        """
        clicking on the continue button
        """
        com_util.tap_on(self.driver, element['clickOnContinue'])

    def click_on_profile(self):
        """
        clicking on the profile icon
        """
        com_util.tap_on(self.driver, element['clickOnProfile'])

    def click_on_more(self):
        """
        Clicking on More Option
        """
        com_util.tap_on(self.driver, element['clickOnMore'])

    def click_on_logout(self):
        """
        clicking on logout option
        """
        com_util.tap_on(self.driver, element['clickOnLogout'])

    def click_on_yes(self):
        """
        clicking on yes in the alert
        """
        com_util.tap_on(self.driver, element['clickOnYes'])
