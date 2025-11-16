"""
WebDriver setup and configuration
Handles browser initialization and teardown
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class DriverSetup:
    @staticmethod
    def get_driver():
        """Initialize and return Chrome WebDriver"""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        
        # Uncomment below for headless mode
        # chrome_options.add_argument("--headless")
        
        try:
            # Use WebDriverManager to automatically download and manage ChromeDriver
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=chrome_options
            )
        except Exception as e:
            print(f"Error initializing Chrome driver: {e}")
            print("Trying alternative method...")
            driver = webdriver.Chrome(options=chrome_options)
        
        driver.implicitly_wait(10)
        return driver

    @staticmethod
    def quit_driver(driver):
        """Quit the WebDriver"""
        if driver:
            driver.quit()
