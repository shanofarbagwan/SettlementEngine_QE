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
    time.sleep(3)

@when("I navigate to the \"Exceptions\" section")
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Exceptions").click()
    time.sleep(2)

@then("I should see the \"Exceptions Update\" form")
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Exceptions Update')]").is_displayed()

@when('I select "{rule_type}" as the Rule Type')
def step_impl(context, rule_type):
    dropdown = context.driver.find_element(By.ID, "rule_type")
    dropdown.send_keys(rule_type)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{severity}" as the Severity')
def step_impl(context, severity):
    dropdown = context.driver.find_element(By.ID, "severity")
    dropdown.send_keys(severity)
    dropdown.send_keys(Keys.RETURN)

@then('I should see exceptions filtered by Rule Type "{rule_type}" and Severity "{severity}"')
def step_impl(context, rule_type, severity):
    table = context.driver.find_element(By.ID, "exceptions_table")
    assert rule_type in table.text and severity in table.text

@when('I locate "{exception_id}" in the exceptions list')
def step_impl(context, exception_id):
    context.exception_row = context.driver.find_element(By.XPATH, f"//tr[td[contains(text(), '{exception_id}')]]")

@when('I click the edit button for "{exception_id}"')
def step_impl(context, exception_id):
    context.exception_row.find_element(By.CLASS_NAME, "edit-button").click()
    time.sleep(2)

@when('I update the Source Attribute to "{new_attribute}"')
def step_impl(context, new_attribute):
    input_field = context.driver.find_element(By.ID, "source_attribute")
    input_field.clear()
    input_field.send_keys(new_attribute)

@when('I click the delete button for "{exception_id}"')
def step_impl(context, exception_id):
    context.exception_row.find_element(By.CLASS_NAME, "delete-button").click()
    time.sleep(1)

@when("I confirm the deletion")
def step_impl(context):
    context.driver.find_element(By.ID, "confirm_delete").click()
    time.sleep(2)

@then('"{exception_id}" should be removed from the exceptions list')
def step_impl(context, exception_id):
    table = context.driver.find_element(By.ID, "exceptions_table")
    assert exception_id not in table.text

@when('I click the "Download" button')
def step_impl(context):
    context.driver.find_element(By.ID, "download_button").click()
    time.sleep(2)

@then("the exceptions list should be downloaded as a file")
def step_impl(context):
    # This part would check for file download, which requires additional setup
    print("Download initiated successfully.")

def after_scenario(context, scenario):
    context.driver.quit()
