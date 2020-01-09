# .py 模块
# 目录文件下含有__init__.py文件的就叫做是包
# import Atest
#
# # 调用Atest里面的函数
# Atest.funcA()
# print(Atest.listvar)
# 不要使用这个方法(涉及到目录下的文件获取都用from)
# from PackageA.test_a import funcA
# from PackageA.test_a import varA
# 默认导入test_a模块下面的全部东西
# from PackageA.test_a import *
# 导入指定模块
# from PackageA.test_a import funcA,varA
# 等价上面指定导入模块
# from PackageA.test_a import (
#     funcA,
#     varA,)
# 改名
# from PackageA.test_a import funcA as haha
# sys path就是 import的时候Python会去找你的包的路径，
# 这个返回的是一个列表，根据列表里面的路径，一个个的区遍历
import sys
#
# result = sys.path
#
# if __name__ == '__main__':
#     print(result)
#
# # 相对路径
# local = './packageA'
# # 绝对路径
local2 = 'E:/pycode2/pybasic/packageA'
# 面试经典问题，导包路径问题
sys.path.append(local2)
result = sys.path
print(result)

# 原生内置库
import time

# 时间戳
# 整数格式显示
a = int(time.time())
print(a)
# 生成不重复的文件
print('{}/report.txt'.format(int(time.time()*1000)))

# 格式化时间
print (time.strftime('%Y/%m/%d %H:%M:%S %A',time.localtime()))
