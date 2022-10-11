from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

user_name = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
build_name = os.getenv("BROWSERSTACK_BUILD_NAME")
browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")
#app = os.getenv("BROWSERSTACK_APP_ID")
app = "SampleAppAndroid"

desired_cap = {
    # Set your access credentials
    "browserstack.local" : "true",
    "browserstack.localIdentifier" : browserstack_local_identifier,

    # Set URL of the application under test
    "app" : app,

    # Specify device and os_version for testing
    "platformName" : "android",
    "device" : "Google Pixel 3",
    "os_version" : "9.0",
    
    # Set other BrowserStack capabilities
    "project" : "Android Test Project", 
    "build" : "browserstack-build-1",
    "name" : build_name,
    
}
  
# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
remote_addr = "https://"+user_name+":"+access_key+"@hub-cloud.browserstack.com/wd/hub"
driver = webdriver.Remote(remote_addr, desired_cap)

  
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