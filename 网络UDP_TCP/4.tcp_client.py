
import socket


def main():
    # 1.创建一个套接字socket对象，用于进行通讯
    # socket.AF_INET 指明使用INET地址集，进行网间通讯
    # socket.SOCK_STREAM 指明使用数据协议，即使用传输层的tcp协议
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # STREAM 字节流

    # 2.链接服务器
    server_address = ("192.168.123.64", 8080)
    tcp_socket.connect(server_address)

    # 3.发送/接收消息
    send_data = input("请输入要发送的消息：")
    tcp_socket.send(send_data.encode("gbk"))

    recv_data = tcp_socket.recv(1024)
    print(recv_data.decode("gbk"))

    # 3.关闭socket
    tcp_socket.close()


if __name__ == "__main__":
    main()