"""
Base Page class containing common methods used across all page objects
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Find element with explicit wait"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise Exception(f"Element not found: {locator}")

    def find_elements(self, locator):
        """Find multiple elements"""
        try:
            return self.wait.until(EC.presence_of_all_elements_located(locator))
        except TimeoutException:
            return []

    def click(self, locator):
        """Click on element with explicit wait"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """Enter text into input field"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from element"""
        element = self.find_element(locator)
        return element.text

    def is_element_displayed(self, locator):
        """Check if element is displayed"""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False

    def get_current_url(self):
        """Get current page URL"""
        return self.driver.current_url
