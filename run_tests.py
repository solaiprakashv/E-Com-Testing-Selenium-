"""
Test execution script with multiple options
Run this script to execute tests with various configurations
"""
import os
import sys
import subprocess
from datetime import datetime


def create_reports_directory():
    """Create reports directory if it doesn't exist"""
    if not os.path.exists('reports'):
        os.makedirs('reports')
        print("✓ Created reports directory")
    
    if not os.path.exists('reports/screenshots'):
        os.makedirs('reports/screenshots')
        print("✓ Created screenshots directory")


def run_all_tests():
    """Run all tests with HTML report"""
    print("\n" + "="*60)
    print("Running All Tests")
    print("="*60 + "\n")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"reports/test_report_{timestamp}.html"
    
    cmd = [
        "pytest",
        "-v",
        f"--html={report_file}",
        "--self-contained-html"
    ]
    
    subprocess.run(cmd)
    print(f"\n✓ Report generated: {report_file}")


def run_smoke_tests():
    """Run smoke tests only"""
    print("\n" + "="*60)
    print("Running Smoke Tests")
    print("="*60 + "\n")
    
    cmd = [
        "pytest",
        "-v",
        "-m", "smoke",
        "--html=reports/smoke_test_report.html",
        "--self-contained-html"
    ]
    
    subprocess.run(cmd)


def run_specific_suite(suite_name):
    """Run specific test suite"""
    print(f"\n" + "="*60)
    print(f"Running {suite_name} Tests")
    print("="*60 + "\n")
    
    test_files = {
        "login": "tests/test_login.py",
        "products": "tests/test_products.py",
        "cart": "tests/test_add_to_cart.py",
        "logout": "tests/test_logout.py"
    }
    
    if suite_name.lower() in test_files:
        cmd = [
            "pytest",
            "-v",
            test_files[suite_name.lower()],
            f"--html=reports/{suite_name}_report.html",
            "--self-contained-html"
        ]
        subprocess.run(cmd)
    else:
        print(f"❌ Unknown test suite: {suite_name}")
        print(f"Available suites: {', '.join(test_files.keys())}")


def show_menu():
    """Display test execution menu"""
    print("\n" + "="*60)
    print("E-Commerce Selenium Test Automation")
    print("="*60)
    print("\nTest Execution Options:")
    print("1. Run All Tests")
    print("2. Run Login Tests")
    print("3. Run Products Tests")
    print("4. Run Cart Tests")
    print("5. Run Logout Tests")
    print("6. Run Smoke Tests")
    print("7. Exit")
    print("="*60)


def main():
    """Main execution function"""
    create_reports_directory()
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            run_all_tests()
        elif choice == "2":
            run_specific_suite("login")
        elif choice == "3":
            run_specific_suite("products")
        elif choice == "4":
            run_specific_suite("cart")
        elif choice == "5":
            run_specific_suite("logout")
        elif choice == "6":
            run_smoke_tests()
        elif choice == "7":
            print("\n✓ Exiting... Goodbye!")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please enter 1-7.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n✓ Test execution interrupted. Goodbye!")
        sys.exit(0)
