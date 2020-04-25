
import time
from appium import webdriver
from day1 import Generics as gs
desired_caps = {
    "platformName": "Android",
    'platformVersion':'10',
    "deviceName": "motorola one power",
    "udid":"ZF62245RHC",
    # "appPackage": 'com.motorola.ts.camera',
    # 'appActivity': 'com.android.camera.CameraLauncher',
    'autoGrantPermissions': True,
     "app": "/Users/aravindanathdm/PycharmProjects/AppiumAutomation/apks/GeneralStore.apk"
}


driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub",desired_caps)

driver.implicitly_wait(30)


driver.find_element_by_id("spinnerCountry").click()

city ="Brazil"
automatorString = 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().textContains("'+city+'"));'
driver.find_elements_by_android_uiautomator(automatorString)


driver.find_element_by_xpath("//*[@text='"+city+"']").click()


