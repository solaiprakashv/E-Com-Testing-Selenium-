"""
Test cases for Products Page functionality
Verifies product listing and display
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from conftest import VALID_USERNAME, VALID_PASSWORD


@pytest.fixture
def logged_in_driver(driver_with_screenshot):
    """Fixture to login before each test"""
    login_page = LoginPage(driver_with_screenshot)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return driver_with_screenshot


class TestProducts:
    
    def test_products_page_loads_correctly(self, logged_in_driver):
        """TC_006: Verify products page loads after login"""
        products_page = ProductsPage(logged_in_driver)
        
        assert products_page.is_products_page_displayed(), "Products page should be displayed"
        assert products_page.get_page_title() == "Products", "Page title should be 'Products'"

    def test_products_are_displayed(self, logged_in_driver):
        """TC_007: Verify products are displayed on the page"""
        products_page = ProductsPage(logged_in_driver)
        
        product_count = products_page.get_product_count()
        assert product_count > 0, "Products should be displayed"
        assert product_count == 6, "Should display 6 products"

    def test_product_names_are_visible(self, logged_in_driver):
        """TC_008: Verify product names are visible"""
        products_page = ProductsPage(logged_in_driver)
        
        product_names = products_page.get_product_names()
        assert len(product_names) > 0, "Product names should be visible"
        assert all(name for name in product_names), "All products should have names"

    def test_product_prices_are_visible(self, logged_in_driver):
        """TC_009: Verify product prices are visible"""
        products_page = ProductsPage(logged_in_driver)
        
        product_prices = products_page.get_product_prices()
        assert len(product_prices) > 0, "Product prices should be visible"
        assert all("$" in price for price in product_prices), "All prices should have $ symbol"
