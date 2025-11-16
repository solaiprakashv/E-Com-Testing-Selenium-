"""
Open website and automatically login for manual exploration
Browser stays open for you to explore the site
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def open_and_login():
    """Open website and automatically login"""
    print("\n" + "="*60)
    print("  Auto-Login to SauceDemo for Manual Exploration")
    print("="*60 + "\n")
    
    # Setup Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    print("🌐 Opening Chrome browser...")
    
    try:
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
    except:
        driver = webdriver.Chrome(options=chrome_options)
    
    # Open website
    print("🔗 Navigating to: https://www.saucedemo.com/")
    driver.get("https://www.saucedemo.com/")
    time.sleep(1)
    
    # Auto-login
    print("⌨️  Entering username: standard_user")
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")
    time.sleep(0.5)
    
    print("⌨️  Entering password: secret_sauce")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    time.sleep(0.5)
    
    print("🖱️  Clicking login button...")
    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()
    time.sleep(2)
    
    print("\n" + "="*60)
    print("  ✅ Successfully Logged In!")
    print("="*60)
    print("\n🎉 You're now on the Products page!")
    print("\n💡 What you can do:")
    print("   • Browse products")
    print("   • Add items to cart")
    print("   • View cart")
    print("   • Sort products")
    print("   • Explore the site")
    print("\n⏳ Browser will stay open for you to explore.")
    print("   Close the browser window when done, or press Ctrl+C here.")
    print("="*60 + "\n")
    
    try:
        # Keep browser open
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Closing browser...")
        driver.quit()
        print("✅ Browser closed. Goodbye!\n")

if __name__ == "__main__":
    open_and_login()
