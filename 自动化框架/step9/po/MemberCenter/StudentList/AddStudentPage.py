# coding:utf-8
import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from po.Common_page import Page

class AddStudentPage(Page):
    """添加学生页面"""

    ##对象层##
    ipt_username_loc = (By.ID, 'username')
    ipt_realname_loc = (By.ID, 'realname')
    ipt_password_loc = (By.ID, 'password')
    radio_sex_loc = (By.XPATH, ".//*[@id='form']/div/div[4]/div")
    select_role_loc = (By.NAME, "roleid")
    ipt_start_student = (By.ID, "isstart")
    # 上传头像模块
    btn_upload_loc = (By.LINK_TEXT, u'上传头像')
    btn_local_loc = (By.XPATH, "html/body/div[3]/div[1]/div[2]/div/div[1]/ul/li[2]")
    btn_browse_parent_object_loc = (By.CLASS_NAME, "ke-upload-area")
    btn_browse_loc = (By.TAG_NAME, 'input')
    btn_confirm_loc = (By.XPATH, "html/body/div[3]/div[1]/div[3]/span[1]/input")

    select_category_loc = (By.ID, 'oneCategory')
    ipt_email_loc = (By.ID, 'email')
    ipt_phone_loc = (By.ID, 'phone')
    btn_save_loc = (By.ID, 'btn_sub')
    btn_comeback_loc = (By.CLASS_NAME, "btn-general")

    ##操作层##
    def set_username_input(self, value):
        '''输入用户名'''
        # WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(By.CLASS_NAME,'main-cont'))
        self.driver.find_element(*self.ipt_username_loc).send_keys(value)

    def set_realname_input(self, value):
        '''输入昵称'''
        self.driver.find_element(*self.ipt_realname_loc).send_keys(value)

    def set_password_input(self, value):
        '''输入登录密码'''
        self.driver.find_element(*self.ipt_password_loc).send_keys(value)

    def select_sex_radio(self, sex=0):
        '''选择性别'''
        rd = self.driver.find_element(*self.radio_sex_loc)
        sx = sex
        if sx == 1:
            rd.find_element_by_xpath('//input[@value="1"]').click()
        elif sx == 2:
            rd.find_element_by_xpath('//input[@value="2"]').click()
        elif sx == 0:
            rd.find_element_by_xpath('//input[@value="0"]').click()

    def select_role_select(self, text):
        '''选择角色'''
        s = self.driver.find_element(*self.select_role_loc)
        Select(s).select_by_visible_text(text)

    def select_start_student_input(self):
        '''选择明星学员'''
        self.driver.find_element(*self.ipt_start_student).click()

    def upload_head_portrait(self):
        '''上传头像操作'''
        self.driver.find_element(*self.btn_upload_loc).click()
        self.driver.find_element(*self.btn_local_loc).click()
        tpm = self.driver.find_element(*self.btn_browse_parent_object_loc)
        obj = tpm.find_elements(*self.btn_browse_loc)[1]
        ActionChains(self.driver).click(obj).perform()
        os.system("D:/share/ZM20190616/uploadFile.exe")
        self.driver.find_element(*self.btn_confirm_loc).click()

    def select_category_select(self, text):
        s = self.driver.find_element(*self.select_category_loc)
        Select(s).select_by_visible_text(text)

    def set_email_input(self, value):
        self.driver.find_element(*self.ipt_email_loc).send_keys(value)

    def set_phone_input(self, value):
        self.driver.find_element(*self.ipt_phone_loc).send_keys(value)

    def click_save_button(self):
        tmp = self.driver.find_element(*self.btn_save_loc)
        ele = WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(self.btn_save_loc))
        js = "window.scrollTo(0,10000)"
        self.driver.execute_script(js)
        time.sleep(2)
        ele.click()

    def click_alert_confirm_button(self):
        WebDriverWait(self.driver, 10, 0.5).until(EC.alert_is_present())
        self.driver.switch_to_alert().accept()

    def click_comeback_button(self):
        ele = self.driver.find_element(*self.btn_comeback_loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        ele.click()

    # 业务层
    def optionAddStudent(self,username,realname,password,sex,role,category,email,phone):
        self.set_username_input(username)
        self.set_realname_input(realname)
        self.set_password_input(password)
        self.select_sex_radio(sex)
        self.select_role_select(role)
        self.select_start_student_input()
        self.upload_head_portrait()
        self.select_category_select(category)
        self.set_email_input(email)
        self.set_phone_input(phone)
        self.click_save_button()
        self.click_alert_confirm_button()
        self.click_comeback_button()


if __name__ == '__main__':
    pass
