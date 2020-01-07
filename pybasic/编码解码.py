# 第一个是字符串
strvar = 'admin'
print(strvar)

# 字节码
bytevar2 = b'admin'
print(bytevar2)

bytevar = b'hello'
print(bytevar)
# 解码（把bytes类型转换utf-8类型） decode
print(bytevar.decode())

strvar = 'hello'
# 编码 （把utf-8类型转化bytes类型）encode
print(strvar.encode())