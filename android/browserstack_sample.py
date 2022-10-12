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
app = "SampleAppAndroid"

desired_cap = {
    # Set your access credentials
    "browserstack.local" : "true",
    "browserstack.localIdentifier" : browserstack_local_identifier,

    # Set URL of the application under test
    "app" : app,

    # Specify device and os_version for testing
    "platformName" : "Android",
    "deviceName" : "Google Pixel 5",
    "platformVersion" : "12.0",
    
    # Set other BrowserStack capabilities
    "project" : "Android Test Project", 
    "build" : "browserstack-build-android",
    "name" : build_name,
    
}
  
# Initialize the remote Webdriver using BrowserStack remote URL
# and desired capabilities defined above
remote_addr = "https://"+user_name+":"+access_key+"@hub-cloud.browserstack.com/wd/hub"
driver = webdriver.Remote(remote_addr, desired_cap)

  
# If you have uploaded your app, write your test case here.
login_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@resource-id='loginButton']"))
)
login_button.click()

username_input = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@resource-id='username']")))

password_input = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@resource-id='password']")))

username_input.send_keys("cucumber@theorchard.io")
password_input.send_keys("??33&suddenly&MILLION&least&51??")

log_in_btn = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//android.widget.Button[@text=\"LOG IN\"]")))

log_in_btn.click()

next_btn = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@resource-id=\"nextButton\"]")))

for x in range(0, 3):
   next_btn.click()

lets_go_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.XPATH, '//*[@text="LET\'S GO!"]')))

lets_go_button.click()

catalog_tab =  WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@content-desc=\"MyCatalogStack, tab, 1 of 3\"]")))

catalog_tab.click()

assert WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.XPATH, '//*[contains(@resource-id, "topTracksItem")]')))

#log out
TouchAction(driver).tap(x=963, y=174).perform()

log_out_btn = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((MobileBy.XPATH, "//*[@resource-id=\"logOutButton\"]")))

log_out_btn.click()

# search_results = driver.find_elements(MobileBy.XPATH("//*[@resource-id='loginButton']"))
# find_elements_by_class_name
search_results = driver.find_elements_by_xpath("//*[@resource-id='loginButton']")
if (len(search_results) > 0):
	driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Results found!"}}')
else:
	driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "No results found"}}')
  
# Invoke driver.quit() after the test is done to indicate that the test is completed.
driver.quit()
