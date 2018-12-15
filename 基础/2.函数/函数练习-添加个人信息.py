f=open(file='./person.txt',mode='a+',encoding='utf8')

while True:
    print('------')
    print('1.添加个人信息')
    print('2.退出')
    choice=int(input('选择：'))
    if choice==1:
        name=input("输入姓名：")
        password=input('密码是：')
        age=(input('年龄：'))

        f.write(name+',')
        f.write(password+',')
        f.write(age+'\n')

    else:
        break

f.close()