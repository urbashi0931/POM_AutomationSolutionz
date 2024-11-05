from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    # Locators for elements on the login page
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginbtn")
    
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_username(self, username: str):
        """Enter the username in the username field."""
        username_field = self.driver.find_element(*self.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password: str):
        """Enter the password in the password field."""
        password_field = self.driver.find_element(*self.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        """Click the login button."""
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def login(self, username: str, password: str):
        """Full login method to enter username, password, and click login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()




