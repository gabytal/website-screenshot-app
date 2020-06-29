from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException, TimeoutException, InvalidArgumentException
import sys

try:
    website = sys.argv[1]
except IndexError:
    print("ooops, no website has entered, please provide a website URL")
    print ("exit program..")
    sys.exit(0)

if "https://" in website:
    pass
if "http://" in website:
    pass
else:
    print("invalid URL, please provide the right protocol before the URL, for example: https://google.com")
    print("Quiting program...")
    sys.exit(0)

options = Options()
options.headless = True
try:
    driver = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')
except WebDriverException as e:
    print("Cannot find gecodriver executable")
    sys.exit(0)

try :
    driver.get(website)
    print("URL successfully Accessed")
    pass
except InvalidArgumentException as e:
    print("Error, invalid URL has entered")
    print("Quiting program...")
    sys.exit(0)
except TimeoutException as e:
    print("Page load Timeout Occured. Quiting...")
    print("Quiting program...")


try:    
    driver.get_screenshot_as_file("/opt/screenshot.png")
    print("Screenshot has been saved successfully...")
    print ("end")
    driver.quit()

except Exception:
    print("Oops, error saving the screenshot")
    print("Quiting..")
    sys.exit(0)

