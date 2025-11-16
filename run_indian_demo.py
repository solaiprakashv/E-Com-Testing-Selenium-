"""
Run Indian E-Commerce Demo Tests
Tests the local Indian demo site with prices in Rupees
"""
import subprocess
import sys
import os
import webbrowser


def print_header(text):
    """Print formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)


def show_menu():
    """Display menu options"""
    print_header("🇮🇳 Indian E-Commerce Demo Menu")
    print("\n1. 🌐 View Indian Demo Site (Browser)")
    print("2. 🧪 Run Indian Demo Tests")
    print("3. 💱 Run USD to INR Conversion Tests")
    print("4. 📊 Run All Tests with INR Display")
    print("5. 📁 Open Demo Site File")
    print("6. ❌ Exit")
    print("="*60)


def view_demo_site():
    """Open Indian demo site in browser"""
    demo_path = os.path.abspath("demo_site/indian_ecommerce.html")
    print(f"\n🌐 Opening Indian E-Commerce Demo...")
    print(f"📁 Location: {demo_path}")
    webbrowser.open(f"file:///{demo_path}")
    print("\n✅ Demo site opened in your browser!")
    print("\n📝 Login Credentials:")
    print("   Username: test_user")
    print("   Password: test123")
    print("\n💰 All prices are in Indian Rupees (₹)")


def run_indian_tests():
    """Run tests for Indian demo site"""
    print_header("Running Indian E-Commerce Tests")
    print("\n🧪 Executing tests on Indian demo site...")
    print("💰 Testing products priced in Rupees (₹)\n")
    
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/test_indian_ecommerce.py",
        "-v",
        "--html=reports/indian_demo_report.html",
        "--self-contained-html"
    ]
    
    subprocess.run(cmd)
    print("\n✅ Tests completed!")
    print("📊 Report: reports/indian_demo_report.html")


def run_inr_conversion_tests():
    """Run USD to INR conversion tests"""
    print_header("Running USD to INR Conversion Tests")
    print("\n💱 Testing currency conversion...")
    print("📊 Shows prices in both USD and INR\n")
    
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/test_cart_with_inr.py",
        "-v", "-s",
        "--html=reports/inr_conversion_report.html",
        "--self-contained-html"
    ]
    
    subprocess.run(cmd)
    print("\n✅ Tests completed!")
    print("📊 Report: reports/inr_conversion_report.html")


def run_all_inr_tests():
    """Run all tests with INR display"""
    print_header("Running All Tests with INR Display")
    print("\n🧪 Running comprehensive test suite...")
    print("💰 Includes both Indian demo and conversion tests\n")
    
    cmd = [
        sys.executable, "-m", "pytest",
        "tests/test_indian_ecommerce.py",
        "tests/test_cart_with_inr.py",
        "-v", "-s",
        "--html=reports/complete_inr_report.html",
        "--self-contained-html"
    ]
    
    subprocess.run(cmd)
    print("\n✅ All tests completed!")
    print("📊 Report: reports/complete_inr_report.html")


def open_demo_file():
    """Open demo site folder"""
    demo_path = os.path.abspath("demo_site")
    print(f"\n📁 Opening demo site folder: {demo_path}")
    os.startfile(demo_path)
    print("✅ Folder opened!")


def main():
    """Main menu loop"""
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            view_demo_site()
        elif choice == "2":
            run_indian_tests()
        elif choice == "3":
            run_inr_conversion_tests()
        elif choice == "4":
            run_all_inr_tests()
        elif choice == "5":
            open_demo_file()
        elif choice == "6":
            print("\n✅ Goodbye!\n")
            sys.exit(0)
        else:
            print("\n❌ Invalid choice. Please enter 1-6.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        print("\n" + "="*60)
        print("  🇮🇳 Indian E-Commerce Automation Testing")
        print("  Prices in Indian Rupees (₹)")
        print("="*60)
        main()
    except KeyboardInterrupt:
        print("\n\n✅ Goodbye!\n")
        sys.exit(0)
