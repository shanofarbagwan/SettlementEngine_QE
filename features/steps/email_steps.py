from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then

@given('the user is on the "Email Template" page')
def step_open_email_template_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://your-app-url.com/email-template")
    context.driver.maximize_window()

@when('the user selects "{template}" from the template dropdown')
def step_select_template(context, template):
    dropdown = Select(context.driver.find_element(By.ID, "template-dropdown"))
    dropdown.select_by_visible_text(template)

@when('enters "{email}" in the email field')
def step_enter_email(context, email):
    email_field = context.driver.find_element(By.ID, "email-input")
    email_field.send_keys(email)

@when('enters "{subject}" in the subject field')
def step_enter_subject(context, subject):
    subject_field = context.driver.find_element(By.ID, "subject-input")
    subject_field.send_keys(subject)

@when('enters "{message}" in the message body')
def step_enter_message(context, message):
    message_field = context.driver.find_element(By.ID, "message-textarea")
    message_field.send_keys(message)

@when('clicks the "Send" button')
def step_click_send(context):
    send_button = context.driver.find_element(By.ID, "send-button")
    send_button.click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, "email-list"))
    )

@then('the email should be displayed in the sent list with "{email}" and "{subject}"')
def step_verify_email_sent(context, email, subject):
    email_list = context.driver.find_elements(By.CSS_SELECTOR, ".email-list-row")
    assert any(email in row.text and subject in row.text for row in email_list)

@when('clicks the "Cancel" button')
def step_click_cancel(context):
    cancel_button = context.driver.find_element(By.ID, "cancel-button")
    cancel_button.click()

@then('all input fields should be cleared')
def step_verify_fields_cleared(context):
    assert context.driver.find_element(By.ID, "email-input").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "subject-input").get_attribute("value") == ""
    assert context.driver.find_element(By.ID, "message-textarea").get_attribute("value") == ""

@then('the email should be visible with correct details')
def step_verify_email_in_list(context):
    email_list = context.driver.find_elements(By.CSS_SELECTOR, ".email-list-row")
    assert len(email_list) > 0

def after_scenario(context, scenario):
    context.driver.quit()
