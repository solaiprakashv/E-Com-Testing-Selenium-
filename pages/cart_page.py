"""
Page Object Model for Shopping Cart Page
Contains cart items, price validation, and checkout functionality
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QUANTITIES = (By.CLASS_NAME, "cart_quantity")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove']")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def is_cart_page_displayed(self):
        """Verify cart page is displayed"""
        return self.is_element_displayed(self.PAGE_TITLE)

    def get_page_title(self):
        """Get cart page title"""
        return self.get_text(self.PAGE_TITLE)

    def get_cart_item_count(self):
        """Get number of items in cart"""
        items = self.find_elements(self.CART_ITEMS)
        return len(items)

    def get_item_names(self):
        """Get list of item names in cart"""
        elements = self.find_elements(self.ITEM_NAMES)
        return [element.text for element in elements]

    def get_item_prices(self):
        """Get list of item prices in cart"""
        elements = self.find_elements(self.ITEM_PRICES)
        return [element.text for element in elements]

    def get_item_quantities(self):
        """Get list of item quantities"""
        elements = self.find_elements(self.ITEM_QUANTITIES)
        return [element.text for element in elements]

    def calculate_total_price(self):
        """Calculate total price of items in cart"""
        prices = self.get_item_prices()
        total = 0.0
        for price in prices:
            # Remove $ symbol and convert to float
            total += float(price.replace("$", ""))
        return total

    def remove_item_by_index(self, index=0):
        """Remove item from cart by index"""
        buttons = self.find_elements(self.REMOVE_BUTTONS)
        if index < len(buttons):
            buttons[index].click()

    def is_cart_empty(self):
        """Check if cart is empty"""
        return self.get_cart_item_count() == 0

    def continue_shopping(self):
        """Click continue shopping button"""
        self.click(self.CONTINUE_SHOPPING)

    def proceed_to_checkout(self):
        """Click checkout button"""
        self.click(self.CHECKOUT_BUTTON)
