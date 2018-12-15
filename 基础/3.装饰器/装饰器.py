

_usrname='alex'
_password='abc123'

user_status=False


def login(func):
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

def home():
    print('---首页---')

def america():

    print('---america---')

@login
def japan():
    print('---japan---')

@login
def china(style):

    print('---china---',style)



# japan=login(japan)


china('tok')

japan()

