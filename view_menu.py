"""
Interactive menu to view website or reports
No tests run - just viewing
"""
import webbrowser
import os
import subprocess
import sys

def print_menu():
    """Display viewing options menu"""
    print("\n" + "="*60)
    print("  🌐 Website & Report Viewer Menu")
    print("="*60)
    print("\nWhat would you like to view?")
    print("\n1. 🌐 Open Website (Manual Login)")
    print("2. 🔐 Open Website (Auto-Login)")
    print("3. 📊 View Test Report (HTML)")
    print("4. 📸 View Failure Screenshots")
    print("5. 📁 Open Reports Folder")
    print("6. 🌍 Open Website in Default Browser (No Selenium)")
    print("7. ❌ Exit")
    print("="*60)

def open_website_browser():
    """Open website in default browser"""
    print("\n🌐 Opening https://www.saucedemo.com/ in your browser...")
    webbrowser.open("https://www.saucedemo.com/")
    print("\n✅ Website opened in your default browser!")
    print("\n📝 Login Credentials:")
    print("   Username: standard_user")
    print("   Password: secret_sauce")

def open_website_selenium():
    """Open website with Selenium (manual login)"""
    print("\n🚀 Launching browser with Selenium...")
    subprocess.run([sys.executable, "view_website.py"])

def open_website_autologin():
    """Open website with auto-login"""
    print("\n🚀 Launching browser with auto-login...")
    subprocess.run([sys.executable, "view_with_login.py"])

def view_report():
    """Open HTML test report"""
    report_path = "reports/test_report.html"
    if os.path.exists(report_path):
        print(f"\n📊 Opening test report: {report_path}")
        os.startfile(report_path)
        print("✅ Report opened in your browser!")
    else:
        print("\n❌ Report not found!")
        print("   Run tests first: python -m pytest tests/ --html=reports/test_report.html --self-contained-html")

def view_screenshots():
    """Open screenshots folder"""
    screenshots_path = "reports/screenshots"
    if os.path.exists(screenshots_path):
        print(f"\n📸 Opening screenshots folder: {screenshots_path}")
        os.startfile(screenshots_path)
        print("✅ Screenshots folder opened!")
    else:
        print("\n❌ Screenshots folder not found!")
        print("   Screenshots are created when tests fail.")

def open_reports_folder():
    """Open reports folder"""
    reports_path = "reports"
    if os.path.exists(reports_path):
        print(f"\n📁 Opening reports folder: {reports_path}")
        os.startfile(reports_path)
        print("✅ Reports folder opened!")
    else:
        print("\n❌ Reports folder not found!")

def main():
    """Main menu loop"""
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            open_website_selenium()
        elif choice == "2":
            open_website_autologin()
        elif choice == "3":
            view_report()
        elif choice == "4":
            view_screenshots()
        elif choice == "5":
            open_reports_folder()
        elif choice == "6":
            open_website_browser()
        elif choice == "7":
            print("\n✅ Goodbye!\n")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please enter 1-7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✅ Goodbye!\n")
        sys.exit(0)
