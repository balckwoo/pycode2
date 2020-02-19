import time
from selenium import webdriver
driver = webdriver.Chrome()

url = 'E:/pycode2/SeleniumDemo/multiple.html'
driver.get(url)
driver.maximize_window()

# 点击
# driver.find_element_by_id('uid').click()
# # 输入文本
# driver.find_element_by_id('uid').send_keys('admin')
# # time.sleep(3)
# # 清空文本
# driver.find_element_by_id('uid').clear()
# 提交表单(建议使用click()方法，因为是万能的)
# driver.find_element_by_id('su').submit()
# 获取标签的文本值
# text_data = driver.find_element_by_id('button_id_1').text
# print(text_data)

# 获取标签的某个属性值
# ele_data = driver.find_element_by_id('uid').get_attribute('type')
# print('获取到标签的属性值是',ele_data)

# 查找你的标签中是否包含hidden属性
# 如果你的标签中含有hidden属性的话就会返回false
# result = driver.find_element_by_id('user_id').is_displayed()
# result2 = driver.find_element_by_id('uid').is_displayed()
# print(result,result2)

# 查找你的标签中是否包含disabled属性
# 如果你的标签中含有disabled属性的话就会返回false
# result = driver.find_element_by_id('role_id').is_enabled()
# result2 = driver.find_element_by_id('uid').is_enabled()
# print(result2,result)

# 查找你select标签中的选项能否被下拉
# 重点是你的下拉的标签必须要是selcet标签
result = driver.find_element_by_xpath('//*[@id="ShippingMethod"]/option[3]').is_selected()
print(result)











time.sleep(3)
driver.quit()