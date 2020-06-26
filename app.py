from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys

website = sys.argv[1]

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')
driver.get(website)

driver.get_screenshot_as_file("/opt/screenshot.png")
driver.quit()
print("end...")
