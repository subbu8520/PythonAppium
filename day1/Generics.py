import subprocess

from appium.webdriver.common.touch_action import TouchAction


def local_cmd(cmd):
    return subprocess.getoutput(cmd)

def adb_cmd(cmd):
    return local_cmd('adb'+cmd)

def adb_shell_cmd(cmd):
    return adb_cmd('shell'+cmd)


def scroll(text,driver):
    automatorString = 'new UiScrollable(new UiSelector()).scrollIntoView(new UiSelector().textContains("' + text + '"));'
    driver.find_elements_by_android_uiautomator(automatorString)
    return driver


def takeScreenshot(driver,path):
    driver.save_screenshot(path)
    return driver


def tap(driver,element):
    actions = TouchAction(driver)
    actions.tap(element)
    actions.perform()
    return driver

def startApp(driver,activity,package):
    driver.start_activity(package, activity);
    return driver

def getCurrentActivity(driver):
    activity =  driver.current_activity;
    return activity


def getCurrentPagePkg(driver):
    package = driver.current_package;
    return package


def longPress(driver,element):
    actions = TouchAction(driver)
    actions.long_press(element)
    actions.perform()
    return driver

def scrollDown(driver):
    driver.execute_script("mobile: scroll", {'direction': 'down'})

def scrollUp(driver):
    driver.execute_script("mobile: scroll", {'direction': 'up'})

def acceptAlert(driver,text):
    driver.execute_script('mobile: alert', {'action': 'accept', 'buttonLabel': text});

def getBatteryInfo(driver):
        info =driver.execute_script('mobile: batteryInfo');
        return info


def getListOfSms():
    return subprocess.getoutput("adb shell am broadcast -a io.appium.settings.sms.read --es max 10")


def turnOffWifi():
    return subprocess.getoutput("adb shell am broadcast -a io.appium.settings.wifi --es setstatus disable")


def turnOnWifi():
    return subprocess.getoutput("adb shell am broadcast -a io.appium.settings.wifi --es setstatus enable")


def turnOffData():
    return subprocess.getoutput("adb shell am broadcast -a io.appium.settings.data_connection --es setstatus disable")


def turnOnData():
    return subprocess.getoutput("adb shell am broadcast -a io.appium.settings.data_connection --es setstatus enable")


def restUSB():
    return subprocess.getoutput("adb usb")






