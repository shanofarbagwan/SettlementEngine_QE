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

@when("I navigate to the \"Exceptions - Comparison\" section")
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Exceptions").click()
    context.driver.find_element(By.LINK_TEXT, "Comparison").click()
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

@then("the selected values should be displayed correctly")
def step_impl(context):
    assert context.driver.find_element(By.ID, "exception_category").get_attribute("value") == "Comparison"
    assert context.driver.find_element(By.ID, "severity").get_attribute("value") == "High"

@when('I select "{source}" as the Input Source')
def step_impl(context, source):
    dropdown = context.driver.find_element(By.ID, "input_source")
    dropdown.send_keys(source)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{attribute}" as the Attribute')
def step_impl(context, attribute):
    dropdown = context.driver.find_element(By.ID, "attribute")
    dropdown.send_keys(attribute)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{operator}" as the Comparison Operator')
def step_impl(context, operator):
    dropdown = context.driver.find_element(By.ID, "comparison_operator")
    dropdown.send_keys(operator)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{source2}" as the Source2')
def step_impl(context, source2):
    dropdown = context.driver.find_element(By.ID, "source2")
    dropdown.send_keys(source2)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{source2_attr}" as the Source2 Attribute')
def step_impl(context, source2_attr):
    dropdown = context.driver.find_element(By.ID, "source2_attribute")
    dropdown.send_keys(source2_attr)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{status}" as the Status')
def step_impl(context, status):
    dropdown = context.driver.find_element(By.ID, "status")
    dropdown.send_keys(status)
    dropdown.send_keys(Keys.RETURN)

@when("I click the \"Save\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "save_button").click()
    time.sleep(2)

@then("the newly added comparison rule should be displayed in the Comparison Explorer table")
def step_impl(context):
    table = context.driver.find_element(By.ID, "comparison_table")
    assert "Talyman" in table.text
    assert "Transaction Amount" in table.text
    assert ">=" in table.text
    assert "Agreement Amount" in table.text
    assert "New" in table.text

@when("I enter values in the Comparison Explorer form")
def step_impl(context):
    context.driver.find_element(By.ID, "input_source").send_keys("Talyman")
    context.driver.find_element(By.ID, "attribute").send_keys("Transaction Amount")
    context.driver.find_element(By.ID, "comparison_operator").send_keys(">=")
    context.driver.find_element(By.ID, "source2").send_keys("Talyman")
    context.driver.find_element(By.ID, "source2_attribute").send_keys("Agreement Amount")
    context.driver.find_element(By.ID, "status").send_keys("New")

@when("I click the \"Reset\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "reset_button").click()
    time.sleep(1)

@then("all fields in the Comparison Explorer form should be cleared")
def step_impl(context):
    assert context.driver.find_element(By.ID, "input_source").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "attribute").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "comparison_operator").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "source2").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "source2_attribute").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "status").get_attribute("value") == ""

def after_scenario(context, scenario):
    context.driver.quit()
