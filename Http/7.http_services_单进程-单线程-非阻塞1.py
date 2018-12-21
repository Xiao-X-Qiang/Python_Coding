
import socket
import time

client_list = list()  # 用于保存与客户端相连的套接字
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("", 8080))
tcp_server.listen()
tcp_server.setblocking(False)  # 设置套接字为非阻塞的方式

while True:
    time.sleep(0.5)
    try:
        new_socket, new_addr = tcp_server.accept()
    except Exception as ret:
        print("没有新客户请求")
    else:
        print("有新客户请求")
        client_list.append(new_socket)
        new_socket.setblocking(False)

    for client_socket in client_list:
        try:
            recv_data = client_socket.recv(1024)  # 解阻塞，要么有数据，要么客户端发起close()
        except Exception as ret:
            print("没有收到消息")
        else:
            if recv_data:
                print("收到消息")
                print(recv_data.decode("gbk"))  #反序列化
            else:
                client_socket.close()
                client_list.remove(client_socket)


