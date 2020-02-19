import time
from selenium import webdriver
# 实例化一个driver对象
# 实例化谷歌浏览器对象
driver = webdriver.Chrome()
url = 'E:/pycode2/SeleniumDemo/multiple.html'
driver.get(url)
# 导入下拉菜单所需要的库
from selenium.webdriver.support.ui import Select

# 如果哟一天你发现公司业务下拉菜单不是用select标签去定位的不需要使用这个方法，直接可以点击具体元素

# 先定位到select标签
ele = driver.find_element_by_id('ShippingMethod')

# 下拉菜单的方式一
# 使用select标签的value属性进行定位
# Select(ele).select_by_value('8.34')

# 下拉菜单的方式2
# 使用select标签的文本值进行定位
# Select(ele).select_by_visible_text('USPS Priority Mail Insured==> $9.25')

# 下拉菜单的方式3
# 使用Select标签的下标的方式去获取值（从0开始）
Select(ele).select_by_index(2)

time.sleep(3)
driver.quit()