import pytest
from selenium.common.exceptions import TimeoutException
from Pages.LoginPage import LoginPage
from Configs.configs import TestData
import time


@pytest.mark.usefixtures('init_driver')
class TestClass:

    # Positive scenario
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login(TestData.GOOD_USER, TestData.PASSWORD)
        time.sleep(3)
        sign_in_success_check = self.loginPage.is_sign_in_visible(TestData.PRODUCTS_LOCATOR)
        assert sign_in_success_check is True

    # Negative scenario
    def test_login_failure(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login(TestData.BAD_USER, TestData.PASSWORD)
        time.sleep(3)
        try:
            sign_in_success_check = self.loginPage.is_sign_in_visible(TestData.PRODUCTS_LOCATOR)
        except TimeoutException:
            sign_in_success_check = False

        assert sign_in_success_check is False
