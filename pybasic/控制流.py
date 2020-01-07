# for循环
# listvar = [10,20,30]
# 生成一个从1到7的列表
# result = range(1,8)
# print(list(result))

# for 循环的方式来实现
# print('原本的列表是',listvar)
# # 初始变量 i
# for i in range(1,6):
#     print(i)
#     listvar.append(10)
# print('现在的列表是',listvar)

# listvar2 = [10,20,30]
# 遍历列表
# i 最开始的初始变量
# 遍历 把序列中有的数值全部都输出一遍
# # 遍历的方式一
# for i in listvar2:
#     print(i)
# # 遍历方式二
# for i in range(len(listvar2)):
#     print(listvar2[i])

# 遍历元组
# tupvar = (10,20,30)
# for i in tupvar:
#     print(i)

# 遍历字符串
# strvar = 'admin'
# for i in strvar:
#     print(i)

# 遍历字典
# dictvar = {
#     'name' : 'top',
#     'job' : 'it',
#     'address' : 'USA'
# }
# # for i in dictvar:
#     # print(i)  只遍历的key 未遍历value
#
# # 处理遍历Key的方式一
# for i in dictvar:
#     print(dictvar[i])
#
# # 处理遍历key的方式二  dictvar.items()  返回可遍历的(键, 值) 元组数组
# for i in dictvar.items():
#     print(i)

# 嵌套循环
# for i in range(1,10):
#     # print('i is',i)
#     for j in range(1,10):
#         print('j is',j)
#         for z in range(1,10):
#             print('z is',z)
# 标准99乘法表
# for i in range(1,10):
#     # i =1  j的循环就是走 （1,1+1）1圈
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,j*i),end=' ')
# print()

# 以阶梯式输出99乘法表
# for i in range(1,10):
#     # i =1  j的循环就是走 （1，1+1） 1圈
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(j,i,i*j),end=' ')
#     print()

# while循环
# listvar = [10,20,30]
# var = 3
# # while语句后面加的是条件
# while var > 0:
#     listvar.append(1)
#     print(listvar)
#     # 终结条件
#     var -=1

# if 条件判断

# var = 10
# # if 后面的也我们条件语句
#     # 需要保证执行的代码块是在if句下面
# if var == 1:
#     print('错')
# elif var == 2:
#     print('cuo')
# elif var == 10:
#     print('dui')
# else:
#     print('shuziqishishi',var)

# 猜数字的游戏
# 不需要使用循环，只需要猜一次，对就对，不对就不对
# import random
# num = random.randint(1,5)
# # print(num,type(num))
#
# result = input('请输入你想猜的数字')
# # print(result,type(result))
#
# if num == int(result):
#     print('你猜对了')
# else:
#     print('你猜错了')

# 输入3个数字abc按大小顺序输出，一定要不一样的数字
# a = int(input('请输出第一个需要猜的数字'))
# b = int(input('请输出第二个要猜的数字'))
# c = int(input('请输出第三个要猜的数字'))
#
# if a > b >c:
#     print('排列的顺序是',a,b,c)
# elif a>c>b:
#     print('排列的顺序的是',a,c,b)
# elif b>a>c:
#     print('排列的顺序是',b,a,c)
# elif b>c>a:
#     print('排列的顺序是',b,c,a)
# elif c>a>b:
#     print('排列的顺序是',c,a,b)
# elif c>b>a:
#     print('排列的顺序是',c,b,a)
# else:
#     print('系统错误')

# for if while等的嵌套使用
# listvar = ['jason','cherry','sherry','peter']
# for i in listvar:
    # print(i)

# for 加 if break的嵌套
# 如果i的值 == cherry 就不再循环
# for i in listvar:
#     print(i)
#     if i == 'cherry':
#         break

# for 加 if continue的嵌套
# 如果i的值 == cheryy就忽略不执行下面的代码
# for i in listvar:
#     print('你原本输出是',i)
#     if i == 'cherry':
#         continue
#     print('你现在输出的是',i)

# while if break continue的嵌套使用

a = 10
b = 29
# # while if break 如果b的值=29就不再循环了
# while a == 10:
#     if b == 29:
#         print(b)
#         break
# while 加 if continue的嵌套
# 如果b的值 == 29就忽略不执行下面的代码
# while a == 10:
#     if b == 29:
#         continue
#     print(b)

# 猜数字游戏（猜10次）
# 猜对了就直接告诉我猜对了
# import random
# num = random.randint(1,10)
# # 定义一个猜测的次数
# count = 10
# while count > 0:
#     var = int(input('请输入第一次猜测的数字'))
#     if var == num:
#         print('恭喜你猜对了')
#         break
#     else:
#         count -=1
#         print('你猜错了，你还剩{}次'.format(count))

# 用户为自己的账户充值
# 1.最多可以充值5次
# 2.充值的次数的总金额不可以超过500
# 定义一个账户
user = 0
# 定义一个充值次数
count = 5
# 定义一个总金额
sum = 500

while count>0:
    money = int(input('请输入你要充值的金额'))
    # 如果充值的金额<=总的充值金额就认为你是正确的
    if money <= sum:
        # 为用户进行充值
        user +=money
        # 减去总的充值金额
        sum -=money
        # 减去充值次数
        count -=1
        print('充值成功用户的余额是',user)
        print('可充值的金额还剩余',sum)
    else:
        print('你充值的金额过大',money)
        # 减去我的充值次数
        count -=1
