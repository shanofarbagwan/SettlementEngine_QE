# features/pages/data_quality_page.py
from selenium import webdriver
from selenium.webdriver.common.by import By


class DataQualityPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_data_quality_assignment_page(self):
        self.driver.find_element(By.XPATH, "//button[text()='Metadata']").click()

    def is_data_quality_header_displayed(self):
        return self.driver.find_element(By.XPATH, "//h1[text()='Data Quality Assignment']").is_displayed()

    def is_data_quality_form_displayed(self):
        return self.driver.find_element(By.ID, "data-quality-form").is_displayed()

    def is_applied_data_quality_table_displayed(self):
        return self.driver.find_element(By.ID, "applied-data-quality-table").is_displayed()

    def fill_data_quality_form(self, source_table, source_attribute, dq_rule, start_date, end_date):
        self.driver.find_element(By.ID, "source-table").send_keys(source_table)
        self.driver.find_element(By.ID, "source-attribute").send_keys(source_attribute)
        self.driver.find_element(By.ID, "dq-rule").send_keys(dq_rule)
        self.driver.find_element(By.ID, "dq-start-date").send_keys(start_date)
        self.driver.find_element(By.ID, "dq-end-date").send_keys(end_date)

    def click_save(self):
        self.driver.find_element(By.ID, "save-button").click()

    def is_error_message_displayed(self):
        try:
            return self.driver.find_element(By.CLASS_NAME, "error-message").is_displayed()
        except:
            return False

    def is_download_button_visible(self):
        return self.driver.find_element(By.ID, "download-button").is_displayed()
