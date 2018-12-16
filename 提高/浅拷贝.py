import copy

a = [11, 22]

b = [33, 44]

c = [a, b]

d = copy.copy(c)

print(id(c), id(d))

print(id(c[0]), id(d[0]))
