import time
from selenium import webdriver
# 实例化一个driver对象
# 实例化谷歌浏览器对象
driver = webdriver.Chrome()
url = 'E:/pycode2/SeleniumDemo/multiple.html'
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

# 警告框有三种类型
# 1.只有确定按钮
# 2.含有确定，取消按钮
# 3.带有文本值输入

# 点击一下按钮，才可以触发（警告框）js事件
driver.find_element_by_name('b1').click()
time.sleep(3)
# 获取文本值
# 带了画横线的意思是这个方法已经过时了
# data = driver.switch_to_alert().text
# 下面这个是新的方法
data = driver.switch_to.alert.text
print(data)
## 点击确认
# 老的方式
# driver.switch_to_alert().accept()

# 新的方式
# driver.switch_to.alert.accept()

# 点击取消
# 老的方式
# driver.switch_to_alert().dismiss()

# 新的方式
# driver.switch_to.alert.dismiss()

# 输入文本值
# 老的方式
# driver.switch_to_alert().send_keys('haha')
# driver.switch_to_alert().accept()

# 新的方式
time.sleep(3)
driver.switch_to.alert.send_keys('这是一个警告框的输入内容')
time.sleep(3)
driver.switch_to.alert.accept()

time.sleep(3)
driver.quit()