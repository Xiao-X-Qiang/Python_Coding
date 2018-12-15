
import os
import multiprocessing


def copy_file(q, temp, old_fold_name, new_fold_name):
    """拷贝文件"""
    old_f = open(old_fold_name + '/' + temp, 'rb')
    # 字节的形式写入，无需考虑编码问题，拿过来放过去的操作，如果需要显示或写入新内容时，需要指定编码
    new_f = open(new_fold_name + '/' + temp, 'wb')
    data = old_f.read()
    new_f.write(data)
    new_f.close()
    old_f.close()
    q.put(temp)  # 拷贝文件后，将文件名放入消息队列，以供主进程获取查看


def main():

    # 1.获取要拷贝的文件夹名
    old_fold_name = input("请输入要拷贝的文件夹:")
    # 2.获取文件列表
    file_names_list = os.listdir(old_fold_name)
    # 3.创建目标文件夹
    new_fold_name = old_fold_name + "复件"
    try:
         os.mkdir(new_fold_name)
    except:
        pass

    # 4.向目标文件夹中多任务写文件
    # 4.1 创建消息队列，使子进程与主进程进行通信，进程池内使用的是Manger()中的Queue()方法
    q = multiprocessing.Manager().Queue()
    # 4.2 创建进程池，多任务拷贝文件
    p = multiprocessing.Pool(5)
    for temp in file_names_list:
        p.apply_async(copy_file, (q, temp, old_fold_name, new_fold_name))

    p.close()
    #p.join()
    # 5.显示文件拷贝进度，通过进程间的消息队列实现
    old_file_num = len(file_names_list)
    new_file_num = 0
    while True:
        q.get()  # 消息队列为空时，阻塞
        new_file_num += 1
        print("\r完成复件的百分比为：%.2f%%" % (new_file_num * 100 / old_file_num), end=' ')
        if new_file_num == old_file_num:
            break


if __name__ == "__main__":
    main()