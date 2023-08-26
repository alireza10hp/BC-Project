from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the Selenium WebDriver
driver = webdriver.Chrome('./chromedriver')

# Navigate to the target webpage
driver.get("https://www.google.com")

# Press F12 to open the Developer Tools window
body = driver.find_element_by_tag_name('body')
body.send_keys(Keys.F12)

# Wait for the Developer Tools window to open
time.sleep(2)

# Switch the focus of the WebDriver to the Developer Tools window
driver.switch_to.window(driver.window_handles[-1])

# You can now use the WebDriver to interact with the Developer Tools window,
# such as inspecting elements and running JavaScript code.

# Quit the WebDriver instance
driver.quit()
