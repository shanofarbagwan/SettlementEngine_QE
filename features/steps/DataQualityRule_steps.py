# steps.py
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user is on the Data Quality Rule page')
def step_open_data_quality_rule_page(context):
    context.driver.get("https://example.com/data-quality-rule")

@when('the user enters Rule ID "{rule_id}"')
def step_enter_rule_id(context, rule_id):
    rule_id_field = context.driver.find_element(By.ID, "rule_id")
    rule_id_field.clear()
    rule_id_field.send_keys(rule_id)

@when('the user enters Rule Expression "{rule_expression}"')
def step_enter_rule_expression(context, rule_expression):
    rule_expression_field = context.driver.find_element(By.ID, "rule_expression")
    rule_expression_field.clear()
    rule_expression_field.send_keys(rule_expression)

@when('the user enters Rule Description "{rule_description}"')
def step_enter_rule_description(context, rule_description):
    rule_description_field = context.driver.find_element(By.ID, "rule_description")
    rule_description_field.clear()
    rule_description_field.send_keys(rule_description)

@when('the user clicks "{button_text}"')
def step_click_button(context, button_text):
    button = context.driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
    button.click()

@then('the rule should be added successfully')
def step_rule_added_successfully(context):
    success_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Rule added successfully')]"))
    )
    assert success_message.is_displayed(), "Success message not displayed"

@then('the form should be reset')
def step_form_reset(context):
    rule_id_field = context.driver.find_element(By.ID, "rule_id")
    assert rule_id_field.get_attribute('value') == "", "Rule ID field not reset"

@then('the rule table should display existing rules')
def step_verify_rule_table(context):
    table = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "rule_table"))
    )
    rows = table.find_elements(By.TAG_NAME, "tr")
    assert len(rows) > 1, "No rules found in the table"
