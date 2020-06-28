from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, InvalidArgumentException
import sys

try:
    website = sys.argv[1]
except IndexError:
    print("ooops, no website has entered, please insert a website URL")
    print ("exit program..")
    sys.exit(0)

if "https://" or "http://" in website:
    pass
else:
    website = "https://"+website

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')

try :
    driver.get(website)
    print("URL successfully Accessed")
    pass
except InvalidArgumentException as e:
    print('invalid URL, please provide the right protocol before the URL, for example: "https://google.com"')
    sys.exit(0)
except TimeoutException as e:
    print("Page load Timeout Occured. Quiting...")
    driver.quit()



driver.get_screenshot_as_file("/opt/screenshot.png")
driver.quit()
print("end...")
