"""driver configs file."""
import os

# Current working directory path
WORKING_DIRECTORY = os.getcwd()
#Chromedriver path for Chrome
CHROME_DRIVER_PATH = os.path.join(WORKING_DIRECTORY,'src','chrome_driver','chromedriver.exe')
#Geckodriver path for Firefox
GECKO_DRIVER_PATH = os.path.join(WORKING_DIRECTORY,'src','firefox_driver','geckodriver.exe')
