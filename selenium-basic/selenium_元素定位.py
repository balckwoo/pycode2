import time
from selenium import webdriver
# 实例化一个driver对象
# 实例化谷歌浏览器对象
driver = webdriver.Chrome()

# 实例化火狐浏览器对象
# f_driver = webdriver.Firefox()

# 实例化IE浏览器对象
# i_driver = webdriver.Ie()


# 打开浏览器 输入网址
url = 'https://www.baidu.com'
url2 = 'D:/share/ZM20190616/SeleniumDemo/multiple2.html'
driver.get(url2)
# 最大化窗口
driver.maximize_window()

# 后退
# driver.back()

# 最小化窗口
# driver.minimize_window()

# 线程休眠
# time.sleep(5)

# 关闭窗口
# driver.close()

# 关闭浏览器
# driver.quit()

#### 元素定位
# 八种定位方式的核心就是要你的定位的标签是独一无二的

# 使用id 方式定位
# click()点击
# send_keys()输入文本
# uid为你的id的属性的值
# driver.find_element_by_id('uid').click()
# driver.find_element_by_id('uid').send_keys('Hello')
# driver.find_element_by_id('uid')


# 使用name方式定位
# pwd为你的name的属性的值
# driver.find_element_by_name('pwd').click()
# driver.find_element_by_name('pwd').send_keys('pwd')

# 使用LinkText方式定位(精确的文本定位)
# driver.find_element_by_link_text('微软').click()

# 使用PARTIAL LINK方式定位(模糊的文本定位)
# driver.find_element_by_partial_link_text('微').click()

# 这是一句错误的定位因为我的text值是来自button标签没有带链接
#driver.find_element_by_link_text('提交').click()

# 当下情况下先理解成带有链接的标签才可以使用LinkText

# 使用CSS方式定位
# driver.find_element_by_css_selector('#uid').click()
# driver.find_element_by_css_selector('#uid').send_keys('admin')
# driver.find_element_by_css_selector('#pwdid').click()
# driver.find_element_by_css_selector('#pwdid').send_keys('pwd')

# 使用xpath定位


# xpath 标签定位里面的[]值不是从0开始从1开始
# 绝对路径下的定位
# driver.find_element_by_xpath('/html/body/div/form/input[1]').click()
# driver.find_element_by_xpath('/html/body/div/form/input[1]').send_keys('admin')
# driver.find_element_by_xpath('/html/body/div/form/input[2]').click()
# driver.find_element_by_xpath('/html/body/div/form/input[2]').send_keys('pwd')

# 相对路径下的定位
# //代表相对路径
# @是套路 套路后面跟属性和值
# * 是匹配所有标签
# 这里是匹配任何标签下id=uid的值
# driver.find_element_by_xpath('//*[@id="uid"]').click()

# 这里是只匹配Input标签下id=uid的值
# driver.find_element_by_xpath('//input[@id="uid"]').send_keys('admin')

# 使用 逻辑运算and 方式加强定位
# driver.find_element_by_xpath('//*[@id="uid" and @name="username"]').click()
# driver.find_element_by_xpath('//input[@id="uid" and @name="username"]').send_keys('admin')

# 使用xpath层级定位
# driver.find_element_by_xpath('//form[@id="f"]/input[@id="uid"]').click()
# driver.find_element_by_xpath('//form[@id="f"]/input[@id="uid"]').send_keys('admin')

# 标签里不加定位属性值也是可以的
#driver.find_element_by_xpath('//form/input[@id="uid"]').send_keys('admin')


# 层级定位方式
# ele = driver.find_element_by_id('div-id-1')
# ele.find_element_by_css_selector('#uid').click()
# ele.find_element_by_css_selector('#uid').send_keys('admin')

# 多重层级定位
# ele = driver.find_element_by_id('div-id-1')
# ele2 = ele.find_element_by_id('f')
# ele2.find_element_by_name('username').click()
# ele2.find_element_by_name('username').send_keys('admin')


# 层级定位定为一组元素
# ele = driver.find_element_by_id('div-id-5')
# result = ele.find_elements_by_tag_name('a')
# print('a标签的结果是',result)
# print('a标签的长度是',len(result))
# result[0].click()




# 定位一组元素
# 使用class或者tag标签比较多

# 定位一组元素使用class标签
# result = driver.find_elements_by_class_name('hiclass')

# 定位一组元素使用a标签
# result2 = driver.find_elements_by_tag_name('a')
# print('结果是',result2)
# print('长度是',len(result2))
# # 根据下标的方式去对具体的元素操作
# result2[4].click()

# JS定位
# 使用JS来进行元素操作定位
# ele = driver.find_element_by_id('uid')
# # 点击元素
# driver.execute_script('arguments[0].click()', ele)
# # 输入文本值
# driver.execute_script('arguments[0].value="hahaha";',ele)
# 使用JS方式拉倒指定元素位置
# target = driver.find_element_by_link_text('微软')
# driver.execute_script("arguments[0].scrollIntoView();", target)


# driver.quit()

