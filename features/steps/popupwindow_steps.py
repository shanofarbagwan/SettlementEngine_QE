import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load the feature file
scenarios("popup.feature")

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("URL_OF_THE_WEB_APPLICATION")  # Replace with the actual URL
    yield driver
    driver.quit()

@given("the user is on the 'Add User Information' popup")
def open_add_user_popup(browser):
    browser.find_element(By.ID, "add_user_popup").click()  # Replace with actual locator

@when('the user selects "James George" from the "User Name" dropdown')
def select_user(browser):
    dropdown = browser.find_element(By.ID, "user_name")  # Replace with actual locator
    dropdown.click()
    option = browser.find_element(By.XPATH, "//option[text()='James George']")
    option.click()

@when('the user enters "james.george@bnpparibas-pf.co.uk" in the "Email" field')
def enter_email(browser):
    email_field = browser.find_element(By.ID, "email")  # Replace with actual locator
    email_field.send_keys("james.george@bnpparibas-pf.co.uk")

@when('the user clicks the "Save" button')
def click_save(browser):
    browser.find_element(By.ID, "save_button").click()  # Replace with actual locator

@then("the user information should be saved successfully")
def verify_save_success(browser):
    success_message = browser.find_element(By.CLASS_NAME, "success-message").text
    assert "User information saved successfully" in success_message

@when('the user clicks the "Cancel" button')
def click_cancel(browser):
    browser.find_element(By.ID, "cancel_button").click()  # Replace with actual locator

@then("the popup should close without saving")
def verify_popup_closed(browser):
    assert not browser.find_element(By.ID, "add_user_popup").is_displayed()

@given("the user performs an update action")
def perform_update(browser):
    browser.find_element(By.ID, "update_button").click()  # Replace with actual locator

@then('a confirmation popup should appear with the text "Are you sure you want to update this activity?"')
def verify_update_popup(browser):
    popup_text = browser.find_element(By.CLASS_NAME, "popup-message").text
    assert "Are you sure you want to update this activity?" in popup_text

@given("the user deletes an activity")
def delete_activity(browser):
    browser.find_element(By.ID, "delete_button").click()  # Replace with actual locator

@then('a confirmation popup should appear with the text "Activity deleted successfully!"')
def verify_delete_popup(browser):
    popup_text = browser.find_element(By.CLASS_NAME, "popup-message").text
    assert "Activity deleted successfully!" in popup_text

@given("a popup is displayed")
def popup_displayed(browser):
    assert browser.find_element(By.CLASS_NAME, "popup").is_displayed()

@when("the user clicks the close (X) button")
def close_popup(browser):
    browser.find_element(By.CLASS_NAME, "close-button").click()  # Replace with actual locator

@then("the popup should close")
def verify_popup_closed(browser):
    assert not browser.find_element(By.CLASS_NAME, "popup").is_displayed()

