from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage(object):
    # 对象层
    username_loc = (By.NAME,'fadlkfjak')

    # 操作层（动作）、
    def sendUsername(self, driver):
        driver.find_element(*self.username_loc).send_keys('admin')

    def sendPwd(self, driver):
        driver.find_element_by_id('password').send_keys('admin')

    def clickLogin(self, driver):
        driver.find_element_by_xpath('//*[@id="loginFrm"]/input').click()

    # 业务层
    def optionLogin(self, driver):
        self.sendUsername(driver)
        self.sendPwd(driver)
        self.clickLogin(driver)