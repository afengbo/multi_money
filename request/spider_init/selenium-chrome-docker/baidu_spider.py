from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests


def test_chrome_server():
    while True:
        i = 0
        try:
            res = requests.get("http://chrome:4444/wd/hub/status", timeout=0.3)
        except Exception as e:
            i += 1
            if i > 10:
                raise
        else:
            print(res.status_code)
            break


test_chrome_server()

driver = webdriver.Remote(
    command_executor="http://chrome:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME
)

driver.get("http://www.baidu.com")
print(driver.title)
with open('/data/baidu.html', 'w') as f:
    f.write(driver.page_source)
driver.close()
