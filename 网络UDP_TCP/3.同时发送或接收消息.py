
import socket


def main():
    # 1.创建一个套接字socket对象，用于进行通讯
    # socket.AF_INET 指明使用INET地址集，进行网间通讯
    # socket.SOCK_DGRAM 指明使用数据协议，即使用传输层的udp协议
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.接收或发送消息
    address = ("", 8080)  # 本地地址，端口设为8080
    origin_address = ("192.168.123.64", 8080)
    udp_socket.bind(address)

    while True:
        msg = input("输入要发送的消息：")
        udp_socket.sendto(msg.encode("gbk"),origin_address)  # 向远程发消息(注意gbk编码)
        (receive_data, origin_address) = udp_socket.recvfrom(1024)  # 接收远程消息
        print("%s：%s"%(str(origin_address), receive_data.decode("gbk")))  # 注意gbk解码

    # 3.关闭socket
    udp_socket.close()


if __name__ == "__main__":
    main()