"""
Screenshot utility for capturing test failures
"""
import os
from datetime import datetime


class Screenshot:
    @staticmethod
    def capture(driver, test_name):
        """Capture screenshot with timestamp"""
        # Create screenshots directory if it doesn't exist
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(screenshot_dir, filename)
        
        # Capture screenshot
        driver.save_screenshot(filepath)
        print(f"Screenshot saved: {filepath}")
        return filepath
