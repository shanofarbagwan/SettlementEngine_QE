import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from behave import given, when, then
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(
    filename='test_report.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

options = Options()
options.headless = False

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Optional: Run in headless mode
    return webdriver.Chrome(options=options)

# You can add more detailed logging to each step
@given("I open the SauceDemo login page")
def open_login_page(context):
    logging.info("Opening SauceDemo login page...")
    context.driver.get("https://www.saucedemo.com/v1/index.html")
    sleep(2)  # Wait for page to load
    logging.info("SauceDemo login page opened successfully.")

@when("I enter valid username and password")
def enter_valid_credentials(context):
    logging.info("Entering valid username and password...")
    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    logging.info("Entered valid credentials.")

@when("I enter invalid username and password")
def enter_invalid_credentials(context):
    logging.info("Entering invalid username and password...")
    context.driver.find_element(By.ID, "user-name").send_keys("invalid_user")
    context.driver.find_element(By.ID, "password").send_keys("wrong_password")
    logging.info("Entered invalid credentials.")

@when("I click the login button")
def click_login_button(context):
    logging.info("Clicking the login button...")
    context.driver.find_element(By.ID, "login-button").click()
    sleep(2)  # Wait for page transition
    logging.info("Login button clicked.")

@then("I should be redirected to the inventory page")
def verify_successful_login(context):
    logging.info("Verifying if the user is redirected to the inventory page...")
    assert "inventory.html" in context.driver.current_url
    logging.info("Successfully redirected to the inventory page.")
    context.driver.quit()

@then("I should see an error message")
def verify_error_message(context):
    logging.info("Verifying error message after failed login...")
    error_message = context.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Epic sadface" in error_message
    logging.info("Error message displayed: " + error_message)
    context.driver.quit()
