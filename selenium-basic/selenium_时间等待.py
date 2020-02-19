import time
from selenium import webdriver
# 实例化一个driver对象
# 实例化谷歌浏览器对象
driver = webdriver.Chrome()
url3 = 'E:/pycode2/SeleniumDemo/multiple.html'
driver.get(url3)
# 线程休眠（不管你的代码是怎么样，只要来到这里他都会休眠五秒不动）
# 如果是碰到和系统交互的模块没有办法的情况下可以使用线程休眠
# time.sleep(5)

# 隐式等待（全局等待）
# 10 ms秒数
# 智能去等待你代码中的判断元素是否出现（10秒指最多不超过10秒）
# 注意全局等待放的位置
# driver.implicitly_wait(10)

# js方式去拉滚动条
# ele = driver.find_element_by_id('uid')
# driver.execute_script("arguments[0].scrollIntoView();",ele)
# driver.find_element_by_id('uid').click()
# driver.find_element_by_id('uid').send_keys('admin')

# BY库的用法
# from selenium.webdriver.common.by import By
# # 解包裹传参方式传入
# tupvar = (By.ID,'uid')
# print(tupvar)
# # 也可以这样使用
# driver.find_element(*tupvar).click()
# driver.find_element(*tupvar).send_keys('admin')


# 显示等待（局部等待）
# 局部等待需要导入的库
# 局部等待（显示等待 针对具体某一个元素）
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# driver 驱动对象
# timeout 最多等待你元素的10秒
# poll_frequency 轮训每0.5秒去判断一次你的元素是否存在
# 判断我的text值里面有没有我包含的文本
# driver是浏览器驱动  0.5是每个0.5秒去访问1次，10是代表最多不超过10秒

# until 是等到标签中的某个值出现为止
# 判断text值是否包含预期文本
# 如果出现result 会返回true
result = WebDriverWait(driver,poll_frequency=0.5,timeout=10).until(EC.text_to_be_present_in_element(By.ID,'button_id_1'),'提交')

# 判断标签是否存在，并返回该标签对象
result2 = WebDriverWait(driver,0.5,10).until(EC.presence_of_all_elements_located(By.ID,'button_id_1'))

time.sleep(3)
driver.quit()
