"""Job listing page actions.

It includes:
- Element locations for job processes
- Driver actions for filtering and validating jobs etc.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class JobListingsPage(BasePage):
    """Job listing page class.

    Args:
        BasePage: Inherited for common actions.
    """
    
    see_job_list_button_location = (
        By.XPATH, 
        '//div[@class="button-group d-flex flex-row"]//a[text()="See all QA jobs"]')
    location_filter_location = (
        By.ID, 
        'select2-filter-by-location-container')
    department_filter_location = (
        By.XPATH,
        '//span[@id="select2-filter-by-department-container" and text()="Quality Assurance"]')
    istanbul_option_location = (
        By.XPATH, 
        "//li[contains(text(),'Istanbul, Turkey')]")
    job_results_location = (
        By.CLASS_NAME, 
        'position-list-item')
    total_results_location = (
        By.CLASS_NAME, 
        'totalResult')
    job_title_location = (
        By.CLASS_NAME, 
        'position-title')
    job_department_location = (
        By.CLASS_NAME, 
        'position-department')
    job_location_location = (
        By.CLASS_NAME, 
        'position-location')
    view_role_button_location = (
        By.XPATH, 
        './/a[contains(@class, "btn") and text()="View Role"]')

    def filter_by_istanbul_location(self):
        """Filter jobs by Istanbul, Turkey."""
        self.wait_element_visibility_and_click(self.location_filter_location)
        self.wait_element_visibility_and_click(self.istanbul_option_location)

    def get_total_job_results(self):
        """Get total amount of filtered jobs.

        Returns:
            int : Amount of total job result.
        """
        return int(self.wait_and_get_element_text(self.total_results_location))

    def validate_job_details(self, job, expected_department, expected_location):
        """
        Validate of job listing details.

        Args:
            job (webElement): The job listing element to validate.
            expected_department (str): The expected department name for validation.
            expected_location (str): The expected location name for validation.

        Returns:
            bool: True if all validations pass, raises an Exception otherwise.
        """
        try:
            # Extract job details
            actual_department = job.find_element(*self.job_department_location).text
            actual_location = job.find_element(*self.job_location_location).text

            # Validate the details
            assert expected_department == actual_department, \
                f"'{actual_department}' department does not match expected '{expected_department}'."
            assert expected_location == actual_location, \
                f"'{actual_location}' department does not match expected '{expected_location}'."
            return True
        except AssertionError as e:
            print(e)
            return False

    def validate_lever_page_of_job(self, job_title):
        """
        Validate for lever page job and title of the lever page.

        Args:
            job_title (str): Title of the job.

        Returns:
            bool: True if all validations pass, raises an Exception otherwise.
        """
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        current_tab = self.driver.current_window_handle
        new_tab = [handle for handle in self.driver.window_handles if handle != current_tab][0]

        self.driver.switch_to.window(new_tab)
        try:
            
            self.wait_for_header_load_of_page()
            
            assert "lever.co" in self.driver.current_url, "Redirected URL is not lever page."
            assert job_title in self.driver.title, f"Job title '{job_title}' does not match on Lever page."
            return True
        except AssertionError as e:
            print("Error : " + e)
            return False
        finally:
            self.driver.close()  # Close the Lever page tab
            self.driver.switch_to.window(current_tab)
