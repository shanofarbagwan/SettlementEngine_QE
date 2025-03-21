from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given("I am on the \"Exceptions\" page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://example.com/exceptions")  # Replace with actual URL
    time.sleep(3)

@when("I click on an exception entry")
def step_impl(context):
    exception_entry = context.driver.find_element(By.XPATH, "//table//tr[1]")  # Select first exception row
    exception_entry.click()
    time.sleep(2)

@then("the \"Exceptions Information\" popup should be displayed")
def step_impl(context):
    popup = context.driver.find_element(By.CLASS_NAME, "popup-container")  # Update with actual class name
    assert popup.is_displayed()

@then("the popup should display impacted attributes, rule type, account number, and client code")
def step_impl(context):
    popup_text = context.driver.find_element(By.CLASS_NAME, "popup-content").text  # Adjust class
    assert "Impacted Attr" in popup_text
    assert "Rule Type" in popup_text
    assert "Account No" in popup_text
    assert "Client Code" in popup_text

@when("I click the \"Cancel\" button")
def step_impl(context):
    cancel_button = context.driver.find_element(By.XPATH, "//button[contains(text(), 'Cancel')]")
    cancel_button.click()
    time.sleep(2)

@then("the popup should be closed")
def step_impl(context):
    popups = context.driver.find_elements(By.CLASS_NAME, "popup-container")
    assert len(popups) == 0  # No popups should be visible

@when("I scroll down within the popup")
def step_impl(context):
    popup = context.driver.find_element(By.CLASS_NAME, "popup-content")  # Adjust as needed
    context.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
    time.sleep(2)

@then("I should be able to view additional exception details")
def step_impl(context):
    popup_text = context.driver.find_element(By.CLASS_NAME, "popup-content").text
    assert "Source Attribute" in popup_text  # Ensure content at the bottom is visible

def after_scenario(context, scenario):
    context.driver.quit()
