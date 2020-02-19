import time
from selenium import webdriver
# 实例化一个driver对象
# 实例化谷歌浏览器对象
driver = webdriver.Chrome()
url = 'E:/pycode2/SeleniumDemo/multiple.html'
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()
# iframe(表单)标签就是在也你按嵌套页面
# iframe标签外面会有1对html标签，里面也有1对html标签

# 定位iframe标签
ele = driver.find_element_by_id('if')

# 切换iframe 标签内
# # 老的方式切换表单
# # driver.switch_to_frame(ele)

# 新的
# ele是需要定位到的iframe标签
driver.switch_to.frame(ele)
driver.find_element_by_id('kw').send_keys('zidonghuaceshi')
# # 老的切换回原本页面的方式
# # driver.switch_to_default_content()

# 新的
driver.switch_to.default_content()
driver.find_element_by_id('uid').send_keys('woyouhuilaila!')

time.sleep(3)
driver.quit()
