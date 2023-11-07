import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap={
  "appium:deviceName": "Android Emulator",
  "platformName": "Android",
  "appium:appPackage": "com.eezy.ai.dev",
  "appium:appWaitActivity": "com.natife.eezy.MainActivity",
  "appium:app": "/Users/vinay/Documents/appium/Android APK/app-dev-debug.apk",
  "appium:noReset": True
}

driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(20)

#first_popup=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/negativeButton').click()
login_btn=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/wizardLoginTextView').click()
country_selector=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/selectedCountry').click()
time.sleep(5)
country_selector1=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/spinner').click()
time.sleep(3)
type_country=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/search').click()
type_country1=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/search').send_keys("india")
time.sleep(3)
select_india=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/countryName').click()
time.sleep(2)
send_phone_nr=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/phoneNumber').send_keys("9972704324")
go_btn=driver.find_element(AppiumBy.ID,'com.eezy.ai.dev:id/iv_next').click()

'''now we need to switch to the native messaging app and the read the received OTP
for this we need to use 'driver.start_activity'''

#driver.start_activity()('com.android.mms', '.ui.ConversationList')

#to select the 1st message conversation in message app
#driver.find_elements(AppiumBy.ID,'com.android.mms:id/subject')[0].click()

# since the ID is same for all the message inside a conversation
#messages = driver.find_elements(AppiumBy.ID,'com.android.mms:id/text_view')
#text = messages[len(messages) - 1].text
#print(text[83:89]) # here we need to calculate the char count from where we get actual OTP



