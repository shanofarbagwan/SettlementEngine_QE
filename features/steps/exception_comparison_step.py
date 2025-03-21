from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@given('the user is on the Exceptions Comparison page')
def step_open_exceptions_comparison_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://example.com/exceptions-comparison")

@when('the user selects "{rule_type}" as the rule type')
def step_select_rule_type(context, rule_type):
    rule_type_dropdown = Select(WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//select[@id='ruleType']"))
    ))
    rule_type_dropdown.select_by_visible_text(rule_type)

@when('the user selects "{severity}" as the severity')
def step_select_severity(context, severity):
    severity_dropdown = Select(context.driver.find_element(By.XPATH, "//select[@id='severity']"))
    severity_dropdown.select_by_visible_text(severity)

@when('the user enters the following exception details:')
def step_enter_exception_details(context):
    for row in context.table:
        context.driver.find_element(By.XPATH, "//input[@id='source1']").send_keys(row['Source1'])
        context.driver.find_element(By.XPATH, "//input[@id='source1Attribute']").send_keys(row['Source1 Attribute'])
        comparison_operator_dropdown = Select(context.driver.find_element(By.XPATH, "//select[@id='comparisonOperator']"))
        comparison_operator_dropdown.select_by_visible_text(row['Comparison Operator'])
        context.driver.find_element(By.XPATH, "//input[@id='source2']").send_keys(row['Source2'])
        context.driver.find_element(By.XPATH, "//input[@id='source2Attribute']").send_keys(row['Source2 Attribute'])
        status_dropdown = Select(context.driver.find_element(By.XPATH, "//select[@id='status']"))
        status_dropdown.select_by_visible_text(row['Status'])

@when('the user clicks on "{button_text}" button')
def step_click_button(context, button_text):
    button = context.driver.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")
    button.click()

@then('the exception should be saved successfully')
def step_exception_saved_successfully(context):
    success_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Exception saved successfully')]"))
    )
    assert success_message.is_displayed(), "Success message not displayed"

@then('close the browser')
def step_close_browser(context):
    context.driver.quit()
