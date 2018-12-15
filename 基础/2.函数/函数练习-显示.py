


def read_info():  #读取文件，并以列表组的形式返回员工信息，以及员工总数  return:(info,count)

    info=[]   #存员工信息
    count=0   #员工总数
    f=open('./person',mode='r+',encoding='utf8')
    data=f.readlines()
    for i in data:
        i=i.strip()
        info.append(i.split(','))
        count+=1
    f.close()

    return info,count

def query_info(info_1,count_1):

    msg = ['id','name','phone','dept','time']
    while True:

        num=0 #查询符合条件的个数

        print('********')
        print('1.按年龄查看')
        print('2.按部门查看')
        print('3.按入职年份查看')
        print('4.退出')
        choice_1=input('your choice is :')
        if choice_1 =='1':
            age_1=input('输入年龄阈值：')
            print(msg)
            for x in info_1:
                if int(x[2])>int(age_1):
                    print(x)
                    num+=1
            print('查询符合该条件的个数为：',num)
        if choice_1 =='3':
            year=input('input the year is :')
            print(msg)
            for x in info_1:
                if year in x[-1].split('-'):
                    print(x)
                    num+=1
            print('查询符合该条件的个数为：',num)

        if choice_1 == '4':
            return

def add_info(info_2,count_2):

    f_2=open(file='./person',mode='a+',encoding='utf8')

    while True:
        temp_2=[] #保存添加的员工信息
        temp_2.append(str(count_2+1)+',')
        temp_2.append(input('name is :')+',')
        temp_2.append(input('phone is :')+',')
        temp_2.append(input('dept is :')+',')
        temp_2.append(input('time is :')+'\n')

        f_2.writelines(temp_2)


        count_2+=1

        print(temp_2)

        again=input('是否继续添加 ？y or n')
        if again == 'y':
            continue
        else:
            break

    f_2.close()



while True:
    info_0 = []  # 保存员工信息
    count_0 = 0  # 保存员工数量

    temp = read_info()  # 读取员工信息
    info_0 = temp[0]
    count_0 = temp[1]

    print('********')
    print('1.查询员工信息')
    print('2.增加员工信息')
    print('3.删除员工信息')
    print('4.修改员工信息')
    print('5.退出')
    print('********')
    choice = input('input your choice is :')
    if choice == '1':
        query_info(info_0,count_0)
        continue
    elif choice == '2':
        add_info(info_0,count_0)
        continue
    elif choice == '5':
        break




