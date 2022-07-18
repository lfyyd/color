from appium import webdriver

info = {
    "platformName": "Android",
    "platformVersion": "11",
    "deviceName": "xxx",
    "appPackage": "tv.danmaku.bili",
    "appActivity": "tv.danmaku.bili.MainActivityV2",
    "noRest": True
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', info)
