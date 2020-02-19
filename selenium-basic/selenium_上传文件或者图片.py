import time
from selenium import webdriver
# 实例化一个driver对象
# 实例化谷歌浏览器对象
driver = webdriver.Chrome()
url = 'E:/pycode2/SeleniumDemo/multiple.html'
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

import os
# 上传图片的方式一
# driver.find_element_by_name('file').click()
# # 因为系统的操作框可能弹出来的时间不稳定，此处只能用线程休眠
# time.sleep(3)
# # 上传图片的这个工作是由uploadFile.exe做完的
# os.system('C:/Users/Administrator/Desktop/uploadFile.exe')


# 方式二

ele = driver.find_element_by_name('file')
driver.execute_script('arguments[0].removeAttribute("readonly");', ele)
ele.send_keys('C:/Users/Administrator/Desktop/111.png')
time.sleep(3)
driver.quit()