# E-Commerce Website Automation using Selenium - Python

## 📋 Project Overview
This project demonstrates automated testing of an e-commerce web application using Selenium WebDriver with Python and PyTest. It implements the Page Object Model (POM) design pattern to automate critical user workflows including login, product browsing, cart management, and logout functionality.

**Test Application:** [SauceDemo](https://www.saucedemo.com/)

## 🎯 Objective
Build a robust automation suite to test essential workflows of an e-commerce platform, validating system functionality and reliability through comprehensive test coverage.

## 🛠️ Tech Stack
- **Python 3.8+** - Programming language
- **Selenium WebDriver 4.15.2** - Browser automation
- **PyTest 7.4.3** - Testing framework
- **pytest-html 4.1.1** - HTML report generation
- **WebDriver Manager** - Automatic driver management
- **Page Object Model (POM)** - Design pattern for maintainability

## ✅ Test Scenarios Covered

### 1. Login Tests (5 test cases)
- Valid credentials login
- Invalid username/password
- Empty credentials validation
- Locked user verification

### 2. Products Page Tests (4 test cases)
- Products page loads correctly after login
- Product listing display verification
- Product names visibility
- Product prices validation

### 3. Add to Cart Tests (7 test cases)
- Add single product to cart
- Add multiple products to cart
- Verify cart quantity
- Validate cart total price calculation
- Product details in cart
- Remove item from cart
- Empty cart verification

### 4. Logout Tests (2 test cases)
- Successful logout
- Logout and re-login workflow

**Total: 18 Automated Test Cases**


## 📁 Project Structure
```
Selenium-Ecommerce-Python/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py           # Base class with common methods
│   ├── login_page.py           # Login page objects and methods
│   ├── products_page.py        # Products page objects
│   └── cart_page.py            # Shopping cart page objects
│
├── tests/
│   ├── __init__.py
│   ├── test_login.py           # Login test cases
│   ├── test_products.py        # Product page test cases
│   ├── test_add_to_cart.py     # Cart functionality tests
│   └── test_logout.py          # Logout test cases
│
├── utils/
│   ├── __init__.py
│   ├── driver_setup.py         # WebDriver configuration
│   └── screenshot.py           # Screenshot utility
│
├── reports/                    # Auto-generated test reports
│   ├── test_report.html
│   └── screenshots/
│
├── conftest.py                 # PyTest fixtures and configuration
├── pytest.ini                  # PyTest settings
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Chrome Browser (latest version)
- Git (optional)

### Installation Steps

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd Selenium-Ecommerce-Python
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python --version
   pip list
   ```

## ▶️ Execution Instructions

### Run all tests
```bash
pytest
```

### Run tests with HTML report
```bash
pytest --html=reports/test_report.html --self-contained-html
```

### Run specific test file
```bash
pytest tests/test_login.py
pytest tests/test_add_to_cart.py
```

### Run specific test case
```bash
pytest tests/test_login.py::TestLogin::test_login_with_valid_credentials
```

### Run tests with verbose output
```bash
pytest -v
```

### Run tests with markers
```bash
pytest -m smoke
pytest -m regression
```

### Run tests in parallel (requires pytest-xdist)
```bash
pip install pytest-xdist
pytest -n 4
```


## 📊 Test Reports

### HTML Report
After test execution, an HTML report is generated at `reports/test_report.html`

Features:
- Test execution summary (passed/failed/skipped)
- Detailed test results with timestamps
- Error messages and stack traces
- Execution duration for each test

### Screenshots on Failure
- Automatically captured when tests fail
- Stored in `reports/screenshots/` directory
- Named with test name and timestamp

## 🎨 Design Pattern: Page Object Model (POM)

### Benefits
- **Reusability**: Page objects can be reused across multiple tests
- **Maintainability**: UI changes require updates only in page classes
- **Readability**: Tests are clean and easy to understand
- **Separation of Concerns**: Test logic separated from page elements

### Implementation
Each page class:
- Inherits from `BasePage` for common functionality
- Contains locators as class variables
- Provides methods for user actions
- Returns appropriate page objects for navigation

### Example
```python
# Page Object
class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    
    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        # ... more actions

# Test
def test_login(driver):
    login_page = LoginPage(driver)
    login_page.login("user", "pass")
    assert products_page.is_displayed()
```

## 🔧 Configuration

### PyTest Configuration (pytest.ini)
- Test discovery patterns
- Command line options
- Test markers for categorization
- Console output styling

### Fixtures (conftest.py)
- `driver`: Basic WebDriver setup/teardown
- `driver_with_screenshot`: WebDriver with screenshot on failure
- Test data constants (BASE_URL, credentials)

## 🐛 Troubleshooting

### Common Issues

**Issue**: ChromeDriver not found
```bash
Solution: WebDriver Manager handles this automatically. 
Ensure you have internet connection on first run.
```

**Issue**: Tests fail with timeout
```bash
Solution: Increase implicit wait in driver_setup.py
or check internet connection to test site.
```

**Issue**: Import errors
```bash
Solution: Ensure virtual environment is activated
and all dependencies are installed.
```

## 🔄 Future Enhancements
- [ ] Cross-browser testing (Firefox, Edge, Safari)
- [ ] Parallel test execution with pytest-xdist
- [ ] Integration with CI/CD (GitHub Actions, Jenkins)
- [ ] Allure reporting for better visualization
- [ ] Data-driven testing with CSV/JSON
- [ ] API testing integration
- [ ] Docker containerization
- [ ] Test retry mechanism for flaky tests


## 📝 Sample Test Execution Output

```
============================= test session starts ==============================
platform win32 -- Python 3.11.0, pytest-7.4.3, pluggy-1.3.0
rootdir: /Selenium-Ecommerce-Python
configfile: pytest.ini
plugins: html-4.1.1
collected 18 items

tests/test_login.py .....                                                [ 27%]
tests/test_products.py ....                                              [ 50%]
tests/test_add_to_cart.py .......                                        [ 88%]
tests/test_logout.py ..                                                  [100%]

============================== 18 passed in 45.23s ==============================

HTML report generated at: reports/test_report.html
```

## 📚 Key Features

✅ **Modular Architecture** - Clean separation of pages, tests, and utilities  
✅ **Automatic Screenshots** - Captures screenshots on test failures  
✅ **HTML Reports** - Professional test execution reports  
✅ **Reusable Fixtures** - PyTest fixtures for setup/teardown  
✅ **Explicit Waits** - Robust element waiting strategies  
✅ **Auto Driver Management** - WebDriver Manager handles browser drivers  
✅ **POM Design Pattern** - Industry-standard design pattern  
✅ **Comprehensive Coverage** - 18+ test cases covering critical flows  


## 📄 License
This project is open source and available for educational purposes.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

---
**Note**: This is a portfolio project demonstrating automation testing skills using Python and Selenium for resume purposes.
