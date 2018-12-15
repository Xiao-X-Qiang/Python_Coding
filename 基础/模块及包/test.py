#
# class A(object):
#
#     def test(self):
#         print('A---test')
#
#     def demo(self):
#         print("A---demo")
#
#
# class B(object):
#
#     def test(self):
#         print("B---test")
#
#     def demo(self):
#         print("B---demo")
#
#
# class C(B,A):
#     pass
#
# c=C()
# print(C.__mro__)
#
# print(dir(object))
#
#
# class MusicPlayer(object):
#
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             MusicPlayer.instance = super().__new__(cls)
#         return cls.instance
#
#     def __init__(self):
#         print('test demo')
#
#
# player1 = MusicPlayer()
# print(player1)
#
# player2 = MusicPlayer()
# print(player2)


from Core.package1.send_message import send_message
send_message()

