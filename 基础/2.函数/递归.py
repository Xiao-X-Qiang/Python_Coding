

# def func(n,count):
#     print(n,count)
#     if count<=5:
#         return func(n/2,count+1)
#     else:
#         return n
# print(func(128,1))


#递归阶乘

def func(n,sum=1):
    if n>0:
        sum=sum*n
        return func(n-1,sum)
    else:
        return sum

print(func(5))





