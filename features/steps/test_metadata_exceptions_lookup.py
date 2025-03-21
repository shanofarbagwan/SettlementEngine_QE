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

@when("I navigate to the \"Exceptions - Look-up\" section")
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Exceptions").click()
    context.driver.find_element(By.LINK_TEXT, "Look-up").click()
    time.sleep(2)

@then("I should see the \"Exceptions Update\" form")
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Exceptions Update')]").is_displayed()

@when('I select "{category}" as the Exception Category')
def step_impl(context, category):
    dropdown = context.driver.find_element(By.ID, "exception_category")
    dropdown.send_keys(category)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{severity}" as the Severity')
def step_impl(context, severity):
    dropdown = context.driver.find_element(By.ID, "severity")
    dropdown.send_keys(severity)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{owner}" as the Exception Owner')
def step_impl(context, owner):
    dropdown = context.driver.find_element(By.ID, "exception_owner")
    dropdown.send_keys(owner)
    dropdown.send_keys(Keys.RETURN)

@then('the selected values should be displayed correctly')
def step_impl(context):
    assert context.driver.find_element(By.ID, "exception_category").get_attribute("value") == "Lookup"
    assert context.driver.find_element(By.ID, "severity").get_attribute("value") == "High"
    assert context.driver.find_element(By.ID, "exception_owner").get_attribute("value") == "John Doe"

@when("I click the \"Add Look-up\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "add_lookup").click()
    time.sleep(1)

@when('I select "{source}" as the Input Source')
def step_impl(context, source):
    dropdown = context.driver.find_element(By.ID, "input_source")
    dropdown.send_keys(source)
    dropdown.send_keys(Keys.RETURN)

@when('I set "{num}" as the No of Attributes')
def step_impl(context, num):
    input_field = context.driver.find_element(By.ID, "num_attributes")
    input_field.clear()
    input_field.send_keys(num)

@when('I enter "{value}" in Attribute {attr_num}')
def step_impl(context, value, attr_num):
    attr_id = f"attribute_{attr_num}"
    input_field = context.driver.find_element(By.ID, attr_id)
    input_field.clear()
    input_field.send_keys(value)

@when("I click the \"Save\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "save_button").click()
    time.sleep(2)

@then("the newly added lookup entry should be displayed in the Lookup Explorer table")
def step_impl(context):
    table = context.driver.find_element(By.ID, "lookup_table")
    assert "Talyman" in table.text
    assert "Client Code" in table.text
    assert "Shop Code" in table.text

@when('I locate "{lookup_name}" in the Lookup Explorer table')
def step_impl(context, lookup_name):
    context.lookup_row = context.driver.find_element(By.XPATH, f"//tr[td[contains(text(), '{lookup_name}')]]")

@when('I click the delete button for "{lookup_name}"')
def step_impl(context, lookup_name):
    context.lookup_row.find_element(By.CLASS_NAME, "delete-button").click()
    time.sleep(1)

@when("I confirm the deletion")
def step_impl(context):
    context.driver.find_element(By.ID, "confirm_delete").click()
    time.sleep(2)

@then('"{lookup_name}" should be removed from the Lookup Explorer table')
def step_impl(context, lookup_name):
    table = context.driver.find_element(By.ID, "lookup_table")
    assert lookup_name not in table.text

@when("I enter values in the Lookup Explorer form")
def step_impl(context):
    context.driver.find_element(By.ID, "input_source").send_keys("Talyman")
    context.driver.find_element(By.ID, "num_attributes").send_keys("4")
    context.driver.find_element(By.ID, "attribute_1").send_keys("Client Code")
    context.driver.find_element(By.ID, "attribute_2").send_keys("Shop Code")

@when("I click the \"Reset\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "reset_button").click()
    time.sleep(1)

@then("all fields in the Lookup Explorer form should be cleared")
def step_impl(context):
    assert context.driver.find_element(By.ID, "input_source").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "num_attributes").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "attribute_1").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "attribute_2").get_attribute("value") == ""

def after_scenario(context, scenario):
    context.driver.quit()
