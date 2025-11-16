"""
Page Object Model for Products Page
Contains product listing, filtering, and cart operations
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):
    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[id^='remove']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver):
        super().__init__(driver)

    def is_products_page_displayed(self):
        """Verify products page is displayed"""
        return self.is_element_displayed(self.PAGE_TITLE)

    def get_page_title(self):
        """Get page title text"""
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self):
        """Get total number of products displayed"""
        products = self.find_elements(self.PRODUCT_ITEMS)
        return len(products)

    def get_product_names(self):
        """Get list of all product names"""
        elements = self.find_elements(self.PRODUCT_NAMES)
        return [element.text for element in elements]

    def get_product_prices(self):
        """Get list of all product prices"""
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

    def open_menu(self):
        """Open hamburger menu"""
        self.click(self.MENU_BUTTON)

    def logout(self):
        """Perform logout action"""
        self.open_menu()
        self.click(self.LOGOUT_LINK)
