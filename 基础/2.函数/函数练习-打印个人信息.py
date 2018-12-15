

info=[]

f=open(file='./person.txt',mode='r+',encoding='utf8')
f1=open(file='./person1.txt',mode='w+',encoding='utf8')


data=f.readlines()

f1.writelines(data)


for x in data:
    data=x.strip()
    info.append(data.split(','))

f.close()
f1.close()
print(info)

for x in info:
    print('-----------')
    print('name is :',x[0])
    print('age is :',x[2])
    print('----------\n')




