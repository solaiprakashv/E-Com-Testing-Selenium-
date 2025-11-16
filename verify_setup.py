"""
Setup Verification Script
Run this script to verify your environment is ready for test execution
"""
import sys
import subprocess
import os


def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)


def print_status(check, status, message=""):
    """Print check status"""
    symbol = "✓" if status else "✗"
    status_text = "PASS" if status else "FAIL"
    print(f"{symbol} {check}: {status_text} {message}")


def check_python_version():
    """Check Python version"""
    print_header("Checking Python Version")
    version = sys.version_info
    required = (3, 8)
    
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version >= required:
        print_status("Python Version", True, f"(>= {required[0]}.{required[1]})")
        return True
    else:
        print_status("Python Version", False, f"(Need >= {required[0]}.{required[1]})")
        return False


def check_pip():
    """Check if pip is installed"""
    print_header("Checking pip")
    try:
        result = subprocess.run(
            ["pip", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout.strip())
        print_status("pip Installation", True)
        return True
    except:
        print_status("pip Installation", False)
        return False


def check_dependencies():
    """Check if required packages are installed"""
    print_header("Checking Dependencies")
    
    required_packages = [
        "selenium",
        "pytest",
        "pytest-html",
        "webdriver-manager"
    ]
    
    all_installed = True
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print_status(f"{package}", True, "Installed")
        except ImportError:
            print_status(f"{package}", False, "Not Installed")
            all_installed = False
    
    return all_installed


def check_project_structure():
    """Check if project structure is correct"""
    print_header("Checking Project Structure")
    
    required_dirs = ["pages", "tests", "utils"]
    required_files = [
        "conftest.py",
        "pytest.ini",
        "requirements.txt",
        "README.md"
    ]
    
    all_present = True
    
    # Check directories
    for directory in required_dirs:
        exists = os.path.isdir(directory)
        print_status(f"Directory: {directory}/", exists)
        if not exists:
            all_present = False
    
    # Check files
    for file in required_files:
        exists = os.path.isfile(file)
        print_status(f"File: {file}", exists)
        if not exists:
            all_present = False
    
    return all_present


def check_page_objects():
    """Check if page object files exist"""
    print_header("Checking Page Objects")
    
    page_files = [
        "pages/__init__.py",
        "pages/base_page.py",
        "pages/login_page.py",
        "pages/products_page.py",
        "pages/cart_page.py"
    ]
    
    all_present = True
    
    for file in page_files:
        exists = os.path.isfile(file)
        print_status(file, exists)
        if not exists:
            all_present = False
    
    return all_present


def check_test_files():
    """Check if test files exist"""
    print_header("Checking Test Files")
    
    test_files = [
        "tests/__init__.py",
        "tests/test_login.py",
        "tests/test_products.py",
        "tests/test_add_to_cart.py",
        "tests/test_logout.py"
    ]
    
    all_present = True
    
    for file in test_files:
        exists = os.path.isfile(file)
        print_status(file, exists)
        if not exists:
            all_present = False
    
    return all_present


def check_internet_connection():
    """Check internet connectivity"""
    print_header("Checking Internet Connection")
    
    try:
        import urllib.request
        urllib.request.urlopen('https://www.saucedemo.com/', timeout=5)
        print_status("Test Site Accessible", True, "(https://www.saucedemo.com/)")
        return True
    except:
        print_status("Test Site Accessible", False, "(Check internet connection)")
        return False


def provide_recommendations(results):
    """Provide recommendations based on check results"""
    print_header("Recommendations")
    
    if not results["python"]:
        print("\n❌ Python 3.8+ is required")
        print("   Install from: https://www.python.org/downloads/")
    
    if not results["pip"]:
        print("\n❌ pip is not installed")
        print("   Install pip: python -m ensurepip --upgrade")
    
    if not results["dependencies"]:
        print("\n❌ Some dependencies are missing")
        print("   Run: pip install -r requirements.txt")
    
    if not results["structure"]:
        print("\n❌ Project structure is incomplete")
        print("   Ensure all required files and folders are present")
    
    if not results["internet"]:
        print("\n❌ Cannot reach test site")
        print("   Check your internet connection")
    
    if all(results.values()):
        print("\n✅ All checks passed! You're ready to run tests!")
        print("\nNext steps:")
        print("1. Run tests: pytest")
        print("2. Generate report: pytest --html=reports/test_report.html --self-contained-html")
        print("3. Run specific suite: pytest tests/test_login.py")


def main():
    """Main verification function"""
    print("\n" + "="*60)
    print("  E-Commerce Selenium Automation - Setup Verification")
    print("="*60)
    
    results = {
        "python": check_python_version(),
        "pip": check_pip(),
        "dependencies": check_dependencies(),
        "structure": check_project_structure(),
        "pages": check_page_objects(),
        "tests": check_test_files(),
        "internet": check_internet_connection()
    }
    
    # Summary
    print_header("Verification Summary")
    passed = sum(results.values())
    total = len(results)
    
    print(f"\nChecks Passed: {passed}/{total}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n🎉 Status: READY TO RUN TESTS")
    else:
        print(f"\n⚠️  Status: {total - passed} ISSUE(S) FOUND")
    
    provide_recommendations(results)
    
    print("\n" + "="*60)
    print("  Verification Complete")
    print("="*60 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nVerification interrupted.")
        sys.exit(0)
