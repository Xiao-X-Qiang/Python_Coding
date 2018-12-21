
import socket

client_list = list()  # 用于保存与客户端相连的套接字
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.setblocking(False)  # 设置套接字为非阻塞的方式

while True:
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
            client_socket.recv()
        except Exception as ret:
            print("没有收到消息")
        else:
            print("收到消息")
