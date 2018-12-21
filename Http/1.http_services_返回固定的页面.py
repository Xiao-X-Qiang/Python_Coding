import socket
import chardet


def service_client(clietn_socket):
    """为客户端返回数据"""

    # 1.接受浏览器的请求
    request = clietn_socket.recv(1024)

    # 2.返回http格式的数据给浏览器
    # 2.1 准备数据  --header
    response = "HTTP/1.1 200 OK\r\n\r\n"

    with open('index.html', 'rb') as f:
        send_data = f.read()

    clietn_socket.send(response.encode("utf8") + send_data)
    # print(chardet.detect(send_data.encode()))
    # clietn_socket.send(send_data)

    # 关闭客户套接字
    clietn_socket.close()


def main():
    """用来完成整体的控制"""

    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2.绑定端口
    tcp_socket.bind(("", 8080))

    # 3.listen
    tcp_socket.listen()

    while True:
        # 4.accept等待
        client_socket, client_address = tcp_socket.accept()


        # 5.服务
        service_client(client_socket)
    # 6.关闭套接字


if __name__ == "__main__":
    main()