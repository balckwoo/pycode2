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
