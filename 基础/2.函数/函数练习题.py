


# f=open(file='./test.txt',mode='r+',encoding='utf8')
#
# data=f.read()
#
# data1=data.split()
#
# f.close()
#
# print(data1,type(data1))

# data=[[1,2],[3,4],[3434,342,67]]
#
# print(len(data))

import os

def add_person():
    name = input('name is :')
    password = input('password is : ')
    age = input('age is:')
    f.seek(0, 2)
    f.write(name + ',')
    f.write(password + ',')
    f.write(age + '\n')

def show_person():
    info=[]
    f.seek(0)
    data=f.readlines()
    for x in data:
        x=x.strip()
        info.append(x.split(','))
    for x in info:
        print('name is :',x[0])
        print('age is :',x[2])
        print('**********')

def login_person(name,password):
    info=[]
    f.seek(0)
    data=f.readlines()
    for x in data:
        x=x.strip()
        info.append(x.split(','))
    for x in info:
        if name==x[0] and password==x[1]:
            return True

def modify_person(f):

    f1=open(file='./person_temp.txt',mode='a+',encoding='utf8')  #临时文件，用于存储未修改的文本
    info1=[]

    info=[]
    f.seek(0)

    data=f.readlines()

    count=0 #标记要修改的行

    for x in data:   #打印个人信息
        x=x.strip()
        info.append(x.split(','))
    for x in info:
        if x[0] ==name:
            print('name is :',x[0])
            print('password is :',x[1])
            print('age is :',x[2])
            continue
        else:
            f1.write(x[0]+',')
            f1.write(x[1]+',')
            f1.write(x[2]+'\n')

    for x in info:   #确认要修改的是第几行
        if x[0] ==name:
            break
        else:
            count+=1




    while True:
        print('1.修改名字')
        print('2.修改密码')
        print('3.修改年龄')
        print('4.退出')


        choice=input('your choice is :')
        if choice=='1':
            new_name=input('new name is :')
            f1.write(new_name+',')
            f1.write(info[count][1]+',')
            f1.write(info[count][2]+'\n')
            continue
        elif choice =='2':
            new_password=input('new password is :')
            data[count][1]=new_password
            continue
        elif choice == '3':
           new_age=input('new age is :')
           data[count][2]=new_age+'\n'
           continue
        elif choice == '4':
            f.close()
            os.remove('person.txt')
            os.rename('person_temp.txt','person.txt')
            f=open(file='./person.txt',mode='r+',encoding='utf8')
            break

        else:
            break

        f1.close()




f=open(file='./person.txt',mode='r+',encoding='utf8')

while True:
   name=input('请输入名字：')
   password=input('请输入密码：')
   if login_person(name,password):
       break
   else:
       continue

while True:
    print('1.添加个人信息')
    print('2.修改个人信息')
    print('3.打印个人信息')
    print('4.退出')
    choice = input('the choice is :')
    if choice == '1':
        add_person()
        continue
    elif choice == '2':
        modify_person(f)
        continue
    elif choice == '3':
        show_person()
        continue
    elif choice =='4':
        break
    else:
        continue

f.close()





