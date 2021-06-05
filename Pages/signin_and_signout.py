"""
Automation Script for Hungama music
"""
from Library.config import Config
from Library.web_utilities import CommonUtility
from Library.file_library import ReadJson
from Pages.basepage import BasePage

read_json = ReadJson()
com_util = CommonUtility()
element = read_json.read_locators(Config.OBJECT_JSON)


class SignInSignOut(BasePage):
    """
    class for signin and signout activity
    """

    def __init__(self, driver, email, password):
        super().__init__(driver, email, password)

    def sign_out(self):
        """
        click on the profile icon, then on more.
        click on logout and click on yes.
        """
        com_util.tap_on(self.driver, element['clickOnProfile'])
        com_util.tap_on(self.driver, element['clickOnMore'])
        com_util.tap_on(self.driver, element['clickOnLogout'])
        com_util.tap_on(self.driver, element['clickOnYes'])
