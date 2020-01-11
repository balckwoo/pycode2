# 装饰器
def decorate(func):
    def inner(*args,**kwargs):
        print('代码从这里开始')
        result = func(*args,**kwargs)
        print('代码到这里结束')
        return result
    return inner
@decorate
def funcA():
    print('这是一个函数')
data = funcA()
print(data)