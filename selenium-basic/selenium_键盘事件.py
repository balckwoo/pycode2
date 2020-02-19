import time
from selenium import webdriver
driver = webdriver.Chrome()

url = 'E:/pycode2/SeleniumDemo/multiple.html'
driver.get(url)
# 全局等待10秒
driver.implicitly_wait(10)

driver.maximize_window()
# 导入一个键盘库
from selenium.webdriver.common.keys import Keys
driver.find_element_by_id('uid').click()
driver.find_element_by_id('uid').send_keys('administrator')
time.sleep(3)

# driver.find_element_by_id('kw').click()
#
# # send_keys 它并不是我们用户方式在键盘输入文本值
# driver.find_element_by_id('kw').send_keys('自动化测试')

# 删除键（BackSpace)
# driver.find_element_by_id('uid').send_keys(Keys.BACK_SPACE)
# 删除五次，使用循环方式处理
# for i in range(1,6):
#     driver.find_element_by_id('uid').send_keys(Keys.BACK_SPACE)

# 空格事件
driver.find_element_by_id('uid').send_keys(Keys.SPACE)

time.sleep(3)








driver.quit()












time.sleep(3)
driver.quit()