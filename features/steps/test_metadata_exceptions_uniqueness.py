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

@when("I navigate to the \"Exceptions - Uniqueness\" section")
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Exceptions").click()
    context.driver.find_element(By.LINK_TEXT, "Uniqueness").click()
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
    assert context.driver.find_element(By.ID, "exception_category").get_attribute("value") == "Unique"
    assert context.driver.find_element(By.ID, "severity").get_attribute("value") == "High"

@when('I select "{source}" as the Input Source')
def step_impl(context, source):
    dropdown = context.driver.find_element(By.ID, "input_source")
    dropdown.send_keys(source)
    dropdown.send_keys(Keys.RETURN)

@when('I enter "{num}" as the Number of Attributes')
def step_impl(context, num):
    input_field = context.driver.find_element(By.ID, "num_attributes")
    input_field.clear()
    input_field.send_keys(num)

@when('I select "{attribute1}" as Attribute 1')
def step_impl(context, attribute1):
    dropdown = context.driver.find_element(By.ID, "attribute1")
    dropdown.send_keys(attribute1)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{attribute2}" as Attribute 2')
def step_impl(context, attribute2):
    dropdown = context.driver.find_element(By.ID, "attribute2")
    dropdown.send_keys(attribute2)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{attribute3}" as Attribute 3')
def step_impl(context, attribute3):
    dropdown = context.driver.find_element(By.ID, "attribute3")
    dropdown.send_keys(attribute3)
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

@then("the newly added uniqueness rule should be displayed in the Unique Explorer table")
def step_impl(context):
    table = context.driver.find_element(By.ID, "unique_table")
    assert "Talyman" in table.text
    assert "Transaction ID" in table.text
    assert "Agreement ID" in table.text
    assert "Client ID" in table.text
    assert "New" in table.text

@when("I enter values in the Uniqueness Explorer form")
def step_impl(context):
    context.driver.find_element(By.ID, "input_source").send_keys("Talyman")
    context.driver.find_element(By.ID, "num_attributes").send_keys("3")
    context.driver.find_element(By.ID, "attribute1").send_keys("Transaction ID")
    context.driver.find_element(By.ID, "attribute2").send_keys("Agreement ID")
    context.driver.find_element(By.ID, "attribute3").send_keys("Client ID")
    context.driver.find_element(By.ID, "status").send_keys("New")

@when("I click the \"Reset\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "reset_button").click()
    time.sleep(1)

@then("all fields in the Uniqueness Explorer form should be cleared")
def step_impl(context):
    assert context.driver.find_element(By.ID, "input_source").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "num_attributes").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "attribute1").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "attribute2").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "attribute3").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "status").get_attribute("value") == ""

def after_scenario(context, scenario):
    context.driver.quit()
