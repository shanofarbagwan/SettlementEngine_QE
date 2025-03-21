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

@when("I navigate to the \"Rule Mapping\" section")
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Rule Mapping").click()
    time.sleep(2)

@then("I should see the \"Metadata Update for Rule Mapping\" form")
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Metadata Update for Rule Mapping')]").is_displayed()

@when('I enter "{name}" in the Attribute Name field')
def step_impl(context, name):
    context.driver.find_element(By.ID, "attribute_name").send_keys(name)

@when('I select "{identifier}" as the Record Identifier')
def step_impl(context, identifier):
    dropdown = context.driver.find_element(By.ID, "record_identifier")
    dropdown.send_keys(identifier)
    dropdown.send_keys(Keys.RETURN)

@when('I enter "{order}" as the Attribute Order')
def step_impl(context, order):
    context.driver.find_element(By.ID, "attribute_order").send_keys(order)

@when('I enter "{position}" as the Attribute Start Position')
def step_impl(context, position):
    context.driver.find_element(By.ID, "attribute_start_position").send_keys(position)

@when('I select "{data_type}" as the Attribute Data Type')
def step_impl(context, data_type):
    dropdown = context.driver.find_element(By.ID, "attribute_data_type")
    dropdown.send_keys(data_type)
    dropdown.send_keys(Keys.RETURN)

@when('I click the "Save" button')
def step_impl(context):
    context.driver.find_element(By.ID, "save_button").click()
    time.sleep(2)

@then('I should see "{rule}" in the metadata rule list')
def step_impl(context, rule):
    table = context.driver.find_element(By.ID, "metadata_rule_table")
    assert rule in table.text

@when('I locate "{rule}" in the metadata rule list')
def step_impl(context, rule):
    context.rule_row = context.driver.find_element(By.XPATH, f"//tr[td[contains(text(), '{rule}')]]")

@when('I click the edit button for "{rule}"')
def step_impl(context, rule):
    context.rule_row.find_element(By.CLASS_NAME, "edit-button").click()
    time.sleep(2)

@when('I update the Attribute Order to "{order}"')
def step_impl(context, order):
    input_field = context.driver.find_element(By.ID, "attribute_order")
    input_field.clear()
    input_field.send_keys(order)

@when('I click the delete button for "{rule}"')
def step_impl(context, rule):
    context.rule_row.find_element(By.CLASS_NAME, "delete-button").click()
    time.sleep(1)

@when("I confirm the deletion")
def step_impl(context):
    context.driver.find_element(By.ID, "confirm_delete").click()
    time.sleep(2)

@then('"{rule}" should be removed from the metadata rule list')
def step_impl(context, rule):
    table = context.driver.find_element(By.ID, "metadata_rule_table")
    assert rule not in table.text

@when("I click the \"Upload\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "upload_button").click()

@when("I select a valid metadata rule file")
def step_impl(context):
    upload_input = context.driver.find_element(By.ID, "file_upload")
    upload_input.send_keys("/path/to/file.csv")  # Replace with actual path
    time.sleep(2)

@when("I confirm the upload")
def step_impl(context):
    context.driver.find_element(By.ID, "confirm_upload").click()
    time.sleep(2)

@then("I should see a success message")
def step_impl(context):
    success_msg = context.driver.find_element(By.CLASS_NAME, "success-message")
    assert success_msg.is_displayed()

def after_scenario(context, scenario):
    context.driver.quit()
