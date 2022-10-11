from platform import platform
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
import time
import os

user_name = os.getenv("BROWSERSTACK_USERNAME")
access_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
browserstack_local = os.getenv("BROWSERSTACK_LOCAL")
build_name = os.getenv("BROWSERSTACK_BUILD_NAME")
browserstack_local_identifier = os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")
#app = os.getenv("BROWSERSTACK_APP_ID")
app = "SampleApp"

desired_cap = {
    # Set your access credentials
    "browserstack.local" : "true",
    "browserstack.localIdentifier" : browserstack_local_identifier,

    # Set URL of the application under test
    "app" : app,

    # Specify device and os_version for testing
    "platformName": "iOS",
    "deviceName" : "iPhone 13",
    "os_version" : "15",

    "autoDissmissAlerts" : "true",
    
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-ios",
    "name" : build_name,
    
}

print(app)
remote_addr = "https://"+user_name+":"+access_key+"@hub-cloud.browserstack.com/wd/hub"

driver = webdriver.Remote(remote_addr, desired_cap)

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

next_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'nextButton')))

for x in range(0, 3):
   next_button.click()

enable_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'enableButton')))

enable_button.click()

done_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'doneButton')))

done_button.click()

#log out
TouchAction(self.driver).tap(x=347, y=61).perform()

logout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'logOutButton')))

driver.quit()
