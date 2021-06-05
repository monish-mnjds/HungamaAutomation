"""
Module for testing signin and signout
"""
import pytest
from Pages.signin_and_signout import SignInSignOut
from Library.config import Config
from Library.file_library import ReadJson
from Library.base_fixtures import DriverInit

ReadTestData = ReadJson()
test_data1, test_data2, test_data3, test_data4 = ReadTestData.read_test_data(Config.TEST_JSON)


@pytest.mark.parametrize(
    """email, password""",
    test_data1
)
@pytest.mark.login
class TestLogin(DriverInit):
    """
    Testing the login and logout
    """
    def testing_login(self, email, password):
        """
        signing in and out
        """
        log_in = SignInSignOut(self.driver, email, password)
        log_in.open_login_page()
        log_in.set_user_inputs()
        log_in.open_home_page()
        log_in.sign_out()
