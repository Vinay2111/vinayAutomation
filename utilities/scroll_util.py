from appium.webdriver.common.appiumby import AppiumBy


class ScrollUtil:
    @staticmethod
    def scrollToTextByUiAutomator(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,"new UiScrollable(new UiSelector().scrollable("
                                                         "true).instance(0)).scrollIntoView(new UiSelector("
                                                         ").textContains(\""+text+"\").instance(0))").click()
    @staticmethod
    def swipeUp(howManySwipes,driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(3287,990,287,293,2000)

    @staticmethod
    def swipeRight(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
             driver.swipe(287,293,287,990,2000)