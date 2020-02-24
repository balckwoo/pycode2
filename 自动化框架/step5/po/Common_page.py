from selenium import webdriver

edu_url = 'http://localhost/admin.php?m=mgr/admin.login'


class Page(object):

    # 生成浏览器驱动
    def createDriver(self):
        driver = webdriver.Chrome()
        return driver

    # 打开浏览器
    def openUrl(self,driver,url=edu_url):
        driver.get(url)
        driver.implicitly_wait(10)

    # 关闭浏览器
    def closeBrowser(self,driver):
        driver.quit()

