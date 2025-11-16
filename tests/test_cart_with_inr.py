"""
Test cases for Shopping Cart with INR Currency Conversion
Shows prices in both USD and INR
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.currency_converter import CurrencyConverter
from conftest import VALID_USERNAME, VALID_PASSWORD


@pytest.fixture
def logged_in_driver(driver_with_screenshot):
    """Fixture to login before each test"""
    login_page = LoginPage(driver_with_screenshot)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return driver_with_screenshot


class TestCartWithINR:
    """Test cart functionality with INR conversion"""
    
    def test_cart_price_in_inr(self, logged_in_driver):
        """TC_INR_001: Verify cart prices with INR conversion"""
        products_page = ProductsPage(logged_in_driver)
        products_page.add_product_to_cart_by_index(0)
        products_page.click_cart_icon()
        
        cart_page = CartPage(logged_in_driver)
        assert cart_page.is_cart_page_displayed(), "Cart page should be displayed"
        
        # Get prices in USD
        usd_prices = cart_page.get_item_prices()
        
        print("\n" + "="*60)
        print("  CART PRICES - USD vs INR")
        print("="*60)
        
        for i, usd_price in enumerate(usd_prices, 1):
            inr_price = CurrencyConverter.convert_and_format(usd_price)
            print(f"Item {i}: {usd_price} = {inr_price}")
        
        print("="*60)
        
        assert len(usd_prices) > 0, "Cart should have items"

    def test_cart_total_in_both_currencies(self, logged_in_driver):
        """TC_INR_002: Verify cart total in both USD and INR"""
        products_page = ProductsPage(logged_in_driver)
        products_page.add_multiple_products_to_cart(3)
        products_page.click_cart_icon()
        
        cart_page = CartPage(logged_in_driver)
        
        # Calculate total in USD
        total_usd = cart_page.calculate_total_price()
        
        # Convert to INR
        total_inr = CurrencyConverter.usd_to_inr(total_usd)
        
        print("\n" + "="*60)
        print("  CART TOTAL - DUAL CURRENCY")
        print("="*60)
        print(f"Total in USD: {CurrencyConverter.format_usd(total_usd)}")
        print(f"Total in INR: {CurrencyConverter.format_inr(total_inr)}")
        print(f"Exchange Rate: 1 USD = {CurrencyConverter.USD_TO_INR} INR")
        print("="*60)
        
        assert total_usd > 0, "Total should be greater than 0"
        assert total_inr > 0, "INR total should be greater than 0"

    def test_individual_product_prices_conversion(self, logged_in_driver):
        """TC_INR_003: Verify individual product price conversion"""
        products_page = ProductsPage(logged_in_driver)
        
        # Get product prices from products page
        usd_prices = products_page.get_product_prices()
        
        print("\n" + "="*60)
        print("  PRODUCT PRICES - USD TO INR CONVERSION")
        print("="*60)
        
        for i, usd_price in enumerate(usd_prices, 1):
            dual_display = CurrencyConverter.get_dual_currency_display(usd_price)
            print(f"Product {i}: {dual_display}")
        
        print("="*60)
        
        assert len(usd_prices) > 0, "Should have product prices"
        assert all("$" in price for price in usd_prices), "All prices should have $ symbol"

    def test_price_comparison_usd_vs_inr(self, logged_in_driver):
        """TC_INR_004: Compare prices in USD vs INR"""
        products_page = ProductsPage(logged_in_driver)
        products_page.add_product_to_cart_by_index(0)
        products_page.add_product_to_cart_by_index(1)
        products_page.click_cart_icon()
        
        cart_page = CartPage(logged_in_driver)
        
        # Get all item prices
        usd_prices = cart_page.get_item_prices()
        item_names = cart_page.get_item_names()
        
        print("\n" + "="*60)
        print("  DETAILED PRICE COMPARISON")
        print("="*60)
        
        for name, usd_price in zip(item_names, usd_prices):
            usd_amount = CurrencyConverter.parse_usd(usd_price)
            inr_amount = CurrencyConverter.usd_to_inr(usd_amount)
            
            print(f"\nProduct: {name}")
            print(f"  USD: {CurrencyConverter.format_usd(usd_amount)}")
            print(f"  INR: {CurrencyConverter.format_inr(inr_amount)}")
            print(f"  Savings in INR: ₹{inr_amount - usd_amount:,.2f}")
        
        print("\n" + "="*60)
        
        assert len(usd_prices) == 2, "Should have 2 items in cart"

    def test_bulk_purchase_savings_in_inr(self, logged_in_driver):
        """TC_INR_005: Calculate bulk purchase total in INR"""
        products_page = ProductsPage(logged_in_driver)
        
        # Add all products to cart
        product_count = products_page.get_product_count()
        products_page.add_multiple_products_to_cart(product_count)
        products_page.click_cart_icon()
        
        cart_page = CartPage(logged_in_driver)
        
        # Calculate totals
        total_usd = cart_page.calculate_total_price()
        total_inr = CurrencyConverter.usd_to_inr(total_usd)
        
        print("\n" + "="*60)
        print("  BULK PURCHASE SUMMARY")
        print("="*60)
        print(f"Total Items: {cart_page.get_cart_item_count()}")
        print(f"Total in USD: {CurrencyConverter.format_usd(total_usd)}")
        print(f"Total in INR: {CurrencyConverter.format_inr(total_inr)}")
        print(f"\nIf paying in INR, you're spending:")
        print(f"  ₹{total_inr:,.2f}")
        print(f"\nExchange Rate: 1 USD = ₹{CurrencyConverter.USD_TO_INR}")
        print("="*60)
        
        assert cart_page.get_cart_item_count() == product_count, \
            f"Should have {product_count} items in cart"
