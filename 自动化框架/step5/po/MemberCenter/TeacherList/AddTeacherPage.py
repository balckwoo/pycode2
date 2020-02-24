import os
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from po.Common_page import Page

class AddTeacherPage(object):
    # 添加教师控件
    click_teacher_button = (By.XPATH, '/html/body/div[2]/h3/a[2]/span')
    # 账号
    ipt_username_loc = (By.ID, 'username')
    # 真实姓名
    ipt_realname_loc = (By.ID, 'realname')
    # 密码
    ipt_password_loc = (By.ID, 'password')
    # 男性别
    select_sex_loc = (By.XPATH, '//*[@id="form"]/div/div[4]/div/label[1]/input')
    # 选择角色
    select_role_loc = (By.NAME, 'roleid')
    # 输入机构
    select_organ = (By.ID, 'oneCategory')
    # 输入邮箱
    ipt_email_loc = (By.ID, 'email')
    # 输入手机
    ipt_phone_loc = (By.ID, 'phone')
    # 选择地址
    select_city_loc = (By.NAME, 'location_p')
    # 选择地区
    select_area_loc = (By.NAME, 'location_c')
    select_area2_loc = (By.NAME, 'location_a')
    # 输入详细地址
    ipt_address_loc = (By.ID, 'address')
    # 输入个人介绍
    ipt_introduce_loc = (By.ID, 'introduce')
    # 保存数据
    ipt_save_loc = (By.XPATH, '//*[@id="btn_sub"]/span')
    # 返回列表
    ipt_return_loc = (By.XPATH, '/html/body/div[2]/h3/a/span')
    # 校验教师列表文本
    check_teacher_list = (By.XPATH, '//*[@id="recordList"]/tr[1]/td[2]/div/a')

    # 操作层
    # 点击添加教师项
    def clickTeacher(self, dv):
        dv.find_element(*self.click_teacher_button).click()

    # 输入账号
    def sendUserName(self, dv, value):
        dv.find_element(*self.ipt_username_loc).send_keys(value)

    def sendRealName(self, dv, value):
        dv.find_element(*self.ipt_realname_loc).send_keys(value)

    # 输入密码
    def sendPassword(self, dv, value):
        '''输入登录密码'''
        dv.find_element(*self.ipt_password_loc).send_keys(value)

    # 选择男性别
    def selectSex(self, dv):
        dv.find_element(*self.select_sex_loc).click()

    # 选择角色
    def selectRole(self, dv):
        ele = dv.find_element(*self.select_role_loc)
        Select(ele).select_by_value('7')

    # 选择机构
    def selectOragnt(self, dv):
        ele = dv.find_element(*self.select_organ)
        Select(ele).select_by_index(1)

    # 输入邮箱
    def sendEmail(self, dv, value):
        dv.find_element(*self.ipt_email_loc).send_keys(value)

    # 输入手机
    def sendPhone(self, dv, value):
        dv.find_element(*self.ipt_phone_loc).send_keys(value)

    # 选择所在地区
    def selectCity(self, dv):
        # 方式一选择角色
        ele = dv.find_element(*self.select_city_loc)
        ele2 = dv.find_element(*self.select_area_loc)
        ele3 = dv.find_element(*self.select_area2_loc)
        Select(ele).select_by_index(1)
        Select(ele2).select_by_index(1)
        Select(ele3).select_by_index(1)

    # 输入详细地址
    def sendAddress(self, dv, value):
        dv.find_element(*self.ipt_address_loc).send_keys(value)

    # 输入自我介绍
    def sendIntroduce(self, dv, value):
        dv.find_element(*self.ipt_introduce_loc).send_keys(value)

    # 保存信息返回列表
    def saveTeacher(self, dv):
        dv.find_element(*self.ipt_save_loc).click()
        time.sleep(5)
        # 确定弹出警告框
        dv.switch_to.alert.accept()
        dv.find_element(*self.ipt_return_loc).click()

    def verifyData(self, dv):
        result = dv.find_element(*self.check_teacher_list).text
        return result

    # 业务层
    def optionAddTeacher(self, dv, username, realname, pwd, email, phone, address, introduce):
        # 点击添加教师
        self.clickTeacher(dv)
        ## 输入一堆信息
        self.sendUserName(dv, username)
        self.sendRealName(dv, realname)
        self.sendPassword(dv, pwd)
        self.selectSex(dv)
        self.selectRole(dv)
        self.selectOragnt(dv)
        self.sendEmail(dv, email)
        self.sendPhone(dv, phone)
        self.selectCity(dv)
        self.sendAddress(dv, address)
        self.sendIntroduce(dv, introduce)

    def optionVerifyData(self, dv):
        self.saveTeacher(dv)
        result = self.verifyData(dv)
        return result

if __name__ == '__main__':
    ...
