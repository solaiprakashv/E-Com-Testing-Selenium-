"""
Page Object Model for Indian E-Commerce Products Page
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class IndianProductsPage(BasePage):
    # Locators
    PRODUCTS_TITLE = (By.CLASS_NAME, "products-title")
    PRODUCT_CARDS = (By.CLASS_NAME, "product-card")
    PRODUCT_NAMES = (By.CLASS_NAME, "product-name")
    PRODUCT_PRICES = (By.CLASS_NAME, "product-price")
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "add-to-cart-btn")
    CART_BADGE = (By.ID, "cartBadge")
    CART_ICON = (By.ID, "cartIcon")
    LOGOUT_BUTTON = (By.ID, "logout-sidebar-link")

    def __init__(self, driver):
        super().__init__(driver)

    def is_products_page_displayed(self):
        """Verify products page is displayed"""
        return self.is_element_displayed(self.PRODUCTS_TITLE)

    def get_page_title(self):
        """Get page title text"""
        return self.get_text(self.PRODUCTS_TITLE)

    def get_product_count(self):
        """Get total number of products displayed"""
        products = self.find_elements(self.PRODUCT_CARDS)
        return len(products)

    def get_product_names(self):
        """Get list of all product names"""
        elements = self.find_elements(self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_product_prices(self):
        """Get list of all product prices in INR"""
        elements = self.find_elements(self.PRODUCT_PRICES)
        return [element.text for element in elements]

    def add_product_to_cart_by_index(self, index=0):
        """Add product to cart by index"""
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        if index < len(buttons):
            buttons[index].click()
        else:
            raise IndexError(f"Product index {index} out of range")

    def add_multiple_products_to_cart(self, count=2):
        """Add multiple products to cart"""
        buttons = self.find_elements(self.ADD_TO_CART_BUTTONS)
        for i in range(min(count, len(buttons))):
            buttons[i].click()

    def get_cart_badge_count(self):
        """Get cart item count from badge"""
        try:
            return self.get_text(self.CART_BADGE)
        except:
            return "0"

    def click_cart_icon(self):
        """Navigate to cart page"""
        self.click(self.CART_ICON)

    def logout(self):
        """Perform logout action"""
        self.click(self.LOGOUT_BUTTON)
