"""
PyTest configuration and fixtures
Contains setup and teardown for all tests
"""
import pytest
from datetime import datetime
from utils.driver_setup import DriverSetup
from utils.screenshot import Screenshot


# Test data constants
BASE_URL = "https://www.saucedemo.com/"
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture(scope="function")
def driver():
    """Setup and teardown WebDriver for each test"""
    driver = DriverSetup.get_driver()
    driver.get(BASE_URL)
    yield driver
    DriverSetup.quit_driver(driver)


@pytest.fixture(scope="function")
def driver_with_screenshot(request):
    """Setup WebDriver with screenshot on failure"""
    driver = DriverSetup.get_driver()
    driver.get(BASE_URL)
    
    yield driver
    
    # Capture screenshot on test failure
    if request.node.rep_call.failed:
        Screenshot.capture(driver, request.node.name)
    
    DriverSetup.quit_driver(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test result for screenshot on failure"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# Custom HTML Report Configuration
def pytest_html_report_title(report):
    """Customize report title"""
    report.title = "🚀 E-Commerce Automation Test Report - India Edition"


def pytest_configure(config):
    """Configure pytest-html metadata"""
    config._metadata['Project'] = 'E-Commerce Automation Testing'
    config._metadata['Test Engineer'] = 'QA Automation Team'
    config._metadata['Environment'] = 'SauceDemo Test Site'
    config._metadata['Currency'] = '₹ Indian Rupees (INR)'
    config._metadata['Browser'] = 'Chrome (Latest)'
    config._metadata['Framework'] = 'Selenium + PyTest'


def pytest_html_results_table_header(cells):
    """Customize table headers"""
    cells.insert(2, '<th>Duration</th>')
    cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')


def pytest_html_results_table_row(report, cells):
    """Customize table rows"""
    cells.insert(2, f'<td class="col-duration">{report.duration:.2f}s</td>')
    cells.insert(1, f'<td class="col-time">{datetime.now().strftime("%H:%M:%S")}</td>')
