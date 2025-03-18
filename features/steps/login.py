import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load the feature file
scenarios("login.feature")

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("URL_OF_THE_LOGIN_PAGE")  # Replace with actual URL
    yield driver
    driver.quit()

@given("the user is on the 'Login Window' screen")
def open_login_page(browser):
    assert "Login" in browser.title

@when("the user enters a valid smart card PIN")
def enter_valid_pin(browser):
    pin_input = browser.find_element(By.ID, "smart_card_pin")  # Replace with actual locator
    pin_input.send_keys("123456")  # Example valid PIN

@when("the user enters an invalid smart card PIN")
def enter_invalid_pin(browser):
    pin_input = browser.find_element(By.ID, "smart_card_pin")  # Replace with actual locator
    pin_input.send_keys("000000")  # Example invalid PIN

@when('the user clicks the "Continue" button')
def click_continue(browser):
    browser.find_element(By.ID, "continue_button").click()  # Replace with actual locator

@then("the user should be redirected to the dashboard")
def verify_dashboard_redirect(browser):
    assert "Dashboard" in browser.title  # Adjust based on expected title

@then("an error message should be displayed")
def verify_error_message(browser):
    error_message = browser.find_element(By.CLASS_NAME, "error-message").text  # Replace with actual locator
    assert "Invalid PIN" in error_message  # Adjust message as per UI

@when("the user clicks the visibility toggle button")
def click_visibility_toggle(browser):
    browser.find_element(By.CLASS_NAME, "visibility-toggle").click()  # Replace with actual locator

@then("the smart card PIN should be visible")
def verify_pin_visibility(browser):
    pin_input = browser.find_element(By.ID, "smart_card_pin")  # Replace with actual locator
    assert pin_input.get_attribute("type") == "text"

@then('the "BNP PARIBAS" logo should be visible')
def verify_logo(browser):
    logo = browser.find_element(By.CLASS_NAME, "logo")  # Replace with actual locator
    assert logo.is_displayed()

@then('the "PF UK Settlement Engine" title should be displayed')
def verify_title(browser):
    title = browser.find_element(By.TAG_NAME, "h1").text  # Replace with actual text locator
    assert "PF UK Settlement Engine" in title

@then("the smart card input field should be present")
def verify_smart_card_input(browser):
    input_field = browser.find_element(By.ID, "smart_card_pin")  # Replace with actual locator
    assert input_field.is_displayed()

@then('the "Continue" button should be enabled')
def verify_continue_button(browser):
    button = browser.find_element(By.ID, "continue_button")  # Replace with actual locator
    assert button.is_enabled()
