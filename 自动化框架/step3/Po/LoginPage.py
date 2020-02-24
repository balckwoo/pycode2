

class LoginPageClass(object):
    def login(self,driver):
        # 输入管理员后台账户及密码
        driver.find_element_by_id('username').send_keys('admin')
        driver.find_element_by_id('password').send_keys('admin')
        # 点击登录
        driver.find_element_by_xpath('//*[@id="loginFrm"]/input').click()
