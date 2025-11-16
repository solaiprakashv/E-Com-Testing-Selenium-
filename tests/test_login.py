"""
Test cases for Login functionality
Covers positive and negative login scenarios
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from conftest import VALID_USERNAME, VALID_PASSWORD


class TestLogin:
    
    def test_login_with_valid_credentials(self, driver_with_screenshot):
        """TC_001: Verify login with valid credentials"""
        login_page = LoginPage(driver_with_screenshot)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        
        products_page = ProductsPage(driver_with_screenshot)
        assert products_page.is_products_page_displayed(), "Products page should be displayed"
        assert products_page.get_page_title() == "Products", "Page title should be 'Products'"

    def test_login_with_invalid_username(self, driver_with_screenshot):
        """TC_002: Verify login with invalid username"""
        login_page = LoginPage(driver_with_screenshot)
        login_page.login("invalid_user", VALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_msg = login_page.get_error_message()
        assert "Username and password do not match" in error_msg, "Error message should indicate invalid credentials"

    def test_login_with_invalid_password(self, driver_with_screenshot):
        """TC_003: Verify login with invalid password"""
        login_page = LoginPage(driver_with_screenshot)
        login_page.login(VALID_USERNAME, "wrong_password")
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_msg = login_page.get_error_message()
        assert "Username and password do not match" in error_msg, "Error message should indicate invalid credentials"

    def test_login_with_empty_credentials(self, driver_with_screenshot):
        """TC_004: Verify login with empty credentials"""
        login_page = LoginPage(driver_with_screenshot)
        login_page.login("", "")
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_msg = login_page.get_error_message()
        assert "Username is required" in error_msg, "Error message should indicate username is required"

    def test_login_with_locked_user(self, driver_with_screenshot):
        """TC_005: Verify login with locked out user"""
        login_page = LoginPage(driver_with_screenshot)
        login_page.login("locked_out_user", VALID_PASSWORD)
        
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_msg = login_page.get_error_message()
        assert "locked out" in error_msg, "Error message should indicate user is locked out"
