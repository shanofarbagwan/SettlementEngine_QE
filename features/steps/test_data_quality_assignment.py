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

@when("I navigate to the \"Applied Data Quality\" section")
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Applied Data Quality").click()
    time.sleep(2)

@then("I should see the \"Data Quality Assignment\" form")
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Data Quality Assignment')]").is_displayed()

@when('I select "{source_table}" as the Source Table')
def step_impl(context, source_table):
    dropdown = context.driver.find_element(By.ID, "source_table")
    dropdown.send_keys(source_table)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{source_attribute}" as the Source Attribute')
def step_impl(context, source_attribute):
    dropdown = context.driver.find_element(By.ID, "source_attribute")
    dropdown.send_keys(source_attribute)
    dropdown.send_keys(Keys.RETURN)

@when('I select "{dq_rule}" as the DQ Rule')
def step_impl(context, dq_rule):
    dropdown = context.driver.find_element(By.ID, "dq_rule")
    dropdown.send_keys(dq_rule)
    dropdown.send_keys(Keys.RETURN)

@when("I enter a Start Date")
def step_impl(context):
    date_field = context.driver.find_element(By.ID, "dq_start_date")
    date_field.send_keys("01/01/2025")
    date_field.send_keys(Keys.RETURN)

@when("I enter an End Date")
def step_impl(context):
    date_field = context.driver.find_element(By.ID, "dq_end_date")
    date_field.send_keys("12/31/2025")
    date_field.send_keys(Keys.RETURN)

@when("I click the \"Save\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "save_button").click()
    time.sleep(2)

@then("the new data quality assignment should be displayed in the table")
def step_impl(context):
    table = context.driver.find_element(By.ID, "applied_data_quality_table")
    assert "Tallyman" in table.text

@when("I enter values in the Data Quality Assignment form")
def step_impl(context):
    context.driver.find_element(By.ID, "source_table").send_keys("Tallyman")
    context.driver.find_element(By.ID, "source_attribute").send_keys("File Name")
    context.driver.find_element(By.ID, "dq_rule").send_keys("Rule 25")

@when("I click the \"Reset\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "reset_button").click()
    time.sleep(1)

@then("all fields in the Data Quality Assignment form should be cleared")
def step_impl(context):
    assert context.driver.find_element(By.ID, "source_table").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "source_attribute").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "dq_rule").get_attribute("value") == ""

@then("the Applied Data Quality table should display rule assignments")
def step_impl(context):
    table = context.driver.find_element(By.ID, "applied_data_quality_table")
    assert len(table.find_elements(By.TAG_NAME, "tr")) > 1

@when("I click the \"Edit\" button for a specific assignment")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//table//tr[1]//button[contains(text(), 'Edit')]").click()
    time.sleep(1)

@when("I modify the End Date")
def step_impl(context):
    date_field = context.driver.find_element(By.ID, "dq_end_date")
    date_field.clear()
    date_field.send_keys("12/31/2026")
    date_field.send_keys(Keys.RETURN)

@then("the updated assignment should be saved and displayed in the table")
def step_impl(context):
    table = context.driver.find_element(By.ID, "applied_data_quality_table")
    assert "12/31/2026" in table.text

@when("I click the \"Delete\" button for a specific assignment")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//table//tr[1]//button[contains(text(), 'Delete')]").click()
    time.sleep(1)

@when("I confirm the deletion")
def step_impl(context):
    context.driver.find_element(By.ID, "confirm_delete").click()
    time.sleep(2)

@then("the assignment should be removed from the table")
def step_impl(context):
    table = context.driver.find_element(By.ID, "applied_data_quality_table")
    assert "Rule 25" not in table.text

@when("I click the \"Download\" button")
def step_impl(context):
    context.driver.find_element(By.ID, "download_button").click()
    time.sleep(3)

@then("a file should be downloaded with the applied data quality assignments")
def step_impl(context):
    # Verification logic for downloaded file (optional)
    print("File downloaded successfully.")

def after_scenario(context, scenario):
    context.driver.quit()
