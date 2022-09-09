from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
  
desired_cap = {
    # Set your access credentials
    "browserstack.user" : "semyonignatenko_stFnfH",
    "browserstack.key" : "HDqFb91FxyR48zGcE9Gb",

    "browserstack.local" : "true",
  
    # Set URL of the application under test
    "app" : "bs://eff1ea8312ee007f737369783c9f34ce65817eab",
  
    # Specify device and os_version for testing
    "device" : "Google Pixel 3",
    "os_version" : "9.0",
      
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-1",
    "name" : "first_test"
}
  
# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
driver = webdriver.Remote(
    command_executor="http://hub-cloud.browserstack.com/wd/hub", 
    desired_capabilities=desired_cap
)
  
# If you have uploaded your app, write your test case here.
#'//*[@resource-id="loginButton"]'
login_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@resource-id='loginButton']"))
)
login_button.click()
# WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.CLASS_NAME, "android.widget.TextView"))
# ) 
  
# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()