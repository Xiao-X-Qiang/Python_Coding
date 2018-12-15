
info=[]

f=open(file='./person.txt',mode='r+',encoding='utf8')

data=f.readlines()
for x in data:
    data=x.strip()
    info.append(data.split(','))

f.close()

while True:
    print('1.添加个人信息')
    print('2.打印个人信息')
    print('3.修改个人信息')
    print('4.退出')
    print('-------------')
    choice=input('输入选项：')
    if choice=='3':

    if choice=='4':
        break;