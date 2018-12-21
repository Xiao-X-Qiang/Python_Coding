from contextlib import contextmanager


@contextmanager
def my_open(path, mode):
    
    f = open(path, mode)
    yield f
    print("文件关闭")
    f.close()


with my_open("out.txt", 'w') as f1:

    f1.write("hello,the simplest contest manager")




