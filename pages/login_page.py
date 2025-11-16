"""
Page Object Model for Login Page
Contains all elements and actions related to login functionality
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    ERROR_CLOSE_BUTTON = (By.CLASS_NAME, "error-button")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        """Enter username in the username field"""
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enter password in the password field"""
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """Click on the login button"""
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Complete login action"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self):
        """Get error message text"""
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self):
        """Check if error message is displayed"""
        return self.is_element_displayed(self.ERROR_MESSAGE)

    def is_login_page(self):
        """Verify if on login page"""
        return self.is_element_displayed(self.LOGIN_BUTTON)
