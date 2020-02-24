from selenium import webdriver

from config.secret import test_edu_url


class Page(object):

    # 生成浏览器驱动
    def __init__(self,driver=''):
        if driver == '':
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver


    # 打开浏览器
    def openUrl(self,url=test_edu_url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    # 关闭浏览器
    def closeBrowser(self):
        self.driver.quit()
