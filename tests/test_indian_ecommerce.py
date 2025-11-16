"""
Test cases for Indian E-Commerce Demo Site
Tests products priced in Indian Rupees (₹)
"""
import pytest
import os
from pages.indian_login_page import IndianLoginPage
from pages.indian_products_page import IndianProductsPage
from pages.indian_cart_page import IndianCartPage


# Test data for Indian demo
INDIAN_DEMO_URL = "file:///" + os.path.abspath("demo_site/indian_ecommerce.html").replace("\\", "/")
VALID_USERNAME = "test_user"
VALID_PASSWORD = "test123"


@pytest.fixture
def indian_driver(driver_with_screenshot):
    """Setup driver for Indian demo site"""
    driver_with_screenshot.get(INDIAN_DEMO_URL)
    return driver_with_screenshot


@pytest.fixture
def logged_in_indian_driver(indian_driver):
    """Fixture to login to Indian demo before each test"""
    login_page = IndianLoginPage(indian_driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return indian_driver


class TestIndianLogin:
    """Test cases for Indian E-Commerce Login"""
    
    def test_login_with_valid_credentials(self, indian_driver):
        """TC_IND_001: Verify login with valid credentials"""
        login_page = IndianLoginPage(indian_driver)
        login_page.login(VALID_USERNAME, VALID_PASSWORD)
        
        products_page = IndianProductsPage(indian_driver)
        assert products_page.is_products_page_displayed(), "Products page should be displayed"
        assert products_page.get_page_title() == "Products", "Page title should be 'Products'"

    def test_login_with_invalid_credentials(self, indian_driver):
        """TC_IND_002: Verify login with invalid credentials"""
        login_page = IndianLoginPage(indian_driver)
        login_page.login("wrong_user", "wrong_pass")
        
        assert login_page.is_error_displayed(), "Error message should be displayed"

    def test_login_with_empty_credentials(self, indian_driver):
        """TC_IND_003: Verify login with empty credentials"""
        login_page = IndianLoginPage(indian_driver)
        login_page.login("", "")
        
        assert login_page.is_error_displayed(), "Error message should be displayed"


class TestIndianProducts:
    """Test cases for Indian E-Commerce Products"""
    
    def test_products_display_in_rupees(self, logged_in_indian_driver):
        """TC_IND_004: Verify products are displayed with ₹ symbol"""
        products_page = IndianProductsPage(logged_in_indian_driver)
        
        assert products_page.is_products_page_displayed(), "Products page should be displayed"
        product_count = products_page.get_product_count()
        assert product_count == 6, "Should display 6 products"
        
        # Verify all prices have ₹ symbol
        prices = products_page.get_product_prices()
        assert all("₹" in price for price in prices), "All prices should have ₹ symbol"

    def test_product_names_are_indian(self, logged_in_indian_driver):
        """TC_IND_005: Verify product names are displayed"""
        products_page = IndianProductsPage(logged_in_indian_driver)
        
        product_names = products_page.get_product_names()
        assert len(product_names) > 0, "Product names should be visible"
        
        # Verify we have Indian products
        expected_products = ["Samsung", "HP", "Sony", "Canon", "Apple", "JBL"]
        assert any(brand in " ".join(product_names) for brand in expected_products), \
            "Should have recognizable product brands"

    def test_add_product_to_cart(self, logged_in_indian_driver):
        """TC_IND_006: Verify adding product to cart"""
        products_page = IndianProductsPage(logged_in_indian_driver)
        products_page.add_product_to_cart_by_index(0)
        
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == "1", "Cart badge should show 1 item"


class TestIndianCart:
    """Test cases for Indian E-Commerce Shopping Cart"""
    
    def test_cart_displays_rupee_prices(self, logged_in_indian_driver):
        """TC_IND_007: Verify cart displays prices in rupees"""
        products_page = IndianProductsPage(logged_in_indian_driver)
        products_page.add_product_to_cart_by_index(0)
        products_page.click_cart_icon()
        
        cart_page = IndianCartPage(logged_in_indian_driver)
        assert cart_page.is_cart_page_displayed(), "Cart page should be displayed"
        
        prices = cart_page.get_item_prices()
        assert all("₹" in price for price in prices), "All cart prices should have ₹ symbol"

    def test_cart_total_calculation_in_rupees(self, logged_in_indian_driver):
        """TC_IND_008: Verify cart total is calculated correctly in rupees"""
        products_page = IndianProductsPage(logged_in_indian_driver)
        products_page.add_multiple_products_to_cart(2)
        products_page.click_cart_icon()
        
        cart_page = IndianCartPage(logged_in_indian_driver)
        total = cart_page.calculate_total_price()
        
        assert total > 0, "Total price should be greater than 0"
        assert cart_page.get_cart_item_count() == 2, "Cart should contain 2 items"
        
        # Verify total amount display has ₹ symbol
        total_display = cart_page.get_total_amount()
        assert "₹" in total_display, "Total amount should display ₹ symbol"

    def test_remove_item_from_cart(self, logged_in_indian_driver):
        """TC_IND_009: Verify removing item from cart"""
        products_page = IndianProductsPage(logged_in_indian_driver)
        products_page.add_multiple_products_to_cart(2)
        products_page.click_cart_icon()
        
        cart_page = IndianCartPage(logged_in_indian_driver)
        initial_count = cart_page.get_cart_item_count()
        assert initial_count == 2, "Cart should initially have 2 items"
        
        cart_page.remove_item_by_index(0)
        final_count = cart_page.get_cart_item_count()
        assert final_count == 1, "Cart should have 1 item after removal"

    def test_empty_cart_display(self, logged_in_indian_driver):
        """TC_IND_010: Verify empty cart state"""
        products_page = IndianProductsPage(logged_in_indian_driver)
        products_page.click_cart_icon()
        
        cart_page = IndianCartPage(logged_in_indian_driver)
        assert cart_page.is_cart_empty(), "Cart should be empty"
        assert cart_page.get_cart_item_count() == 0, "Cart count should be 0"


class TestIndianLogout:
    """Test cases for Indian E-Commerce Logout"""
    
    def test_logout_functionality(self, logged_in_indian_driver):
        """TC_IND_011: Verify logout functionality"""
        products_page = IndianProductsPage(logged_in_indian_driver)
        assert products_page.is_products_page_displayed(), "User should be logged in"
        
        products_page.logout()
        
        login_page = IndianLoginPage(logged_in_indian_driver)
        assert login_page.is_login_page(), "Should be redirected to login page"
