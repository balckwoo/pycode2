# 类 计算机类
# class ComputerClass(object):
#     # 类的属性(变量）
#     color = 'red'
#     size = 19
#
#     # 类的动作（方法）
#     def screw(self):
#         print('可以砸')
#
#     def watchTV(self):
#         pass
#
#     def sendcode(self):
#         return '这台电脑用于写代码'
# if __name__ == '__main__':
#     DELL = ComputerClass()
#     # 戴尔电脑实例化
#     HP = ComputerClass()
#     # 惠普电脑实例化
#     Apple = ComputerClass()
#     # 苹果电脑实例化
#
#     def funcA():
#         print('haha')
#     var = DELL.sendcode()
#     print('DELL在',var)
#     var1 = Apple.sendcode()
#     print('Apple',var)
#
#     # 注意函数和方法的区别
#     funcA()
# # # 面向对象编程
# # # 面向（去处理实例所发生的各种情况的）编程

# 这是一个函数
# def funcA(a):
#     return 'this is hanshu'

# 全局变量（作用域所有）
# var1 = 10
#
# class Aclass(object):
#     # 类变量（作用域 类本身）
#     var2 = 20
#     # 这是一个方法（动作）
#     # self 就是和我们运行实例化的时候的实例绑定了关系
#     def methodA(self,a,b,*args,**kwargs):
#         print(a,b)
#         print(args)
#         print(kwargs)
#         return 'this is fangfa'
#
#     def methodB(self):
#         # 局部变量（作用域仅限于本方法内）
#         var3 = 30
#         print(var3)
#         print(self.var2)
#
#     def methodC(self):
#         # 类变量的调用  实例.变量
#         print(self.var2)
#
#     def methodD(self):
#         # 这是一个实例变量（作用域类本身）
#         # 必须要运行进入到内存才可运用
#         self.var4 = 40
#         print(self.var4)
#
#     def methodE(self):
#         print(self.var4)
#
# if __name__ == '__main__':
#     run = Aclass()
#     # print(run.methodA(1,2,3,4,5,x=23,y=55,u=242))
#     run.methodB()
#     run.methodD()
#     print(run.var4)
#     print(run.var2)
#     # run.methodE()

class Bclass(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print('实例变量self a的值是',self.a)
        print('实例变量self b的值是',self.b)
        print('这是构造方法的内容')

    def methodA(self,a):
        print(self.b)
        print(a)
        print('这是一个实例方法1')

    def methodB(self):
        print(self.a)
        print('这是一个实例方法2')

    # 魔法方法（析构方法）
    # 在所有调用完毕后自动执行
    def __del__(self):
        print('这是析构方法的内容')

if __name__ == '__main__':
    # 实例化过程中，在类中赋值就是给init方法赋值
    run = Bclass(10,'admin')

    run.methodB()
    run.methodA(a=23)
