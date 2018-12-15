

# 注意事项：
#     1.Unicode,gbk,utf8,二进制之间的关系，具体可参考幕布相关文档
#     2.关于文本的相关操作，都会在文件打开时指定编码，而二进制文件在打开时无需指定，在后续的显示或写入需求时，指定相应的解码及编码形式；
#     3.关于写操作时，文件是否存在时内容都会被清空，并且文件指针在文件开头；关于追加相关操作时，文件打开时文件指针指向文件末尾；
#     4.区分读写（以读的形式打开文件）和写读（以写的形式打开），区别在于文件指针的位置

#---------------------
#文本读

f=open(file='./hell.txt',mode='r',encoding='utf8')
data=f.read()
print(data)
f.close()

#二进制读
# f=open(file='./hell.txt',mode='rb')
# data=f.read()
# data1=data.decode('utf8')
# print(data)
# print(data1)
# f.close()

#---------------------

#文本写
# f=open(file='./hello.txt',mode='w',encoding='gbk')
# f.write('hello,world')
# f.write('这是一个测试文件')
# f.close()


#二进制写
# f=open(file='./hello_bin.txt',mode='wb')
# f.write('hello.world'.encode('gbk'))
# f.write('这是一个二进制写测试文件'.encode('gbk'))
# f.close()

#---------------------

#文本追加
# f=open(file='./hell.a.txt',mode='a',encoding='gbk')
# f.write('hell')
# f.write('这是一个文本追加测试文件')
# f.close()

#二进制追加
# f=open(file='./hell_bin.a.txt',mode='ab')
# f.write('helo.world\n'.encode('gbk'))
# f.write('这是一个二进制追加写测试文件'.encode('gbk'))
# f.close()

#---------------------

#文本追加读写
# f=open(file='./hell.txt',mode='a+',encoding='utf8')
# f.seek(0)
# data=f.read()
# print(data)
#
# f.write('这是一个文本追加读写测试文件\n')
#
# f.seek(0)
# data1=f.read()
# print(data1)
# f.close()

#二进制追加读写
# f=open(file='./hell.txt',mode='ab+')
# f.seek(0)
# data=f.read()
# print(data.decode('utf8'))
#
# f.write('这是一个二进制读写测试文件\n'.encode('utf8'))
#
# f.seek(0)
# data1=f.read()
# print(data1.decode('utf8'))
# f.close()


#---------------------

#文本读写
# f=open(file='./hell.txt',mode='r+',encoding='utf8')
# data=f.read()
# print(data)
# f.write('这是一个文本读写测试文件\n')
# f.seek(0)
# data1=f.read()
# print(data1)
# f.close()

#二进制读写
# f=open(file='./hell.txt',mode='rb+')
# data=f.read()
# print(data.decode('utf8'))
# f.write('这是一个二进制读写测试文件'.encode('utf8'))
# f.seek(0)
# data1=f.read()
# print(data1.decode('utf8'))
# f.close()

#---------------------

#文本写读
# f=open(file='./hell.txt',mode='w+',encoding='utf8')
# data=f.read()
# print(data)
#
# f.write('这是一个文件写读测试文件')
# f.seek(0)
# data1=f.read()
# print(data1)
# f.close()


#二进制写读
# f=open(file='./hell.txt',mode='wb+')
# data=f.read()
# print(data.decode('utf8'))
#
# f.seek(0)
# f.write('这是一个二进制写读测试文件'.encode('utf8'))
#
# f.seek(0)
# data1=f.read()
# print(data1.decode('utf8'))
# f.close()

#---------------------