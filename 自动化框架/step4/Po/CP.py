import time
from selenium import webdriver

class CommmPageClass(object):


    def openUrl(self):
        url = 'http://localhost/admin.php?m=mgr/admin.login'
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(10)
        return driver