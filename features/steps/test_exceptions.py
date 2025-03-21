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

@then("I should see the \"Exceptions information\" table")
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Exceptions information')]").is_displayed()

@then("the table should display exception details including Account No, Client Code, Shop Code, and Rule Type")
def step_impl(context):
    table = context.driver.find_element(By.ID, "exceptions_table")
    assert "Account No" in table.text
    assert "Client Code" in table.text
    assert "Shop Code" in table.text
    assert "Rule Type" in table.text

@when("I enter \"Lookup\" in the Rule Type filter")
def step_impl(context):
    filter_box = context.driver.find_element(By.ID, "rule_type_filter")
    filter_box.send_keys("Lookup")

@when("I apply the filter")
def step_impl(context):
    context.driver.find_element(By.ID, "apply_filter").click()
    time.sleep(2)

@then("only exceptions with the Rule Type \"Lookup\" should be displayed")
def step_impl(context):
    table = context.driver.find_element(By.ID, "exceptions_table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        assert "Lookup" in row.text

@when("I enter an Account No in the search box")
def step_impl(context):
    search_box = context.driver.find_element(By.ID, "search_box")
    search_box.send_keys("127199")

@when("I click the \"Search\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "search_button").click()
    time.sleep(2)

@then("the table should display only the matching exception")
def step_impl(context):
    table = context.driver.find_element(By.ID, "exceptions_table")
    assert "127199" in table.text

@when("I select an exception from the table")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//table//tr[1]").click()

@when("I click the \"Reprocess\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "reprocess_button").click()
    time.sleep(2)

@then("the selected exception should be reprocessed successfully")
def step_impl(context):
    success_message = context.driver.find_element(By.ID, "success_message")
    assert "Reprocessed successfully" in success_message.text

def after_scenario(context, scenario):
    context.driver.quit()
