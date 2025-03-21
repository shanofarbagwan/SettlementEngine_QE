from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given("I am logged into the BNP Paribas system as an admin")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://example.com/login")  # Replace with actual URL
    context.driver.find_element(By.ID, "username").send_keys("admin")
    context.driver.find_element(By.ID, "password").send_keys("password123")
    context.driver.find_element(By.ID, "loginButton").click()
    time.sleep(3)  # Wait for the page to load

@when("I navigate to the \"Metadata Column\" section")
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Metadata Column").click()
    time.sleep(2)

@then("I should see the \"Metadata Update for Columns\" form")
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Metadata Update for Columns')]").is_displayed()

@when('I select a file "{file_name}"')
def step_impl(context, file_name):
    dropdown = context.driver.find_element(By.ID, "file_name")
    dropdown.send_keys(file_name)
    dropdown.send_keys(Keys.RETURN)

@when('I enter "{column_name}" in the Column Name field')
def step_impl(context, column_name):
    context.driver.find_element(By.ID, "column_name").send_keys(column_name)

@when('I select "{data_type}" as the Column Data Type')
def step_impl(context, data_type):
    dropdown = context.driver.find_element(By.ID, "column_data_type")
    dropdown.send_keys(data_type)
    dropdown.send_keys(Keys.RETURN)

@when('I enter "{column_null}" as the Column Null')
def step_impl(context, column_null):
    context.driver.find_element(By.ID, "column_null").send_keys(column_null)

@when('I enter "{column_match}" as the Column Match')
def step_impl(context, column_match):
    context.driver.find_element(By.ID, "column_match").send_keys(column_match)

@when('I enter "{max_size}" as the Max Size')
def step_impl(context, max_size):
    context.driver.find_element(By.ID, "max_size").send_keys(max_size)

@when('I enter "{date_format}" as the Column Date Format')
def step_impl(context, date_format):
    context.driver.find_element(By.ID, "column_date_format").send_keys(date_format)

@when('I click the "Submit" button')
def step_impl(context):
    context.driver.find_element(By.ID, "submit_button").click()
    time.sleep(2)

@then('I should see "{column}" in the metadata table column list')
def step_impl(context, column):
    table = context.driver.find_element(By.ID, "metadata_column_table")
    assert column in table.text

@when('I locate "{column}" in the metadata table column list')
def step_impl(context, column):
    context.column_row = context.driver.find_element(By.XPATH, f"//tr[td[contains(text(), '{column}')]]")

@when('I click the edit button for "{column}"')
def step_impl(context, column):
    context.column_row.find_element(By.CLASS_NAME, "edit-button").click()
    time.sleep(2)

@when('I update the Max Size to "{max_size}"')
def step_impl(context, max_size):
    input_field = context.driver.find_element(By.ID, "max_size")
    input_field.clear()
    input_field.send_keys(max_size)

@when('I click the delete button for "{column}"')
def step_impl(context, column):
    context.column_row.find_element(By.CLASS_NAME, "delete-button").click()
    time.sleep(1)

@when("I confirm the deletion")
def step_impl(context):
    context.driver.find_element(By.ID, "confirm_delete").click()
    time.sleep(2)

@then('"{column}" should be removed from the metadata table column list')
def step_impl(context, column):
    table = context.driver.find_element(By.ID, "metadata_column_table")
    assert column not in table.text

def after_scenario(context, scenario):
    context.driver.quit()
