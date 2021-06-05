"""
Module for fixtures
"""
import pytest
from appium import webdriver
from Library.config import Config


class DriverInit: #pylint: disable=too-few-public-methods
    """
    Fixtures
    """

    @classmethod
    @pytest.fixture(autouse=True)
    def driver_init(cls, request):
        """
        Mobile Option
        """
        if Config.MOBILE.upper() == 'PIXEL':
            driver = webdriver.Remote("http://localhost:4723/wd/hub", Config.DC1)

        request.cls.driver = driver
        driver.implicitly_wait(30)
        yield
        driver.quit()
