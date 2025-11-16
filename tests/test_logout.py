"""
Test cases for Logout functionality
Verifies user can successfully logout
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from conftest import VALID_USERNAME, VALID_PASSWORD, BASE_URL


@pytest.fixture
def logged_in_driver(driver_with_screenshot):
    """Fixture to login before each test"""
    login_page = LoginPage(driver_with_screenshot)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return driver_with_screenshot


class TestLogout:
    
    def test_logout_successfully(self, logged_in_driver):
        """TC_017: Verify logout functionality"""
        products_page = ProductsPage(logged_in_driver)
        assert products_page.is_products_page_displayed(), "User should be logged in"
        
        products_page.logout()
        
        login_page = LoginPage(logged_in_driver)
        assert login_page.is_login_page(), "Should be redirected to login page"
        assert logged_in_driver.current_url == BASE_URL, "URL should be login page URL"

    def test_logout_and_relogin(self, logged_in_driver):
        """TC_018: Verify logout and re-login workflow"""
        products_page = ProductsPage(logged_in_driver)
        products_page.logout()
        
        # Re-login
        login_page = LoginPage(logged_in_driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        
        products_page = ProductsPage(logged_in_driver)
        assert products_page.is_products_page_displayed(), "User should be able to login again"
        assert products_page.get_page_title() == "Products", "Should be on products page"
