from selenium.webdriver.common.by import By
from Pages.Utils import Utilities
from Configs.configs import TestData


class LoginPage(Utilities):
    EMAIL = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.NAME, 'login-button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def is_sign_in_visible(self, locator):
        return self.is_visible(locator)

    def login(self, username, password):
        self.send_keys(self.EMAIL, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
