from appium import webdriver
import time

from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.select import Select

desired_cap= dict(

    deviceName='Android',
    platformName='Android',
    browserName='Chrome'
)
'''to start the appium server didrectly'''
# appium_service=AppiumService()
# appium_service.start()

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)
driver.get("https://wikipedia.org")
print(driver.title)
dropdown=driver.find_element(AppiumBy.CSS_SELECTOR,'#searchLanguage')
select=Select(dropdown)
select.select_by_value("es")

options=driver.find_elements(AppiumBy.TAG_NAME,"option")
print(len(options))
for option in options:
    print("Text is:",option.text,", Lang is:",option.get_attribute('Lang'))
time.sleep(5)
'''to stop the server'''
# appium_service.stop()



