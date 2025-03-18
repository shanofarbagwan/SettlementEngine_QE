from selenium import webdriver
from pages import searchpage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def before_all(context):
    gridUrl = context.config.userdata.get('gridUrl')
    browserName = context.config.userdata.get('browser')
    if(gridUrl!=""):
        context.browser = webdriver.Remote(
            command_executor=gridUrl, desired_capabilities={"browserName": browserName}
        )
        context.SearchPage = searchpage.searchPage(context.browser)
    else:
        isHeadless = context.config.userdata.get("headless")
        if(browserName == 'chrome'):
            chromeOptions = webdriver.ChromeOptions()
            if(isHeadless == "true"):
                chromeOptions.add_argument("--headless")
            context.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),chrome_options=chromeOptions)
        if(browserName == 'edge'):
            edgeOptions = webdriver.EdgeOptions()
            if(isHeadless == "true"):
                edgeOptions.add_argument("--headless")
            context.browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        if(browserName == 'firefox'):
            firefoxOptions = webdriver.FirefoxOptions()
            if(isHeadless == "true"):
                firefoxOptions.add_argument("--headless")
            context.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),firefox_options=firefoxOptions )

def after_all(context):
    context.browser.quit()