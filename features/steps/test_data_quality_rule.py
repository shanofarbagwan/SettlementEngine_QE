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

@when("I navigate to the \"Data Quality Rule\" section")
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Data Quality Rule").click()
    time.sleep(2)

@then("I should see the \"Data Quality Rule\" form")
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Data Quality Rule')]").is_displayed()

@when('I select "{rule_type}" as the Rule Type')
def step_impl(context, rule_type):
    dropdown = context.driver.find_element(By.ID, "rule_expression")
    dropdown.send_keys(rule_type)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{severity}" as the Severity')
def step_impl(context, severity):
    dropdown = context.driver.find_element(By.ID, "severity")
    dropdown.send_keys(severity)
    dropdown.send_keys(Keys.RETURN)

@when('I enter "{description}" in the Rule Description field')
def step_impl(context, description):
    input_field = context.driver.find_element(By.ID, "rule_description")
    input_field.clear()
    input_field.send_keys(description)

@when("I click the \"Save\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "save_button").click()
    time.sleep(2)

@then("the new data quality rule should be displayed in the table")
def step_impl(context):
    table = context.driver.find_element(By.ID, "data_quality_table")
    assert "Sample Rule Description" in table.text

@when("I enter values in the Data Quality Rule form")
def step_impl(context):
    context.driver.find_element(By.ID, "rule_expression").send_keys("Rule Expression")
    context.driver.find_element(By.ID, "severity").send_keys("High")
    context.driver.find_element(By.ID, "rule_description").send_keys("Sample Rule")

@when("I click the \"Reset\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "reset_button").click()
    time.sleep(1)

@then("all fields in the Data Quality Rule form should be cleared")
def step_impl(context):
    assert context.driver.find_element(By.ID, "rule_expression").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "severity").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "rule_description").get_attribute("value") == ""

@then("the Data Quality Rule table should display rule entries")
def step_impl(context):
    table = context.driver.find_element(By.ID, "data_quality_table")
    assert len(table.find_elements(By.TAG_NAME, "tr")) > 1

@when("I click the \"Edit\" button for a specific rule")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//table//tr[1]//button[contains(text(), 'Edit')]").click()
    time.sleep(1)

@when('I modify the Rule Description to "{new_description}"')
def step_impl(context, new_description):
    input_field = context.driver.find_element(By.ID, "rule_description")
    input_field.clear()
    input_field.send_keys(new_description)

@then("the updated rule should be saved and displayed in the table")
def step_impl(context):
    table = context.driver.find_element(By.ID, "data_quality_table")
    assert "Updated Description" in table.text

@when("I click the \"Delete\" button for a specific rule")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//table//tr[1]//button[contains(text(), 'Delete')]").click()
    time.sleep(1)

@when("I confirm the deletion")
def step_impl(context):
    context.driver.find_element(By.ID, "confirm_delete").click()
    time.sleep(2)

@then("the rule should be removed from the table")
def step_impl(context):
    table = context.driver.find_element(By.ID, "data_quality_table")
    assert "Sample Rule Description" not in table.text

def after_scenario(context, scenario):
    context.driver.quit()
