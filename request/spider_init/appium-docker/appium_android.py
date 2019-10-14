import time
import requests
from appium import webdriver

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "8.0.0"
desired_caps["deviceName"] = "Honor V10"

desired_caps["appPackage"] = "com.ted.android"
desired_caps["appActivity"] = ".view.splash.SplashActivity"


def test_chrome_server():
    while True:
        i = 0
        try:
            res = requests.get("http://appium:4723/wd/hub/status", timeout=0.3)
        except Exception as e:
            i += 1
            if i > 10:
                raise
        else:
            print(res.status_code)
            break


test_chrome_server()

print("尝试连接")
driver = webdriver.Remote(
    command_executor="http://appium:4723/wd/hub",
    desired_capabilities=desired_caps
)
print("连接成功")
time.sleep(3)
driver.find_element_by_android_uiautomator('text(\"热门\")').click()
driver.quit()
