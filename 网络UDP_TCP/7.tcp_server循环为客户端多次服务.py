
import socket

def main():
    # 1.创建套接字,此为监听套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定IP及Port
    server_address = ("", 8080)
    tcp_server.bind(server_address)

    # 3.listen使套接字变为可以被动链接
    tcp_server.listen(128)
    while True:
        # 4.accept等待客户端的链接，返回的新套接字用于为客户端服务
        client_socket, client_address = tcp_server.accept()
        while True:
            # 5.recv/send接收发送消息
            recv_data = client_socket.recv(1024)
            if recv_data:
                print(recv_data.decode("gbk"))
                client_socket.send("信息己收到".encode("gbk"))
            else:
                break

        # 6.关闭套接字
        client_socket.close()
    tcp_server.close()

if __name__ == "__main__":
    main()