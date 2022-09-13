from platform import platform
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os



# user_name = os.getenv("BROWSERSTACK_USERNAME")
# access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
# browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
# build_name = os.getenv("BROWSERSTACK_BUILD_NAME")
# browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")
# app = os.getenv("BROWSERSTACK_APP_ID")

# desired_cap = {
#     # Set your access credentials
#     "browserstack.user" : "semyonignatenko_stFnfH",
#     "browserstack.key" : "HDqFb91FxyR48zGcE9Gb",
#     # "browserstack.local" : "true",

#     # Set URL of the application under test
#     "app" : "bs://ee884312c12db9d98879dc154080a24d451c595b",

#     # Specify device and os_version for testing
#     "device" : "iPhone 13",
#     "os_version" : "15",

#     "autoDissmissAlerts" : "true",

#     # Set other BrowserStack capabilities
#     "project" : "First Python project", 
#     "build" : "browserstack-build-1",
#     "name" : "first_test"
# }

# user_name = "semyonignatenko_stFnfH"
# access_key = "HDqFb91FxyR48zGcE9Gb"
user_name = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
build_name = os.getenv("BROWSERSTACK_BUILD_NAME")
browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")
app = os.getenv("BROWSERSTACK_APP_ID")

desired_cap = {
    # Set your access credentials
    # "browserstack.user" : user_name,
    # "browserstack.key" : access_key,
    "browserstack.local" : browserstack_local,
    "browserstack.localIdentifier" : browserstack_local_identifier,

    # Set URL of the application under test
    "app" : app,

    # Specify device and os_version for testing
    "platformName": "iOS",
    "device" : "iPhone 13",
    "os_version" : "15",

    "autoDissmissAlerts" : "true",
    
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-2",
    "name" : build_name,
    
}

remote_addr = "https://"+user_name+":"+access_key+"@hub-cloud.browserstack.com/wd/hub"

print(remote_addr)

driver = webdriver.Remote(remote_addr, desired_cap)

# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
# driver = webdriver.Remote(
#     command_executor="http://hub-cloud.browserstack.com/wd/hub", 
#     desired_capabilities=desired_cap
# )

login_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.ID, "loginButton"))
)
login_button.click()
continue_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.ID, "Continue"))
)
continue_button.click()

username_input_xpath = '//*/XCUIElementTypeTextField'
password_input_xpath = '//*/XCUIElementTypeSecureTextField'

login_btn_id = 'LOG IN'

username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((MobileBy.XPATH, username_input_xpath))
)

password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((MobileBy.XPATH, password_input_xpath))
)
username.click()
username.send_keys("cucumber@theorchard.io")
password.send_keys("??33&suddenly&MILLION&least&51??")

login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, login_btn_id))
)

login_btn.click()


# # Test case for the BrowserStack sample Android app. 
# # If you have uploaded your app, update the test case here. 
# text_button = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Button"))
# )
# text_button.click()
# text_input = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Input"))
# )
# text_input.send_keys("hello@browserstack.com"+"\n")
# time.sleep(5)
# text_output = WebDriverWait(driver, 30).until(
#     EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Output"))
# )
# if text_output!=None and text_output.text=="hello@browserstack.com":
# 	assert True
# else:
# 	assert False

# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()