import socket
import threading

def main():

    def send_message(udp_socket, origin_address):
        # 3.发送消息
        while True:
            send_msg = input("请输入要发送的消息：")
            udp_socket.sendto(send_msg.encode("gbk"), origin_address)

    def recv_message(udp_socket):
        # 4.接收消息
        while True:
            recv_data = udp_socket.recvfrom(1024)
            print("%s : %s" % (str(recv_data[1]), recv_data[0].decode("gbk")))

    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定端口
    ip_address = ("192.168.123.22", 8080)  # 本地ip及端口
    origin_address = ("192.168.123.64", 8080)  # 远程的ip及端口
    udp_socket.bind(ip_address)
    # 创建子线程对象
    thread1 = threading.Thread(target=send_message, args=(udp_socket, origin_address))
    thread2 = threading.Thread(target=recv_message, args=(udp_socket, ))  # (3,)加，后才是元组
    # 创建子线程并运行
    thread1.start()
    thread2.start()

    # 5.关闭套接字
    #udp_socket.close()  # 不能添加该语句，否则主线程执行该语句后等待，子线程使用的套接字已经被关闭将会出错

if __name__ == "__main__":
    main()
