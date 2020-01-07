intvar =10
# 赋值运算符
# 为intvar赋值加1
# intvar = intvar + 1  等价 intvar +=1
intvar +=1
print(intvar)

# 字符串
strvar = 'admin'
strvar2 = 'nihao'
# +号拼接了字符串
print(strvar+strvar2)

# 列表
listvar = [10,20]
listvar2 = [2,34,4]
print(listvar+listvar2)

# 元组
tupvar = (10,20)
tupvar2 = (1,23,4)
print(tupvar2+tupvar)

# 强类型语言和弱类型语言的差别?
# Python属于强类型的动态脚本语言
# 强类型：不予许不同类型相加
# 动态：不使用显示数据声明类型，且确定一个变量的类型是第一次给他赋值的时候
# 脚本语言：一般也是解释性语言，运行代码只需要一个解释器，不需要编译
# print(strvar + intvar)

boolvar = True
# 注意== 和 is 的区别
# ==判断具值是否相等
print(strvar == boolvar)

# 字符串值换成bool来判断
print(bool(strvar) is True)
