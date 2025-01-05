"""Careers page actions.

It includes:
- Navigate to careers page
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CareersPage(BasePage):
    """Careers Page class.

    Args:
        BasePage: Inherited for common actions.
    """
    
    company_menu_location = (By.XPATH, '//a[contains(text(),"Company")]')
    career_link_location = (By.XPATH, '//a[contains(text(),"Careers")]')
    headers_tag_location = (By.XPATH, '//h1 | //h2 | //h3 | //h4 | //h5 | //h6')

    def navigate_to_careers(self):
        """Navigate to careers page."""
        self.wait_element_clickablity_and_click_with_action_chain(self.company_menu_location)
        self.wait_element_clickablity_and_click_with_action_chain(self.career_link_location)
        self.wait_for_header_load_of_page()