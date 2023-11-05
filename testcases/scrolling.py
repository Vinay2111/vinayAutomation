import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

desired_cap= {
    "appium:deviceName": "6a45d0657d05",
    "platformName": "Android",
    "appium:appPackage": "com.eezy.ai.dev",
    "appium:appWaitActivity": "com.natife.eezy.MainActivity",
    "appium:app": "/Users/vinay/Documents/appium/Android APK/app-dev-debug.apk"
}

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)

nope_btn=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/negativeButton').click()
get_started_btn=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/wizardBottomButton').click()
more_sign_in=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/moreLoginOptions').click()
email_sign_up=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/emailSignUp').click()
driver.implicitly_wait(5)

login_btn=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/signUpAlreadyHaveAccountTextView').click()
login_clickMore=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/moreLoginOptions').click()
login_email_btn=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/emailSignUp').click()
driver.implicitly_wait(4)
login_email_id=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/loginEmailEditText').send_keys("qwerty1@ymail.com")
login_password=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/loginPasswordEditText').send_keys('111111')
driver.implicitly_wait(3)
login_continue_btn=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/loginNowButton').click()

driver.implicitly_wait(200)


friends_bottom_btn=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/friendsFragment').click()
driver.implicitly_wait(15)
'''will we using UIselector and UIscrollable class'''

#touch=TouchAction(driver)
# driver.implicitly_wait(10)
# for i in range(2):
#     touch.press(x=357,y=920).move_to(x=353,y=367).release().perform()
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Phase335").instance(0))').click()
