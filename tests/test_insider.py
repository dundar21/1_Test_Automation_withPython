"""test case for useinsider web page actions"""
import pytest
import time
from page_objects.base_page import BasePage
from page_objects.careers_page import CareersPage
from page_objects.job_listing_page import JobListingsPage

class TestInsider:
    """Insider test case class."""
    
    def test_open_site(self, browser):
        """Test to check whether the Insider site open."""

        base_page_actions = BasePage(browser)
        base_page_actions.get_page("https://useinsider.com/")
        assert \
        "#1 Leader in Individualized, Cross-Channel CX — Insider" in \
        base_page_actions.get_title(), \
        "Homepage title does not match."

    def test_open_careers_from_company_menu(self, browser):
        """Test to verify the enterance to Careers page with checking necessary page headers."""

        career_page_actions = CareersPage(browser)
        career_page_actions.get_page("https://useinsider.com/")
        career_page_actions.navigate_to_careers()
        #Entrance of the Careers page check
        assert "Ready to disrupt? | Insider Careers" in career_page_actions.get_title()
        # Iterate through the header tags and add tag names to the header list
        headers = [header.text for header in career_page_actions.find_multiple_elements(career_page_actions.headers_tag_location)]
        #Location check
        assert "Our Locations" in  headers
        #Teams check
        assert "Find your calling" in  headers
        #Life at insider check
        assert "Life at Insider" in  headers

    def test_quality_assurance_job_search_for_istanbul_turkey(self,browser):
        """Test for search job in Istanbul, Turkey."""

        job_search_actions = JobListingsPage(browser)
        job_search_actions.get_page("https://useinsider.com/careers/quality-assurance/")
        job_search_actions.wait_element_clickability_and_click(
            job_search_actions.see_job_list_button_location)
        #Wait for visiblity of Quality Assurance as department and load of all locations
        job_search_actions.wait_element_visibility(job_search_actions.department_filter_location)
        job_search_actions.filter_by_istanbul_location()
        #Scroll the screen down to see job list count
        job_search_actions.scroll_down(600)
        #Waiting job results visibility on screen
        job_search_actions.wait_element_visibility(job_search_actions.total_results_location)
        #delay for consistent job result calculation
        time.sleep(5)
        #check for total jobs counter returns greater than 0.
        assert job_search_actions.get_total_job_results() > 0, \
            "No jobs found after filtering."
        #Job list of all listed elements
        jobs_list = job_search_actions.find_presence_of_elements(job_search_actions.job_results_location)
        for job in jobs_list:
            is_job_validated = job_search_actions.validate_job_details(
                job = job,
                expected_department = "Quality Assurance",
                expected_location = "Istanbul, Turkey"
            )
            #Check jobs' detailes
            assert is_job_validated is True
            #Job title
            job_title_name = job.find_element(*job_search_actions.job_title_location).text
            #View role button
            view_role = job.find_element(*job_search_actions.view_role_button_location)
            view_role.click()

            #Check job lever page
            assert job_search_actions.validate_lever_page_of_job(job_title_name) is True