import time


class AddTeacherClass(object):

    def optionTeacher(self,driver):
        # 点击教师列表
        driver.find_element_by_link_text('教师列表').click()
        # 切入Iframe框操作教师列表里面的内容
        ele = driver.find_element_by_id('mainframe')
        driver.switch_to.frame(ele)
        # 添加教师
        driver.find_element_by_xpath('/html/body/div[2]/h3/a[2]/span').click()

    def sendTeacherData(self,driver):
        # 填写教师详情的信息
        driver.find_element_by_id('username').send_keys('13766666661')
        driver.find_element_by_id('realname').send_keys('我是你爸爸209')
        driver.find_element_by_id('password').send_keys('12345678')
        # 选择性别
        driver.find_element_by_xpath('//*[@id="form"]/div/div[4]/div/label[1]/input').click()
        # 下来选择角色
        from selenium.webdriver.support.ui import Select
        # 方式一选择角色
        select_role = driver.find_element_by_name('roleid')
        Select(select_role).select_by_value('7')
        # 方式二选择机构
        select_organ = driver.find_element_by_id('oneCategory')
        Select(select_role).select_by_index(1)
        # 选择邮箱
        driver.find_element_by_id('email').send_keys('aaa@163.com')
        # 选择手机
        driver.find_element_by_id('phone').send_keys('1378988777')
        # 下拉地址
        select_city = driver.find_element_by_name('location_p')
        Select(select_city).select_by_index(1)
        # 下拉区
        select_area1 = driver.find_element_by_name('location_c')
        Select(select_area1).select_by_index(1)
        select_area2 = driver.find_element_by_name('location_c')
        Select(select_area2).select_by_index(1)
        # 详细地址
        driver.find_element_by_id('address').click()
        driver.find_element_by_id('address').send_keys('你爸爸家')
        # 个人介绍
        driver.find_element_by_id('introduce').click()
        driver.find_element_by_id('introduce').send_keys('我是爸爸')
        # 确定保存
        driver.find_element_by_xpath('//*[@id="btn_sub"]/span').click()
        time.sleep(5)
        # 弹出确认成功框
        driver.switch_to.alert.accept()
        # 返回列表确认是否添加成功
        driver.find_element_by_xpath('/html/body/div[2]/h3/a/span').click()

    def verifyData(self, driver):
        # 校验
        result = driver.find_element_by_xpath('//*[@id="recordList"]/tr[1]/td[2]/div/a').text
        return result