
import socket


def main():
    # 1.创建一个套接字socket对象，用于进行通讯
    # socket.AF_INET 指明使用INET地址集，进行网间通讯
    # socket.SOCK_DGRAM 指明使用数据协议，即使用传输层的udp协议
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # DGRAM 数据报

    # 2.发送消息
    origin_address = ("192.168.123.64", 8080)  # 远程地址

    while True:
        msg = input("请输入发送的消息：")
        if msg == "exit":
            break
        udp_socket.sendto(msg.encode("gbk"), origin_address)  # encode("gbk")，远程是windows系统(默认gbk编码)

    # 3.关闭socket
    udp_socket.close()


if __name__ == "__main__":
    main()