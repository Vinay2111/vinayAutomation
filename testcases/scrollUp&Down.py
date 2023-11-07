from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from pytestFramework.utilities.scroll_util import ScrollUtil

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


ScrollUtil.scrollToTextByUiAutomator("Chiggers",driver)
'''driver.swipe(287,990,287,293,2000)
driver.swipe(287,990,287,293,2000)
driver.swipe(287,990,287,293,2000)
driver.swipe(287,990,287,293,2000)

driver.swipe(287,293,287,990,2000)
driver.swipe(287,293,287,990,2000)
driver.swipe(287,293,287,990,2000)'''
