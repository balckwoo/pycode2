import time
from selenium import webdriver
# 实例化一个driver对象
# 实例化谷歌浏览器对象

driver = webdriver.Chrome()

url = 'https://www.baidu.com'

# 本地页面的拖拽
url2 = 'E:/pycode2/拖动/Drag&DropDemo.html'
url3 = 'E:/pycode2/SeleniumDemo/multiple.html'
driver.get(url2)
driver.implicitly_wait(10)
driver.maximize_window()
# 导入鼠标事件实现悬停功能
from selenium.webdriver.common.action_chains import ActionChains
# 悬停
# ele = driver.find_element_by_name('pwd')
# # driver是本身驱动对象，ele是需要悬停的标签
# ActionChains(driver).move_to_element(ele).perform()
# # 使用Linktext方式定位
# driver.find_element_by_link_text('百度').click()

# 拖拽
# 起始需要拖动的目标
start_ele = driver.find_element_by_id('dragger')
# 需要拖动到的具体位置
end_ele = driver.find_element_by_xpath('/html/body/div[5]')

ActionChains(driver).drag_and_drop(start_ele,end_ele).perform()

time.sleep(3)

driver.quit()