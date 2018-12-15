
from collections import Iterator
from collections import Iterable

num = (x for x in range(1, 11))


class Classmate(object):
    def __iter__(self):
        pass

    def __next__(self):
        pass

classmate = Classmate()

print(isinstance(classmate, Iterable))
print(isinstance(classmate, Iterator))
print(isinstance([], Iterable))  # 可迭代的
print(isinstance(num, Iterator))  # 迭代器

