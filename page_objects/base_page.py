"""Base page actions.

It includes:
- Open giving page
- Get title of the page
- Capture Error Screenshot
- Driver actions such as click, get text, etc.
"""
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class BasePage:
    """Base Page class."""
    
    def __init__(self, driver):
        """Initialize the BasePage with a WebDriver instance."""
        self.driver = driver
        self.timeout = 15  # Default timeout for waiting for elements

    def get_page(self, url):
        """Open specified page.

        Args:
            url (str): URL of the page.
        """
        self.driver.get(url)

    def get_title(self):
        """Get title of current title."""
        WebDriverWait(self.driver, self.timeout).until(lambda driver: driver.title != "")
        return self.driver.title

    def wait_for_header_load_of_page(self):
        """Wait for header page load of the page."""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((By.TAG_NAME, "h2"))
        )
        except TimeoutException:
            print(f"Page header element not found within {self.timeout} seconds.")
        

    def wait_element_clickability_and_click(self,element_location):
        """Wait for an element clickability and then click it.

        Args:
            element_location (webElement): The desired element to location to operate.

        Raises:
            Exception: Raises exception after timeout error occurs.
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(element_location)
            )
            element.click()
        except TimeoutException:
            raise Exception(f"Element : {element_location} could not clickable after {self.timeout} seconds.")

    def wait_element_visibility_and_click(self,element_location):
        """Wait for an element visibility and then return it.

        Args:
            element_location (webElement): The desired element to location to operate.

        Raises:
            Exception: Raises exception after timeout error occurs.
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(element_location)
            )
            element.click()
        except TimeoutException:
            raise Exception(f"Element : {element_location} could not visible after {self.timeout} seconds.")

    def find_multiple_elements(self,element_location):
        """Wait for multiple elements visibility and then return them.

        Args:
            element_location (webElement): The desired element to location to operate.

        Raises:
            Exception: Raises exception after timeout error occurs.

        Returns:
            list : List of visible elements
        """
        try:
            return self.driver.find_elements(*element_location)
        except TimeoutException:
            raise Exception(f"Elements : {element_location} could not visible after {self.timeout} seconds.")

    def find_presence_of_elements(self, element_location):
        """Wait for all elements visibility and get them.

        Args:
            element_location (webElement): The desired element to location to operate.

        Raises:
            Exception: Raises exception after timeout error occurs.

        Returns:
            list : List of visible elements
        """
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_all_elements_located(element_location)
            )
            return elements
        except TimeoutException:
            raise Exception(f"Elements with locator {element_location} could not be found within {self.timeout} seconds.")

    def wait_and_get_element_text(self,element_location):
        """Wait for element visibility and then return its text.

        Args:
            element_location (webElement): The desired element to location to operate.

        Returns:
            str : Text of the element
        """
        element = self.wait_element_visibility(element_location)
        return element.text

    def wait_element_clickablity_and_click_with_action_chain(self, element_location):
        """Wait element clickablity then click with ActionChain.

        Args:
            element_location (webElement): The desired element to location to operate.

        Raises:
            Exception: Raises exception after timeout error occurs.
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(element_location)
            )
            actions = AC(self.driver)
            actions.move_to_element(element)
            actions.click()
            actions.perform()
        except TimeoutException:
            raise Exception(f"Element : {element_location} could not clickable after {self.timeout} seconds.")

    def wait_element_visibility(self, element_location):
        """Check if element visible on page or not.

        Args:
            element_location (webElement): The desired element to location to operate.

        Raises:
            Exception: Raises exception after timeout error occurs.

        Returns:
            bool : True if the element is visible, otherwise False
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(element_location)
            )
        except TimeoutException:
            raise Exception(f"Element : {element_location} was not visible after {self.timeout} seconds.")

    def scroll_down(self, scroll_amount=200):
        """Scroll down the screen as desired amount.

        Args:
            scroll_amount (int, optional): _description_. Defaults to 200.
        """
        try:
            self.driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        except Exception as e:
            print(f"Error while scrolling: {str(e)}")