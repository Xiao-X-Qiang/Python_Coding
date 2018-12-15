

_usrname='alex'
_password='abc123'

user_status=False


def login(*login_type):

    if login_type =='qq':
        def outer(func):
            def inner(*arg):
                global user_status
                if user_status == False:

                    while True:
                        username = input('user:')
                        password = input('password:')
                        if username == _usrname and password == _password:
                            print('welcome login')
                            user_status = True
                            break
                        else:
                            print('wrong username or password,please try again')

                else:
                    print('已验证，允许登陆')

                func(*arg)

            return inner
        return outer
    else:
        def outer(func):
            def inner(*arg):
                global user_status
                if user_status == False:

                    while True:
                        username = input('user:')
                        password = input('password:')
                        if username == _usrname and password == _password:
                            print('welcome login')
                            user_status = True
                            break
                        else:
                            print('wrong username or password,please try again')

                else:
                    print('已验证，允许登陆')

                func(*arg)

            return inner
        return outer



def home():
    print('---首页---')

def america():

    print('---america---')

@login()
def japan():
    print('---japan---')

@login('qq')
def china(style):

    print('---china---',style)






china('tok')



