# var = 'gaf'
# # 正常语法，代码没有错误
# try:
#     # 可能出错的代码
#     var1 = int(var)
# # 捕获我错误代码的异常并输出（如果代码的语法是没有问题的是不会走到except里面）
# except BaseException as msg:
#     print(msg)
# BaseException 是万能的错误异常类型

# try:
#     print(hello)
# except BaseException as msg:
#     print('错误的异常是',msg)
# else:
#     print('nihao')

 # else 语法当我的try代码块里面没有问题的话就会去执行
# try:
#     print('hello')
# except BaseException as msg:
#     print('错误的异常是', msg)
# else:
#     print('nihao')

# finally的代码，不管我try 里面的代码块是否正确，它都会执行
# try:
#     print('hello')
# except BaseException as msg:
#     print('错误的异常是',msg)
# finally:
#     print('nihao')

# # 综合场景
# try:
#     print(这是一个没有错的代码块)
# except BaseException as msg:
#     print(msg)
# else:
#     print('try代码没有问题的话就会执行这里')
# finally:
#     print('不管try代码块里面有没有问题他都会执行')

a = None
try:
    if a == None:
        # 主动抛出异常
        raise EOFError
    print('出错了之后代码就不会走到这里')
except BaseException as msg:
    print('代码出错了')