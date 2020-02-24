import time
from selenium import webdriver
# 用类把脚本包装起来
# 打开网址
class CommonPageClass(object):
    def openUrl(self):
        url = 'http://localhost/admin.php?m=mgr/admin.login'
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(10)
        time.sleep(3)
        return driver

if __name__ == '__main__':
    run = CommonPageClass()
    run.openUrl()

