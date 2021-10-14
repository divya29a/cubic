from selenium.webdriver.common.by import By


class TestData:
    CHROME_EXECUTABLE_PATH = r"E:\chromedriver_win32\chromedriver.exe"
    BASE_URL = 'https://www.saucedemo.com'
    GOOD_USER = 'standard_user'
    BAD_USER = "locked_out_user"
    PASSWORD = 'secret_sauce'
    PRODUCTS_LOCATOR = (By.XPATH, "//span[@class='title']")
