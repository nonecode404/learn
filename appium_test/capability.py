from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps ={
  "platformName": "Android",
  "platformVersion": "8.0.0",
  "deviceName": "BNU5T17410011889",
  "udid": "BNU5T17410011889",
  "appPackage": "com.tal.kaoyan",
  "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
  "noReset": "True"
}
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(7)
