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
#
# class Bclass(object):
#     # 魔法方法（构造方法）在初始化的过程中首先运行
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         print('实例变量self a的值是',self.a)
#         print('实例变量self b的值是',self.b)
#         print('这是构造方法的内容')
#
#     def methodA(self,a):
#         print(self.b)
#         print(a)
#         print('这是一个实例方法1')
#
#     def methodB(self):
#         print(self.a)
#         print('这是一个实例方法2')
#
#     # 魔法方法（析构方法）
#     # 在所有调用完毕后自动执行
#     def __del__(self):
#         print('这是析构方法的内容')
#
# if __name__ == '__main__':
#     # 实例化过程中，在类中赋值就是给init方法赋值
#     run = Bclass(10,'admin')
#
#     run.methodB()
#     run.methodA(a=23)

# 定义一个列表类
# 列表类里面可以用列表的方法
# 列表类包含
# 添加的方法
# （不传参的情况下，在最后添加一个数据）
# 传下标的情况下，添加到对应位置

# 删除的方法
# 不传参的情况下，删除最后面一个数据
# 传下标的情况下，删除对应位置

# 查询方法（查询整个列表的所有数据）

# listvar = []

# 增加
# listvar.append(10)
# listvar.append(14)
# listvar.append(13)
# listvar.insert(2,243)
# print(listvar)
#
# # 删除
# listvar.pop()
# listvar.pop(2)
# print(listvar)

# class ListClass(object):
#     def __init__(self):
#         self.listvar = []
#
#     def add(self,var,index=None):
#         if index is None:
#             self.listvar.append(var)
#         else:
#             self.listvar.insert(index,var)
#         return '添加列表成功{}'.format(self.listvar)
#
#     def remove(self,index=None):
#         if index is None:
#             self.listvar.pop()
#         else:
#             self.listvar.pop(index)
#         return '删除列表成功{}'.format(self.listvar)
#
#     def get(self):
#         return self.listvar
# if __name__ == '__main__':
#     run = ListClass()
#     print(run.add(30))
#     print(run.add(32,12))
#     print(run.remove())
#     print(run.remove(0))
#     print(run.get())

# class Bclass(object):
#     # 实例方法
#     def methonA(self):
#         print('self is',self)
#         print('这是一个实例方法')
#
#     # 类方法
#     @classmethod
#     def methodB(cls):
#         print('cls is',cls)
#         print('这是一个类方法')
#
#     @staticmethod
#     def methodC():
#         print('这是一个静态方法')
#
# if __name__ == '__main__':
#     # 实例方法必须要实例化之后才可以调用
#     run = Bclass()
#     run.methonA()
#     # 类方法不需要实例化
#     Bclass.methodB()
#     print('Bclass is',Bclass)
#     # 静态方法
#     run.methodC()
#     Bclass.methodC()

# class Cclass(object):
#     var =10
#     # __两个下划线的比那里，就叫做私密变量
#     # 只可以以在类里面被调用，实例化后无法调用
#     __var2 = 20
#     def methodA(self):
#         print(self.__var2)
#         print('这是一个实例方法')
#
#     # __两个下划线的方法，就叫做私密方法
#     # 只可以在类里面被调用，实例化吼无法调用
#     def __methodB(self):
#         print('这是一个实例方法2')
#
#     def methodC(self):
#         self.__methodB()
# if __name__ == '__main__':
#     run = Cclass()
#     print(run.methodC())

# class Register(object):
#     def __init__(self):
#         self.username = 'admin'
#         self.pwd = '123456'
#         self.role = '10'
#     def funcA(self):
#         print('这是一个实例方法')
#
# if __name__ == '__main__':
#
#     run = Register()
#     # __dict__以字典的格式获取init中的所有的属性（变量）
#     print('原来的init字典中有',run.__dict__)
#     result = run.__dict__
#     print(result)
#
#     # setattr()  init中添加属性（变量）
#     setattr(run,'job','it')
#     print('现在的init字典中有',run.__dict__)
#
#     # getattr() init中查找属性方法是有存在
#     print(getattr(run,'self.username','not found'))

# 爸爸类
# class FatherClass(object):
#     def __init__(self):
#         self.var = 10
#     def fatherMethod(self):
#         print('babadefangfa')
#
# # 儿子类
# # 儿子类括号中写的内容是爸爸类的名称
# class SonClass(FatherClass):
#
#     def sonMethod(self):
#         # 继承后可直接self.爸爸类的方法
#         self.fatherMethod()
#         # 儿子类中没有init魔法方法，会调用爸爸类的init魔法方法
#         print(self.var)
#
# if __name__ == '__main__':
#     run = SonClass()
#     run.sonMethod()
#

#########################
# 爸爸类
# class FatherClass(object):
#     def __init__(self):
#         self.var = 10
#
#     def fatherMethod(self):
#         print('这是一个爸爸类实例方法')
#
#
# # 儿子类
# # 儿子类括号中写的内容是爸爸类的名称
# class SonClass(FatherClass):
#     def __init__(self):
#         self.var = 20
#
#     def sonMethon(self):
#         #           继承后可直接self.爸爸类的方法
#         #         self.fatherMethod()
#         #         儿子类中有init魔法方法，会调用本身属于自己的init魔法方法
#         print(self.var)
#
# if __name__ == '__main__':
#     run = SonClass()
#     run.sonMethon()

################################################
# # 爸爸类
# class FatherClass(object):
#     def fatherMethod(self):
#         print('这是一个爸爸类实例方法')
#
# # 儿子类
# class SonClass(FatherClass):
#     def funcA(self):
#         print('hello')
#
#     def fatherMethod(self):
#         print('重写，这是一个儿子类的实例方法')
#
#     def funcB(self):
#         self.fatherMethod()
#
# if __name__ == '__main__':
#     run = SonClass()
#     run.funcB()

#############################
# # 爷爷类
# class GrandPaClass(object):
#     def grandPaMethod(self):
#         print('这是爷爷类的方法')
#
# # 爸爸类
# # 爸爸类继承爷爷类
# class FatherClass(GrandPaClass):
#     def fatherMethod(self):
#         print('这是一个爸爸类的实例方法')
#
# # 儿子类
# # 儿子类继承爸爸类
# class SonClass(FatherClass):
#     def sonMethod(self):
#         print('这是一个儿子类的方法')
#     def methodB(self):
#         # 孙子就可以调用到爷爷的方法
#         self.grandPaMethod()
# if __name__ == '__main__':
#     run = SonClass()
#     run.methodB()
#######################
# # 爷爷类
# class GrandPaClass(object):
#     def __init__(self):
#         self.var = 10
#
#     def grandPaMethod(self):
#         print('这是爷爷')
# # 爸爸类
# # 爸爸类继承爷爷类
# class FatherClass(GrandPaClass):
#     def fatherMethod(self):
#         print('这是爸爸')
# # 儿子类
# # 纵向继承 （爷爷继承爸爸，爸爸继承儿子）
# # 儿子继承爸爸
# class SonClass(FatherClass):
#     def sonMethod(self):
#         print('这是儿子')
#
#     def methodB(self):
#         # 孙子可以调用到爷爷的方法
#         self.grandPaMethod()
#         # 爷爷类的Init方法内的变量
#         print(self.var)
# if __name__ == '__main__':
#     run = SonClass()
#     run.methodB()
###########################
# # 爷爷类
# class GrandPaClass(object):
#     def __init__(self):
#         self.var = 10
#
#     def grandPaMethod(self):
#         print('这是爷爷类的方法')
# # 爸爸类
# # 爸爸类继承爷爷类
# class FatherClass(GrandPaClass):
#     def __init__(self):
#         self.var = 20
#
#     def fatherMethod(self):
#         print('这是爸爸类的方法')
# # 儿子类
# # 纵向继承 （爷爷继承爸爸，爸爸继承儿子）
# # 儿子类继承爸爸类
# class SonClass(FatherClass):
#     def sonMethod(self):
#         print('这是儿子类的方法')
#     def methodB(self):
# # 孙子就可以调用到爷爷的方法
#         self.grandPaMethod()
#     # 如果爷爷类和爸爸类永阳有init会先获取爸爸类的init方法
#         print(self.var)
# if __name__ == '__main__':
#     run = SonClass()
#     run.methodB()

#######################
# 爷爷类
# class GrandPaClass(object):
#     def __init__(self):
#         self.var = 10
#
#     def grandPaMethod(self):
#         print('这是爷爷类的方法')
#
#
# # 爸爸类
# # 爸爸类继承爷爷类
# class FatherClass(GrandPaClass):
#     def __init__(self):
#         self.var = 20
#
#     def fatherMethod(self):
#         print('这是爸爸类的方法')
#
#
# # 儿子类
# # 纵向继承 （爷爷继承爸爸，爸爸继承儿子）
# # 儿子类继承爸爸类
# class SonClass(FatherClass):
#
#     def __init__(self):
#         self.var = 30
#
#
#     def sonMethod(self):
#         print('这是儿子类的方法')
#
#     def methodB(self):
#         # 孙子就可以调用到爷爷的方法
#         self.grandPaMethod()
#         # 儿子类本身有init优先获取自己的init
#         print(self.var)
#
#
# if __name__ == '__main__':
#     run = SonClass()
#     run.methodB()
########################
# 爷爷类
# class GrandPaClass(object):
#
#     def funcA(self):
#         print('这是爷爷的方法A')
#
#     def grandPaMethod(self):
#         print('这是爷爷类的方法')
#
#
# # 爸爸类
# # 爸爸类继承爷爷类
# class FatherClass(GrandPaClass):
#
#     def funcA(self):
#         print('这是爸爸的方法A')
#     def fatherMethod(self):
#         print('这是爸爸类的方法')
#
#
# # 儿子类
# # 纵向继承 （爷爷继承爸爸，爸爸继承儿子）
# # 儿子类继承爸爸类
# class SonClass(FatherClass):
#     def sonMethod(self):
#         print('这是儿子类的方法')
#
#     # 重写的时候优先获取自己的同名方法，没有在依次往上获取
#     def funcA(self):
#         print('这是儿子的方法A')
#
# if __name__ == '__main__':
#     run = SonClass()
#     run.funcA()

# 横向继承
# # 爸爸类
# class FatherClass(object):
#     def fatherMethod(self):
#         print('这是一个爸爸方法')
# # 叔叔类
# class UncleWangClass(object):
#     def uncleMethod(self):
#         print('这是一个叔叔方法')
# # 儿子类中 同时继承爸爸类和叔叔类
# class SonClass(FatherClass,UncleWangClass):
#     def sonMethod(self):
#         print('这是儿子')
#     def methodA(self):
#         self.uncleMethod()
#         self.fatherMethod()
# if __name__ == '__main__':
#     run = SonClass()
#     run.methodA()
# # 爸爸类
# class FatherClass(object):
#     def __init__(self):
#         self.var = 10
#
#     def fatherMethod(self):
#         print('这是一个爸爸方法')
#
#
# # 叔叔类
# class UncleWangClass(object):
#     def __init__(self):
#         self.var = 20
#
#     def uncleMethod(self):
#         print('这是一个叔叔方法')
# # 儿子类中 同时继承类爸爸类和叔叔类
# # 横向继承悠闲获取的顺序是，先获取本身，如果没有从左到右获取
# class SonClass(UncleWangClass,FatherClass):
#     def sonMethod(self):
#         print('这是儿子')
#     def methodA(self):
#         print(self.var)
# if __name__ == '__main__':
#     run = SonClass()
#     run.methodA()

# 定义一个用户类
# 使用字典数据类型作为数据库

# 编写一个注册方法
# 使用校验方法校验业务

# 编写一个登陆方法
# 字典数据库包含账号密码
# 数据一致返回登陆成功
# 数据不一致返回登陆失败

# 编写一个或多个校验方法
# 在注册方法中调用校验注册规则
# 校验方法规则
# 1.账号 密码长度必须大于5
# 2.账号 密码必须包含英文
# 3.字典数据库排重
###########################################
# 定义一个用户类
# 使用字典数据类型作为数据库
class UserClass(object):
    def __init__(self):
        # 数据库
        self.database = {'amdinisrator':'a23143243543'}
    # 编写一个注册方法
    # 使用校验方法校验业务
    def register(self,username,pwd):
        # 校验账户名，密码长度
        result = self.check_length(username,pwd)
        # 校验账户名，密码是否包含英文
        result2 = self.check_english(username,pwd)
        # 校验账户名，密码是否排重
        result3 = self.check_rules(username,pwd)
        # 根据三个结果进行校验
        if result is True:
            if result2 is True:
                if result3 is True:
                    return '注册成功'
        else:
            return '注册失败'
        # 编写一个登陆方法
        # 字典数据库包含账号密码
        # 数据一致返回登陆成功
        # 数据不一致返回登陆失败
    def login(self,username,pwd):
        # 获取用户数据库密码
        d_pwd = self.database.get(username,None)
        if d_pwd is not None:
            if pwd == d_pwd:
                return '登录成功'
            else:
                return '登录失败'
        # 编写一个或多个校验方法
        # 在注册方法中调用校验注册规则
        # 校验方法规则
        # 1.账号 密码长度必须大于5
        # 2.账号 密码必须包含英文
        # 3.字典数据库排重
    def check_length(self,username,pwd):
        if len(username)>5 and len(pwd)>5:
            return '长度校验通过'
        else:
            return '长度校验失败'
    def check_english(self,username,pwd):
        for i in username:
            # 如果用户名的内容包含英文就望下去校验密码是否包含英文
            if i.isalpha() is True:
                for j in pwd:
                    # 如果密码包含英文返回校验通过
                    if j.isalpha() is True:
                        return '账号密码包含英文检验通过'
            else:
                return '账号密码英文校验不通过'

    def check_rules(self,username,pwd):
        result = self.database.get(username,None)
        if result is None:
            return '校验排重通过'
        else:
            return '排重失败'

if __name__ == '__main__':
    run = UserClass()

    print(run.check_length('adminisrator','a23143243543'))
    print(run.check_english('adminisrator','a23143243543'))
    print(run.check_rules('adminisrator', 'a23143243543'))
    print(run.register('adminisrator','a23143243543'))
    print(run.login('adminisrator', 'a23143243543'))
