# 定义一个函数
# def test():
#     print('hello')
#
# # 执行函数
# test()
#
# # 函数对象
# # 把test函数对象赋值给var 这时var就是test函数对象
# var = test
# # 执行var函数
# var()

# 命名规范
# 驼峰命名法
# def getApplePie():
#     print('this is tuofeng')
#
# # 下划线命名法
# def get_apple_pie():
#     print('this is xiahuaxian')

# 函数参数
# a 叫做形参
# def funcA(a):
#     print(a)
# # 执行函数10 叫做实参
# funcA(10)
#
# # 实参给形参的传参顺序是从左到右的
# def funcB(a,b,c):
#     print(a,b,c)
# funcB(1,2,3)
#
# # 指定传参
# def funcC(a,b,c):
#     print(a,b,c)
# funcC(a=1,b=2,c=6)
#
# # 默认传参
# def funcD(a,b,c=222):
#     print(a,b,c)
# funcD(1,2)
#
# # 实参传了默认参数的值的时候，优先实参的数据，没有的时候去默认参数的数据
# def funcE(a,b,c=2324):
#     print(a,b,c)
# funcE(23,3,c=55)
#
# # 默认传参顺序从右往左
# def funcF(a,b,c=200):
#     print(a,b,c)
# funcF(1,b=2,c=22)
#
# def testA(a):
#     print(a)
# testA(1)
# a参数可以是任何东西，此处传入的是testA函数对象
# def funcG(a):
#     a()
# funcG(testA)

# 函数可以自由定义规则
# testA()需要传一个参数才能执行

# funcG()中把testA内容分开传入，最后在代码块中合并
# def funcG(a,b):
#     a(b)
# funcG(testA,10)

# 多类型传参
# 元组多类型传参（多输出的内容会变成元组）
# def funcA(a, b, *args):
#     print(a, b, args)
# funcA(10, 20, 30, 40, 50, 60, 79, 'admin', 2939)
#
# # 字典多类型传参（包裹传参）（多输出的内容会变成字典）
# def funcB(a,b,**kwargs):
#     print(a,b,kwargs)
# funcB(10,232,x=2,jfidsjf=22321,fdfs=213)
#
# # 字典元组类型多传参（包裹传参）
# def funcC(a,*args,**kwargs):
#     print(a,args,kwargs)
# funcC(2,34,5,5,6,6,6,'admin',x=1,y=2,z=2)

# 解包裹传参
# *的传参方式
# tupvar = (10,20)
# listvar = [10,20]
# strvar = 'ad'
# setvar = {10,20}
#
# def funcA(a,b):
#     print(a,b)
# funcA(*setvar)

# **的传参方式
# 传参的key 需要与变量的key相对应
# dictvar = {
#     'name':'jason',
#     'job':'it'
# }
#
# def funcB(name,job):
#     print(name,job)
# funcB(**dictvar)

# 函数默认不加return关键字，默认return None
# funcA函数中return了admin字符串，所以执行funcA()函数后var的值就是admin
# def funcA():
#     print('haha')
#     # return 'admin'
# print(funcA())
#
# def funcA():
#     print('haha')
#     return 'admin',10,[]
#
# var = funcA()
# print(var)

# 函数A可以返回多个值
def funcA():
    print('haha')
    return 'wuru',2,34
# 使用一个变量去接多个返回值的时候返回一个元组
# var = funcA()
# print(var)

# 使用多个变量去接会返回 一一对应的数据
# var,var2,var3 = funcA()
#
# print(var,var2,var3)

# if else 判断return多个结果（方式一）
# def funcA(a):
#     if a == 10:
#         return True
#     else:
#         return False
# result = funcA(9)
# print(result)

# if else判断来return多个结果（方式二）

# def funcA(a):
#     if a ==10:
#         result = True
#     else:
#         result = False
#     return result
# flag = funcA(10)
# print(flag)

# return 拥有两个作用
# 1.获取我想要的返回结果值
# 2、具备break功效

# def funcA():
#     for i in range(1,10):
#         # print(i)
#         if i == 5:
#             return i
# result = funcA()
# print(result)

# 函数变量概念
# 1.全局变量（所有地方都可以调用的到的变量）
# var = 10
# def funcA(a):
#     # (局部变量)函数内定义的变量
#     print(a)
#     var2 = 109
#     return var2
# result = funcA(var)
# print(result)

# global()声明全局变量关键字
# var =10
# print('原本的数值是',var)
# def funcA():
#     # global 关键字 声明全局变量并修改
#     global var
#     var +=1
#     return var
# funcA()
# print(var)

# listvar = [10,20]
# print('原本的列表是',listvar)
# def funcA():
#     # 改变listvar主人
#     global listvar
#     listvar = 10
# funcA()
# print(listvar)
#
# dictvar = {
#     'name':'jason',
#     'job':'it'
# }
# print('原本的字典是',dictvar)
# def funcA():
#     # 改变dictvar主人
#     global dictvar
#     dictvar = 10
# funcA()
# print(dictvar)

# 练习题
# 函数来编写一个计算器(return关键字返回结果)
# icon =+-*/
# num1
# num2
# num1 icon(+-*/) num2     1+2
# def calc(num1,num2,icon):
#     if icon == '+':
#         return '他们相加的结果是{}'.format(num1+num2)
#     elif icon == '-':
#         return '他们相减的结果是{}'.format(num1-num2)
#     elif icon == '*':
#         return '他们相乘的结果是{}'.format(num1*num2)
#     elif icon == '/':
#         return '他们相除的结果是{}'.format(num1/num2)
#     else:
#         return '输入错误'
# print(calc(2,3,'3'))

# 练习题 用函数方式
# strvar = 'fasjdfjka21jsn3jsdsd7kdn9k8nc'
# 分别输出英文和数字
# 分别输出英文的总数和数字的总数

# 我希望最后输出的结果是
# 英文字符有一共有N个
# 数字字符有一共有N个


# 方法一的提醒
# 判断是否是数字
# var = 'admin'
# result = '1'.isdigit()
# print('结果是',result)
# #
# # # 判断是否是英文
# result2 = 'a'.isalpha()
# print('结果是',result2)
# strvar = 'fasjdfjka21jsn3jsdsd7kdn9k8nc'
# def testA():
#     shuzi = []
#     yinwen = []
#     for i in strvar:
#         # print(i)
#         if i.isalpha() == True:
#             shuzhi.append(i)
#         else:
#             yinwen.append(i)
#     print('数字的长度是',len(shuzi),'英文的长度是',len(yinwen))
# testA()

# 方法二
# def testB():
#     shuzi = []
#     yinwen = []
#     for i in strvar:
#         try:
#             var = int(i)
#             shuzi.append(var)
#         except BaseException as msg:
#             yinwen.append(i)
#     print('数字的长度是', len(shuzi), '英文的长度是', len(yinwen))
# testB()

#1.小王正在学习英语单词，所以请你编写两个函数，
# 一个函数用来为它收集新的单词和翻译，
# 另一个函数用来查询自己的单词笔记

# a.当收集函数，
# 收集到已经存在单词的时候，
# 返回已经收集过不可以修改

# dictvar = {}
# def get(key):
#     return dictvar.get(key,'字典没有这个单词')
# def add(key,value):
#     if dictvar.get(key,None) is not None:
#         return '已经收集过不可以修改'
#     else:
#         dictvar[key] = value
#         return '添加单词成功'
# print(add('fdsf','ds'))
# print(get('f2'))

from functools import reduce


listvar = [10,20,30,40,50]
# 过滤函数
# print(list(filter(lambda a:a>20,listvar )))
# 对比普通函数
# def funcA():
#     new_list = []
#     for i in range(len(listvar)):
#         if listvar[i] > 20:
#             new_list.append(listvar[i])
#     return new_list
# result = funcA()
# print(result)

# 阶乘函数
# print(reduce(lambda x,y:x*y,listvar))
# def funcA(listvar):
#     a = 1
#     for i in listvar:
#         a *= i
#     return a

#
# # enumerate函数获取到列表对应的index
# for k,v in enumerate(listvar):
#     print('k is',k)
#     print('v is',v)






