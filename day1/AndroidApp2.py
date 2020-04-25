
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

gs.scroll(city,driver)

driver.find_element_by_xpath("//*[@text='"+city+"']").click()

gs.takeScreenshot(driver,"../demo.png")

activity =gs.getCurrentActivity(driver)
print("Current activity:",activity)


pkg =gs.getCurrentPagePkg(driver)
print("Current package:",pkg)

print(gs.getListOfSms())
print(gs.turnOffWifi())
