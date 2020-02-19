import time
from selenium import webdriver
# 实例化一个driver对象
# 实例化谷歌浏览器对象
driver = webdriver.Chrome()
url = 'E:/pycode2/SeleniumDemo/multiple.html'
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

var = int(time.time())
# 截图
driver.get_screenshot_as_file('./{}.png'.format(var))
time.sleep(3)
driver.quit()