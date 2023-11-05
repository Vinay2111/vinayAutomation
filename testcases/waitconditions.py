from appium import webdriver
import time


from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

desired_cap={
  "appium:deviceName": "6a45d0657d05",
  "platformName": "Android",
  "appium:appPackage": "com.eezy.ai.dev",
  "appium:appWaitActivity": "com.natife.eezy.MainActivity",
  "appium:app": "/Users/vinay/Documents/appium/Android APK/app-dev-debug.apk"
}
# time.sleep(7)
driver= webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
#if we need to handle a condition where a button will be visible or clicable only after some time
wait=WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable(AppiumBy.ID,''))
driver.press_keycode()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, )

wait.until(EC.element_to_be_clickable())
a=driver.get_window_rect()

