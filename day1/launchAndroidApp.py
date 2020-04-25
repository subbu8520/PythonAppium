from appium import webdriver

desired_caps = {
    "platformName": "Android",
    'platformVersion':'10',
    "deviceName": "motorola one power",
    "udid":"ZF62245RHC",
    "appPackage": 'com.motorola.ts.camera',
    'appActivity': 'com.android.camera.CameraLauncher',
    'autoGrantPermissions': True
    # "app": "/Users/aravindanathdm/PycharmProjects/AppiumAutomation/apks/General_Store.apk"
}

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub",desired_caps)



