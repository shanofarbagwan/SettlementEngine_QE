from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@given('I navigate to the "Meta Data" page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:4200/metadata")

@when('I click on "Add New"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Add New')]").click()

@when('I enter "{value}" in the "{field}" field')
def step_impl(context, value, field):
    field_mapping = {
        "File Name": "file_name",
        "File Type": "file_type",
        "File path raw": "file_path_raw",
        "File Path Cleansed": "file_path_cleansed",
        "File Pattern": "file_pattern",
        "File Max Size(MB)": "file_max_size",
        "File Delimeter": "file_delimeter",
        "Header Identifier": "header_identifier"
    }
    field_id = field_mapping[field]
    context.driver.find_element(By.NAME, field_id).send_keys(value)

@when('I click on "Submit"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()

@then('I should see the file "{file_name}" added in the table')
def step_impl(context, file_name):
    table = context.driver.find_element(By.XPATH, "//table")
    assert file_name in table.text

@when('I click on "Reset"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Reset')]").click()

@then('all input fields should be cleared')
def step_impl(context):
    inputs = context.driver.find_elements(By.TAG_NAME, "input")
    for field in inputs:
        assert field.get_attribute("value") == ""

@when('I click on "Cancel"')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Cancel')]").click()

@then('I should return to the "Meta Data" page without changes')
def step_impl(context):
    assert "Meta Data" in context.driver.title

@when('I click on the delete icon for file "{file_name}"')
def step_impl(context, file_name):
    delete_xpath = f"//td[contains(text(),'{file_name}')]/preceding-sibling::td//button[contains(@class, 'delete-icon')]"
    context.driver.find_element(By.XPATH, delete_xpath).click()

@when('I confirm the deletion')
def step_impl(context):
    context.driver.switch_to.alert.accept()

@then('I should not see "{file_name}" in the file table')
def step_impl(context, file_name):
    table = context.driver.find_element(By.XPATH, "//table")
    assert file_name not in table.text
