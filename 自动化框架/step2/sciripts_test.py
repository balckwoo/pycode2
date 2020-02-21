import time
from selenium import webdriver
# 第二步用函数把脚本包装起来
# 打开网址
def openUrl():
    url = 'http://localhost/admin.php?m=mgr/admin.login'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    return driver

def login(driver):
    # 输入管理员后台账户及密码
    driver.find_element_by_id('username').send_keys('admin')
    driver.find_element_by_id('password').send_keys('admin')
    # 点击登录
    driver.find_element_by_xpath('//*[@id="loginFrm"]/input').click()

def memberCenter(driver):
    # 点击会员中心
    driver.find_element_by_link_text('会员中心').click()
def optionTeacher(driver):
    # 点击教室列表
    driver.find_element_by_xpath('//*[@id="side-menu"]/div[3]/ul/li[2]/a').click()
    # 切入Iframe框操作教室列表里面的内容

    time.sleep(5)
    ele = driver.find_element_by_id('mainframe')
    driver.switch_to.frame(ele)

def addTeacher(driver):
    # 添加教师
    driver.find_element_by_xpath("//*[text()='添加教师']").click()
    # driver.find_element_by_xpath('/html/body/div[2]/h3/a[2]/span').click()
    # 输入用户账号
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('18797766767')
    # 输入昵称
    driver.find_element_by_xpath('//*[@id="realname"]').send_keys('baba')
    # 输入密码
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('wo1234567')
    # 选择性别
    driver.find_element_by_xpath('//*[@id="form"]/div/div[4]/div/label[2]/input').click()
    # 选择角色，导入下拉菜单所需要的库
    from selenium.webdriver.support.ui import Select
    ele = driver.find_element_by_xpath('//*[@id="form"]/div/div[5]/div/select')
    Select(ele).select_by_value('8')
    # 选择机构
    ele2 = driver.find_element_by_xpath('//*[@id="oneCategory"]')
    Select(ele2).select_by_value('110')
    # 输入邮箱
    driver.find_element_by_xpath('//*[@id="email"]').send_keys('123@163.com')
    # 输入手机号
    driver.find_element_by_xpath('//*[@id="phone"]').send_keys('18797766767')
    # 选择城市
    city = driver.find_element_by_xpath('//*[@id="form"]/div/div[9]/div/select[1]')
    Select(city).select_by_value('天津市')
    # 选择地区1
    area1 = driver.find_element_by_xpath('//*[@id="form"]/div/div[9]/div/select[2]')
    Select(area1).select_by_value('市辖区')
    # 选择地区2
    area2 = driver.find_element_by_xpath('//*[@id="form"]/div/div[9]/div/select[3]')
    Select(area2).select_by_value('和平区')
    # 输入详细地址
    driver.find_element_by_xpath('//*[@id="address"]').send_keys('myhouse')
    # 输入个人简介
    driver.find_element_by_xpath('//*[@id="introduce"]').send_keys('tianzhenkeai')
    # 点击保存确定按钮
    driver.find_element_by_xpath('//*[@id="btn_sub"]/span').click()
    time.sleep(3)
    # 点击弹出框确定按钮
    driver.switch_to.alert.accept()
    time.sleep(3)
    # 点击返回列表确认是否添加成功
    driver.find_element_by_xpath('/html/body/div[2]/h3/a/span').click()
def verifyData(driver):
    # 校验
    result = driver.find_element_by_xpath('//*[@id="recordList"]/tr[1]/td[2]/div/a').text
    return result







