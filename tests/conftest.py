"""conftest.py."""
import pytest
import os
import time
from tests.driver_configs import CHROME_DRIVER_PATH
from tests.driver_configs import GECKO_DRIVER_PATH
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    """Add browser console option to pytest."""
    parser.addoption("--browser", 
                     action="store", 
                     default="chrome", 
                     help="Driver Selection: Chrome or Firefox")

@pytest.fixture(scope="session")
def browser_type(request):
    """Fixture to fetch the browser type."""
    return request.config.getoption("--browser")

@pytest.fixture
def browser(browser_type):
    """Start the browser driver based on the browser_type fixture."""
    if browser_type == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--log-level=3")  # Suppress logs
        driver = webdriver.Chrome(service=ChromeService(CHROME_DRIVER_PATH), options=chrome_options)
    elif browser_type == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--log-level=3") # Suppress logs
        driver = webdriver.Firefox(service=FirefoxService(GECKO_DRIVER_PATH), options=firefox_options)
    else:
        raise ValueError("Unsupported browser selected!! " \
            "Please ensure you have selected one of the desired browsers : "\
                "'chrome' or 'firefox'.")
    
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    """Capture screenshot if test fails."""
    if call.when == 'call' and call.excinfo is not None:
        # Retrieve the test name
        test_function_name = item.nodeid.split("::")[-1]
        test_class_name = item.nodeid.split("::")[-2]
        test_name = test_class_name + "-" + test_function_name
        
        # Capture screenshot
        driver = item.funcargs['browser']  # Access the browser driver
        record_error_screenshot(driver, test_name)

def record_error_screenshot(driver, test_name):
    """Capture and save screenshot for the failed test."""
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_dir = "error_screenshots"
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot of the error saved to {screenshot_path}")