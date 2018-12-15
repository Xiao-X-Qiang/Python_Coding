
import gevent, time
from gevent import monkey

monkey.patch_all()


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(2)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()

# name = [gevent.spawn(f, 5),
#         gevent.spawn(f, 5),
#         gevent.spawn(f, 5)]
# gevent.joinall(name)





