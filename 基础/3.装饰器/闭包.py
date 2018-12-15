

def outer():
    name='qiang'
    def inner():
        #name='xiong'
        print('inner name is :',name)


    print('outer name is :',name)
    return inner



f=outer()
f()

