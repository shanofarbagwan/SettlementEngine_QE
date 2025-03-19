import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Load the feature file
scenarios("metadata_source_table.feature")

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("URL_OF_METADATA_SOURCE_TABLE_PAGE")  # Replace with actual URL
    yield driver
    driver.quit()

@given('the user is logged in as "Admin"')
def user_logged_in(browser):
    assert browser.find_element(By.CLASS_NAME, "user-profile").text == "John doe"

@given('the user is on the "Metadata Source Table" page')
@when('the user navigates to the "Metadata Source Table" page')
def open_metadata_source_page(browser):
    assert "Metadata Source Table" in browser.title

@then('the page title should be "Metadata Source Table"')
def verify_page_title(browser):
    assert "Metadata Source Table" in browser.title

@then('the "File Information" and "File Identification Settings" sections should be visible')
def verify_sections(browser):
    file_info = browser.find_element(By.ID, "file-info-section")  # Adjust locator
    file_id_settings = browser.find_element(By.ID, "file-id-settings-section")  # Adjust locator
    assert file_info.is_displayed()
    assert file_id_settings.is_displayed()

@then('the "Submit" and "Reset" buttons should be displayed')
def verify_buttons(browser):
    submit_button = browser.find_element(By.ID, "submit-button")  # Adjust locator
    reset_button = browser.find_element(By.ID, "reset-button")  # Adjust locator
    assert submit_button.is_displayed()
    assert reset_button.is_displayed()

@then('the metadata source table should be visible')
def verify_metadata_table(browser):
    table = browser.find_element(By.ID, "metadata-source-table")  # Adjust locator
    assert table.is_displayed()

@then('it should display columns "File Type", "File Name", "File Path Raw", "File Date", "Created By"')
def verify_table_columns(browser):
    columns = [col.text for col in browser.find_elements(By.XPATH, "//table/thead/tr/th")]
    expected_columns = ["File Type", "File Name", "File Path Raw", "File Date", "Created By"]
    assert all(col in columns for col in expected_columns)

@when('the user enters "TestFile" in the "File Name" field')
def enter_file_name(browser):
    input_field = browser.find_element(By.ID, "file-name-input")  # Adjust locator
    input_field.send_keys("TestFile")

@when('the user selects "CSV" from the "File Type" dropdown')
def select_file_type(browser):
    dropdown = Select(browser.find_element(By.ID, "file-type-dropdown"))  # Adjust locator
    dropdown.select_by_visible_text("CSV")

@when('the user enters "Pattern123" in the "File Pattern" field')
def enter_file_pattern(browser):
    input_field = browser.find_element(By.ID, "file-pattern-input")  # Adjust locator
    input_field.send_keys("Pattern123")

@when('the user enters "1000" in the "File Max Size (MB)" field')
def enter_file_size(browser):
    input_field = browser.find_element(By.ID, "file-size-input")  # Adjust locator
    input_field.send_keys("1000")

@then('the respective input fields should contain the entered values')
def verify_input_values(browser):
    assert browser.find_element(By.ID, "file-name-input").get_attribute("value") == "TestFile"
    assert browser.find_element(By.ID, "file-pattern-input").get_attribute("value") == "Pattern123"
    assert browser.find_element(By.ID, "file-size-input").get_attribute("value") == "1000"

@when('the user clicks the "Submit" button')
def click_submit(browser):
    button = browser.find_element(By.ID, "submit-button")  # Adjust locator
    button.click()

@then('a success message should be displayed')
def verify_success_message(browser):
    message = browser.find_element(By.CLASS_NAME, "success-message")  # Adjust locator
    assert message.is_displayed()

@when('the user clicks the "Reset" button')
def click_reset(browser):
    button = browser.find_element(By.ID, "reset-button")  # Adjust locator
    button.click()

@then('all input fields should be cleared')
def verify_reset(browser):
    assert browser.find_element(By.ID, "file-name-input").get_attribute("value") == ""
    assert browser.find_element(By.ID, "file-pattern-input").get_attribute("value") == ""
    assert browser.find_element(By.ID, "file-size-input").get_attribute("value") == ""

@when('the user clicks the "Next Page" button')
def click_next_page(browser):
    next_button = browser.find_element(By.CLASS_NAME, "next-page")  # Adjust locator
    next_button.click()

@then('the next set of metadata source entries should be displayed')
def verify_next_page(browser):
    assert "page=2" in browser.current_url  # Assuming URL updates on pagination

@when('the user clicks the "Previous Page" button')
def click_previous_page(browser):
    prev_button = browser.find_element(By.CLASS_NAME, "previous-page")  # Adjust locator
    prev_button.click()

@then('the previous set of metadata source entries should be displayed')
def verify_previous_page(browser):
    assert "page=1" in browser.current_url  # Assuming URL updates on pagination

