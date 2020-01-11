# 相对路径
# local = './test.txt'

# 绝对路径
local = 'E:/pycode2/pybasic/test.txt'
# f = open(local,'r',encoding='utf-8')
# 以字符串的方式读取数据
# data = f.read()
# print(data)

# 以列表的方式去读取数据
# data = f.readlines()
# print(data)
# 以字节的方式去读取数据

# data = f.readline(2)
# # print(data)
# print('数据类型是',type(data))
# f.close()

# w + 具备读写功能 （清空在读写）
# f = open(local,'w+',encoding='utf-8')
# data = f.read()
# print(data)

# 只可以写入字符串
# result = f.write('administrator')
# print(result)
# data = f.read()
# print(data)
# 可写入字符串,也可以写入序列，但是序列里面的内容必须是字符串

# result = f.writelines({'ijijijiji'})
# print(result)
#
# # # 把缓存区数据写入硬盘，并清空内存
# f.flush()
# f.close()

# a+具备读写功能 （追加在读写）
# f = open(local,'a+',encoding='utf-8')
# # f.seek(1)
# # # 只可以写入字符串
# # result = f.write('haha')
# # # 可写入字符串,也可以写入序列，但是序列里面的内容必须是字符串
# # result = f.writelines({'name':'jason'})
# # data = f.read()
# # print(data)

# 新建一个test.txt记事本
# # 在里面填写hello python
# # open 函数读取并获得数据
# # 使用replace
# # 方法把数据修改Hello Python清空在写入
#
# f = open(local,'r',encoding='utf-8')
# data = f.read()
# print(data,type(data))
# result = data.replace('hello python','Hello Python')
# w = open(local,'w+',encoding='utf-8')
# data2 = w.write(result)

# open读写数据的方式二
# local = './test2.txt'
# # with关键字进行读写
# with open(local,'r',encoding='utf-8') as f:
#     data = f.read()
#     print(data)
#
# with open(local,'w+',encoding='utf-8') as f:
#     f.write('jiaowodashen2')
# # 新建一个account记事本
# 新建一个password记事本
# 1.以open函数方式在
#account记事本添加内容admin
#password记事本添加内容123456
#
# local = './account.txt'
# local2 = './password.txt'
# with open(local,'w+',encoding='utf-8') as f:
#     f.write('admin')
#
# with open(local2,'w+',encoding='utf-8') as g:
#     g.write('123456')
#
# with open(local,'r',encoding='utf-8') as h:
#     data = h.read()
#     # print(data)
# with open(local2,'r',encoding='utf-8') as j:
#     data2 = j.read()
#     # print(data2)

# 2.编写一个登陆函数(传两个参数)
# 登陆函数先判断账号是否为account账户内的值
# 相等则判断password密码的值
# 如果都相等返回登陆成功
# 否则返回登陆失败

# def denglu(zhanghao,mima):
#     if zhanghao == data:
#         if mima == data2:
#             return '登录成功！'
#     else:
#         return '账号或密码错误，请检查输入是否正确'
# result = denglu('adin','123456')
# print(result)

# local = './test2.txt'
# listvar = [10,20,30,40]
# dictvar = {
#     'name':'jason',
#     'job': 'it',
# }
#
# import json
# with open(local,'w+',encoding='utf-8') as f:
#     f.write(json.dumps(dictvar))
# #     把数据类型转换成字符串存入文本中
# with open(local,'r',encoding='utf-8') as f:
#     # 把数据类型从字符串转换为对应数据的类型
#     data = f.read()
#     print(data)
#     data2 = json.loads(data)
#     print(type(data2),data2)

# 1.编写一个注册函数
#(1)注册规则
# 账号和密码长度必须大于5
# 密码必须包含1个英文(可去掉)
# strvar = ''.isalpha()
# 账号排重（返回账户名已存在）
# import json
# def registet(username,pwd):
#     # 定义一个账户的字典
#     account = {}
#     # 账户长度必须大于5
#     if len(username) > 5:
#         # 密码长度必须大于5
#         if len(pwd) >5:
#             # 判断密码必须包含英文
#             for i in pwd:
#                 if i.isalpha() is True:
#                     account[username] = pwd
#                     with open('./account.txt','w+',encoding='utf-8') as f:
#                         f.write(json.dumps(account))
#                         return '注册成功'
#
# result = registet('administrator','a12345')
# print(result)
# 账号排重
# def register(username,pwd):
#     with open('./account.txt','r',encoding='utf-8')as f:
#         # 获取数据库里面全部的数据
#         account = json.loads(f.read())
#     # 校验数据库是否存在
#     result = account.get(username,None)
#     if result is None:
#         if len(username)>5:
#             if len(pwd)>5:
#                 for i in pwd:
#                     if i.isalpha() is True:
#                         account[username] = pwd
#                         with open('account.txt','w+',encoding='utf_8') as f:
#                             f.write(json.dumps(account))
#                             return '注册成功'
#     else:
#         return '账户已存在'
# print(register('administrator','a12345'))
# print(register('kkkkkkkk','f243255543'))

# 编写一个登录函数
# 登陆函数
#1.以字典的方式去读取数据
#2.使用字典的方式来获取key value判断

# import json
#
# # 登录函数
# def login(username,pwd):
#     with open('./account.txt','r',encoding='utf-8') as f:
#         # 通过文本读取的方式获取数据库的账户信息
#         d_account = json.loads(f.read())
#         result = d_account.get(username,None)
#         if result is None:
#             return '账户不存在'
#         else:
#             if result == pwd:
#                 return '登录成功'
#             else:
#                 return '登录失败'
# var = login('administrator','a1345')
# print(var)


# 数先判断账号是否为account账户内的值
# 相等则判断编写一个登陆函数(传两个参数)
# 登陆函password密码的值
# 如果都相等返回登陆成功
# 否则返回登陆失败
# local = './test2.txt'

# def login(account,pwd):
#     # 获取用户密码
#     with open('./password.txt', 'r', encoding='utf-8') as f:
#         d_password = f.read()
#     # 获取用户名
#     with open('./account.txt','r',encoding='utf-8') as f:
#         d_account = f.read()
#     # 如果登陆用户名 == 数据库的用户名
#     if account == d_account:
#         # 判断数据库的密码是否等于用户输入的密码
#         if pwd == d_password:
#             return '登陆成功'
#         else:
#             return '密码错误'
#     else:
#         return '账号错误'
#
# dataBase()
# result = login('admin','123456')
# print('登陆的结果是',result)

