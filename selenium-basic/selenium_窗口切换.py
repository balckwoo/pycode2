import time
from selenium import webdriver
# 实例化一个driver对象
# 实例化谷歌浏览器对象
driver = webdriver.Chrome()
url = 'E:/pycode2/SeleniumDemo/multiple.html'
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()

# 当前窗口对象（句柄）
current_data = driver.current_window_handle
# 因为我的a标签中有个属性叫做target 会直接打开新窗口页面工作
driver.find_element_by_link_text('百度').click()

# 获取当前浏览器全部的窗口对象
all_data = driver.window_handles
print('all data 长度是', len(all_data))
print('all data 类型是', type(all_data))
print('all data is', all_data)

# 切换到指定的窗口对象（句柄）
for i in all_data:
    # 因为all
    # data是一个列表里面有多个窗口
    # 所以需要根据一开始进入首页面的第一个窗口来判断
    # 是否是新的窗口页面
    if i != current_data:
        # 老方法
        # driver.switch_to_window()
        # 新方法
        driver.switch_to.window(i)
        current_data2 = driver.current_window_handle
        print('data2 is',current_data2)
        driver.find_element_by_id('kw').send_keys('zidonghuaceshi')
# 因为一开始打开浏览器已经获取到了当前窗口页面
# 所以可以使用该数据切换回来
time.sleep(3)
driver.switch_to.window(current_data)
driver.find_element_by_id('uid').send_keys('damin')
time.sleep(3)
driver.quit()
