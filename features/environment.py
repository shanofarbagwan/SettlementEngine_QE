from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# This function will run before all scenarios
def before_scenario(context, scenario):
    options = Options()
    options.headless = False  # Set to True to run in headless mode
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# This function will run after all scenarios
def after_scenario(context, scenario):
    context.driver.quit()
