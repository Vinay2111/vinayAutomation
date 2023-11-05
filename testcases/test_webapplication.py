import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap= dict(

    deviceName='Android',
    platformName='Android',
    browserName='Chrome'
)



driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cap)

driver.get("http://google.com")
print(driver.title)
driver.find_element(AppiumBy.XPATH,'//*[@name="q"]').send_keys("VInay kumar IAS")
time.sleep(10)

