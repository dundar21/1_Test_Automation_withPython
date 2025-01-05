# Insider Test Automation
- This project is demo for QA job list test Insider Web Page via Python Selenium

## Steps

### 1-Create a virtual environment
- Create web_env by -> **python -m venv web_env**

### 2-Install Required Pip Packages
- Activate venv -> **.\web_env\Scripts\activate**
- Install related packages from requirements.txt file -> **pip install -r requirements.txt**

### 3-Check Chrome Driver version
- Check driver version from **src/chrome_driver** folder and update if necessary
- Chromedriver version -> 131...
- Geckodriver version -> 0.35.0
- [ChromeDriverChannel](https://googlechromelabs.github.io/chrome-for-testing/)
- [GeckoDriverChannel](https://github.com/mozilla/geckodriver/releases)

### 4-Run Test
- run tests according to browser type
- **pytest -v .\tests\test_insider.py --browser [chrome/firefox]**
