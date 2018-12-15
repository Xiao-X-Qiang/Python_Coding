(func):
            def inner(*args):
                print('not qq ==inner==')
                func(args[0])
            return inner
        return outer


        return outer

@login('wechat')
def japan(*args):
    print('welcome japan',args[0])





japan('zhangqiang')