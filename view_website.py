"""
Simple script to open and view the test website manually
No tests run - just opens browser for manual exploration
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def open_website():
    """Open the test website in browser for manual viewing"""
    print("\n" + "="*60)
    print("  Opening SauceDemo Website for Manual Viewing")
    print("="*60 + "\n")
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    print("🌐 Opening Chrome browser...")
    
    try:
        # Initialize driver
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
    except:
        driver = webdriver.Chrome(options=chrome_options)
    
    # Open the website
    print("🔗 Navigating to: https://www.saucedemo.com/")
    driver.get("https://www.saucedemo.com/")
    
    print("\n" + "="*60)
    print("  Website Opened Successfully!")
    print("="*60)
    print("\n📝 Login Credentials:")
    print("   Username: standard_user")
    print("   Password: secret_sauce")
    print("\n💡 The browser will stay open for you to explore.")
    print("   Close the browser window when you're done.")
    print("\n⏳ Browser will stay open indefinitely...")
    print("   Press Ctrl+C in this terminal to close the browser.")
    print("="*60 + "\n")
    
    try:
        # Keep browser open until user closes it
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Closing browser...")
        driver.quit()
        print("✅ Browser closed. Goodbye!\n")

if __name__ == "__main__":
    open_website()
