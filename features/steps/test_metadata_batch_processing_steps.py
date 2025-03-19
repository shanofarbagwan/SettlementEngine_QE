import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Load the feature file
scenarios("metadata_batch_processing.feature")

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("URL_OF_METADATA_BATCH_PROCESSING_PAGE")  # Replace with actual URL
    yield driver
    driver.quit()

@given('the user is logged in as "Admin"')
def user_logged_in(browser):
    assert browser.find_element(By.CLASS_NAME, "user-profile").text == "John doe"

@given('the user is on the "Metadata Batch Processing" page')
@when('the user navigates to the "Metadata Batch Processing" page')
def open_metadata_batch_page(browser):
    assert "Metadata Batch Processing" in browser.title

@then('the page title should be "Metadata Batch Processing"')
def verify_page_title(browser):
    assert "Metadata Batch Processing" in browser.title

@then('the "Batch Processing Information" section should be visible')
def verify_batch_processing_section(browser):
    section = browser.find_element(By.CLASS_NAME, "batch-processing-section")  # Adjust locator
    assert section.is_displayed()

@then('the "Submit" and "Reset" buttons should be displayed')
def verify_buttons(browser):
    submit_button = browser.find_element(By.ID, "submit-button")  # Adjust locator
    reset_button = browser.find_element(By.ID, "reset-button")  # Adjust locator
    assert submit_button.is_displayed()
    assert reset_button.is_displayed()

@then('the batch processing table should be visible')
def verify_batch_table(browser):
    table = browser.find_element(By.ID, "batch-processing-table")  # Adjust locator
    assert table.is_displayed()

@then('it should display columns "Batch Name", "Frequency", "Source System", "File Date", "Created By"')
def verify_table_columns(browser):
    columns = [col.text for col in browser.find_elements(By.XPATH, "//table/thead/tr/th")]
    expected_columns = ["Batch Name", "Frequency", "Source System", "File Date", "Created By"]
    assert all(col in columns for col in expected_columns)

@when('the user clicks on the "Frequency" dropdown')
def click_frequency_dropdown(browser):
    dropdown = browser.find_element(By.ID, "frequency-dropdown")  # Adjust locator
    dropdown.click()

@then('the dropdown should display options "Daily", "Monthly", "One-Off"')
def verify_dropdown_options(browser):
    dropdown = Select(browser.find_element(By.ID, "frequency-dropdown"))  # Adjust locator
    options = [option.text for option in dropdown.options]
    assert "Daily" in options
    assert "Monthly" in options
    assert "One-Off" in options

@when('the user enters "Test System" in the "Source System" input field')
def enter_source_system(browser):
    input_field = browser.find_element(By.ID, "source-system-input")  # Adjust locator
    input_field.send_keys("Test System")

@then('the "Source System" field should contain "Test System"')
def verify_source_system_input(browser):
    input_field = browser.find_element(By.ID, "source-system-input")  # Adjust locator
    assert input_field.get_attribute("value") == "Test System"

@when('the user selects "Daily" from the "Frequency" dropdown')
def select_frequency(browser):
    dropdown = Select(browser.find_element(By.ID, "frequency-dropdown"))  # Adjust locator
    dropdown.select_by_visible_text("Daily")

@when('the user clicks the "Submit" button')
def click_submit(browser):
    button = browser.find_element(By.ID, "submit-button")  # Adjust locator
    button.click()

@then('a success message should be displayed')
def verify_success_message(browser):
    message = browser.find_element(By.CLASS_NAME, "success-message")  # Adjust locator
    assert message.is_displayed()

@then('the new batch entry should be added to the batch processing table')
def verify_new_entry_in_table(browser):
    table = browser.find_element(By.ID, "batch-processing-table")  # Adjust locator
    rows = table.find_elements(By.TAG_NAME, "tr")
    assert len(rows) > 1  # Ensure new row is added

@when('the user clicks the "Reset" button')
def click_reset(browser):
    button = browser.find_element(By.ID, "reset-button")  # Adjust locator
    button.click()

@then('the "Frequency" dropdown should be reset')
def verify_reset_frequency(browser):
    dropdown = Select(browser.find_element(By.ID, "frequency-dropdown"))  # Adjust locator
    assert dropdown.first_selected_option.text == "Select"

@then('the "Source System" input field should be empty')
def verify_reset_source_system(browser):
    input_field = browser.find_element(By.ID, "source-system-input")  # Adjust locator
    assert input_field.get_attribute("value") == ""

@when('the user clicks the "Next Page" button')
def click_next_page(browser):
    next_button = browser.find_element(By.CLASS_NAME, "next-page")  # Adjust locator
    next_button.click()

@then('the next set of batch entries should be displayed')
def verify_next_page(browser):
    assert "page=2" in browser.current_url  # Assuming URL updates on pagination

@when('the user clicks the "Previous Page" button')
def click_previous_page(browser):
    prev_button = browser.find_element(By.CLASS_NAME, "previous-page")  # Adjust locator
    prev_button.click()

@then('the previous set of batch entries should be displayed')
def verify_previous_page(browser):
    assert "page=1" in browser.current_url  # Assuming URL updates on pagination
