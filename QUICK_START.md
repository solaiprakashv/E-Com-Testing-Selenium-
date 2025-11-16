# Quick Start Guide

## Get Started in 5 Minutes! 🚀

### Step 1: Prerequisites Check
```bash
# Check Python version (need 3.8+)
python --version

# Check pip
pip --version
```

### Step 2: Setup Project
```bash
# Navigate to project directory
cd Selenium-Ecommerce-Python

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Run Tests
```bash
# Run all tests
pytest

# Run with HTML report
pytest --html=reports/test_report.html --self-contained-html

# Run specific test file
pytest tests/test_login.py

# Run with verbose output
pytest -v
```

### Step 4: View Results
- Open `reports/test_report.html` in your browser
- Check `reports/screenshots/` for failure screenshots

---

## Common Commands Cheat Sheet

```bash
# Run all tests with detailed output
pytest -v

# Run specific test class
pytest tests/test_login.py::TestLogin

# Run specific test method
pytest tests/test_login.py::TestLogin::test_login_with_valid_credentials

# Run tests matching keyword
pytest -k "login"

# Run tests with markers
pytest -m smoke

# Show print statements
pytest -s

# Stop on first failure
pytest -x

# Run last failed tests
pytest --lf

# Generate HTML report
pytest --html=reports/test_report.html --self-contained-html

# Run with coverage (requires pytest-cov)
pytest --cov=pages --cov=tests
```

---

## Project Structure Quick Reference

```
pages/          → Page Object classes
tests/          → Test scripts
utils/          → Helper utilities
reports/        → Test reports (auto-generated)
conftest.py     → PyTest fixtures
pytest.ini      → PyTest configuration
requirements.txt → Dependencies
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution**: Activate virtual environment and install dependencies
```bash
pip install -r requirements.txt
```

### Issue: "ChromeDriver not found"
**Solution**: WebDriver Manager handles this automatically. Ensure internet connection.

### Issue: Tests are slow
**Solution**: Check internet connection. The test site might be slow.

### Issue: Element not found
**Solution**: Increase wait time in `utils/driver_setup.py`

---

## Next Steps

1. ✅ Run all tests successfully
2. ✅ Review test reports
3. ✅ Explore page objects in `pages/` directory
4. ✅ Read test cases in `tests/` directory
5. ✅ Customize for your needs

---

## Need Help?

- Check `README.md` for detailed documentation
- Review `INTERVIEW_GUIDE.md` for project explanation
- See `TEST_CASES_DOCUMENTATION.md` for test details

---

**Happy Testing! 🎉**
