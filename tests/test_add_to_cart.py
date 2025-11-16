"""
Test cases for Add to Cart functionality
Verifies cart operations and price calculations
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from conftest import VALID_USERNAME, VALID_PASSWORD


@pytest.fixture
def logged_in_driver(driver_with_screenshot):
    """Fixture to login before each test"""
    login_page = LoginPage(driver_with_screenshot)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return driver_with_screenshot


class TestAddToCart:
    
    def test_add_single_product_to_cart(self, logged_in_driver):
        """TC_010: Verify adding single product to cart"""
        products_page = ProductsPage(logged_in_driver)
        products_page.add_product_to_cart_by_index(0)
        
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == "1", "Cart badge should show 1 item"

    def test_add_multiple_products_to_cart(self, logged_in_driver):
        """TC_011: Verify adding multiple products to cart"""
        products_page = ProductsPage(logged_in_driver)
        products_page.add_multiple_products_to_cart(3)
        
        cart_count = products_page.get_cart_badge_count()
        assert cart_count == "3", "Cart badge should show 3 items"

    def test_verify_cart_quantity(self, logged_in_driver):
        """TC_012: Verify cart quantity after adding products"""
        products_page = ProductsPage(logged_in_driver)
        products_page.add_product_to_cart_by_index(0)
        products_page.click_cart_icon()
        
        cart_page = CartPage(logged_in_driver)
        assert cart_page.is_cart_page_displayed(), "Cart page should be displayed"
        assert cart_page.get_cart_item_count() == 1, "Cart should contain 1 item"
        
        quantities = cart_page.get_item_quantities()
        assert quantities[0] == "1", "Item quantity should be 1"

    def test_validate_cart_total_price(self, logged_in_driver):
        """TC_013: Verify cart total price calculation"""
        products_page = ProductsPage(logged_in_driver)
        products_page.add_multiple_products_to_cart(2)
        products_page.click_cart_icon()
        
        cart_page = CartPage(logged_in_driver)
        total_price = cart_page.calculate_total_price()
        
        assert total_price > 0, "Total price should be greater than 0"
        assert cart_page.get_cart_item_count() == 2, "Cart should contain 2 items"

    def test_verify_product_details_in_cart(self, logged_in_driver):
        """TC_014: Verify product details are displayed in cart"""
        products_page = ProductsPage(logged_in_driver)
        products_page.add_product_to_cart_by_index(0)
        products_page.click_cart_icon()
        
        cart_page = CartPage(logged_in_driver)
        item_names = cart_page.get_item_names()
        item_prices = cart_page.get_item_prices()
        
        assert len(item_names) > 0, "Item names should be displayed"
        assert len(item_prices) > 0, "Item prices should be displayed"
        assert "$" in item_prices[0], "Price should contain $ symbol"

    def test_remove_item_from_cart(self, logged_in_driver):
        """TC_015: Verify removing item from cart"""
        products_page = ProductsPage(logged_in_driver)
        products_page.add_multiple_products_to_cart(2)
        products_page.click_cart_icon()
        
        cart_page = CartPage(logged_in_driver)
        initial_count = cart_page.get_cart_item_count()
        assert initial_count == 2, "Cart should initially have 2 items"
        
        cart_page.remove_item_by_index(0)
        final_count = cart_page.get_cart_item_count()
        assert final_count == 1, "Cart should have 1 item after removal"

    def test_empty_cart_verification(self, logged_in_driver):
        """TC_016: Verify empty cart state"""
        products_page = ProductsPage(logged_in_driver)
        products_page.click_cart_icon()
        
        cart_page = CartPage(logged_in_driver)
        assert cart_page.is_cart_empty(), "Cart should be empty"
        assert cart_page.get_cart_item_count() == 0, "Cart count should be 0"
