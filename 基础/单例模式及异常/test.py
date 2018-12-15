#
#
# class Singleton(object):
#     __instance=None
#     __first_init=False
#
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance=object.__new__(cls)
#         return cls.__instance



try:
    print(abs())
except Exception as result:
    print('hello')
else:
    print('--else--')
finally:
    print('--finally--')

