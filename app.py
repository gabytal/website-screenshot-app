    #import required modules
try:
    import time 
    import os.path
    import sys
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    from selenium.common.exceptions import WebDriverException, TimeoutException, InvalidArgumentException
except ModuleNotFoundError:
    print("Importing required modules faild. please install selenium with pip")
    sys.exit(1)

    #assign user argument as variable
try:
    website = sys.argv[1]
except IndexError:
    print("ooops, no website has entered, please provide a website URL")
    print ("exit program..")
    sys.exit(1)

   #check if the url scheme has provided
if "https://" in website:
    pass
elif "http://" in website:
    pass
else:
    print("invalid URL has entered, please check protocol scheme, for example: https://google.com")
    print("Quiting program...")
    sys.exit(1)

#create an instance from Selenium Options class 
options = Options()
#set the headless parameter
options.headless = True
    
#create an instance from Selenium Firefox class and configure the options and the geckodriver executable
try:
    driver = webdriver.Firefox(options=options, executable_path='/usr/local/bin/geckodriver')
except WebDriverException as e:
    print("Error with gecodriver")
    print("Quiting...")
    sys.exit(1)
except PermissionError as e:
    print("Driver permission Error! have you used the right permissions?")

driver.set_page_load_timeout(50)

#load the website
try :
    driver.get(website)
    time.sleep(15)
    print("URL successfully Accessed")
    pass
except InvalidArgumentException as e:
    print("Error, invalid URL has entered")
    print("Quiting program...")
    sys.exit(1)
except TimeoutException as e:
    print("Page load Timeout Occured. Quiting...")
    print("Quiting program...")
    sys.exit(1)
except WebDriverException as e:
    print("Connection problem, please check your internet connection or the URL that has been provided")
    print("Quiting program...")
    sys.exit(0)
 
#save a screenshot of the website
try:    
    driver.get_screenshot_as_file("/opt/screenshot.png")
    if os.path.exists("/opt/screenshot.png"):
        print("Screenshot has been saved successfully...")
        print ("end")
        driver.quit()
    else:
        print("Screenshot has not been saved. do you have the right permissions?")

except Exception:
    print("Oops, error saving the screenshot")
    print("Quiting..")
    sys.exit(1) 

