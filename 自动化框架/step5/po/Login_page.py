import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(object):
    # 对象层
    ipt_username_loc = (By.ID,'username')
    ipt_password_loc = (By.ID,'password')
    btn_login_loc = (By.XPATH,".//*[@id='loginFrm']/input")
    txt_success_msg_loc = (By.XPATH, ".//*[@id='header']/p/span[1]/strong")
    txt_username_error_msg_loc = (By.ID, "username_msg")
    txt_password_error_msg_loc = (By.ID, "password_msg")

    # 操作层
    def set_username(self,dv,username):

        dv.find_element(*self.ipt_username_loc).send_keys(username)

    def set_password(self, dv, password):
        dv.find_element(*self.ipt_password_loc).send_keys(password)

    def click_login_button(self, dv):
        dv.find_element(*self.btn_login_loc).click()

    def get_success_msg(self, dv):
        r = dv.find_element(*self.txt_success_msg_loc).text
        return r

    def get_username_error_msg(self, dv):
        WebDriverWait(self.dv, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_username_error_msg_loc, u"帐号或密码不能为空"))
        r = dv.find_element(*self.txt_username_error_msg_loc).text
        return r

    def get_password_error_msg(self, dv):
        WebDriverWait(dv, 10, 0.5).until(EC.text_to_be_present_in_element \
                                             (self.txt_password_error_msg_loc, \
                                              "密码错误"))
        r = dv.find_element(*self.txt_password_error_msg_loc).text
        return r

    # 业务层
    # 登录业务
    def optionLogin(self,dv,username,password):
        self.set_username(dv,username)
        self.set_password(dv,password)
        self.click_login_button(dv)

if __name__ == '__main__':
    obj = LoginPage()
    obj.login_operator('admin','admin')
    time.sleep(3)
    obj.close_broswer()
