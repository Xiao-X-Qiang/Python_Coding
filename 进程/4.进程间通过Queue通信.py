import multiprocessing


def down_load_weg(q):
    """下载数据"""
    data = [11, 22, 33]
    q.put(data)


def analysis_data(q):
    """处理数据"""
    analysis_data = list()
    while True:
        analysis_data.append(q.get())
        if q.empty():
            break
    print(analysis_data)


def main():
    # 1.创建队列
    q1 = multiprocessing.Queue()
    # 2.创建多个进程，将队列的引用当作实参传递到进程

    p1 = multiprocessing.Process(target=down_load_weg, args=(q1,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q1,))

    p1.start()
    p2.start()

if __name__ == "__main__":
    main()
