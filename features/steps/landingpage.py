import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load the feature file
scenarios("landing_page.feature")

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.get("URL_OF_LANDING_PAGE")  # Replace with actual URL
    yield driver
    driver.quit()

@given('the user is logged in as "Admin"')
def user_logged_in(browser):
    assert browser.find_element(By.CLASS_NAME, "user-profile").text == "John doe"

@given('the user is on the "Landing Page"')
@when('the user navigates to the "Landing Page"')
def open_landing_page(browser):
    assert "Landing Page" in browser.title

@then('the "PF UK Settlement Engine" heading should be displayed')
def verify_heading(browser):
    heading = browser.find_element(By.TAG_NAME, "h1").text
    assert "PF UK Settlement Engine" in heading

@then("the BNP PARIBAS logo should be visible")
def verify_logo(browser):
    logo = browser.find_element(By.CLASS_NAME, "logo")  # Replace with actual locator
    assert logo.is_displayed()

@then("the user's profile should be displayed")
def verify_user_profile(browser):
    profile = browser.find_element(By.CLASS_NAME, "user-profile")  # Replace with actual locator
    assert profile.is_displayed()

@then('the "Payment" section should be visible')
@then('the "Exceptions" section should be visible')
@then('the "Reference Look Up" section should be visible')
@then('the "Metadata" section should be visible')
def verify_sections(browser, section_name):
    section = browser.find_element(By.XPATH, f"//div[contains(text(), '{section_name}')]")  # Adjust locator
    assert section.is_displayed()

@when('the user clicks the "{section_name}" section')
def click_section(browser, section_name):
    section = browser.find_element(By.XPATH, f"//div[contains(text(), '{section_name}')]")  # Adjust locator
    section.click()

@then('the user should be navigated to the "{section_name}" page')
def verify_navigation(browser, section_name):
    assert section_name in browser.title
