import socket
import chardet
import re
import threading


def service_client(client_socket):
    """为客户端返回数据"""

    # 1.接受浏览器的请求
    request = client_socket.recv(1024).decode("utf8")  # 反序列化
    print(request)
    request_lines = request.split('\r\n')

    # GET /index.html HTTP/1.1
    ret = re.match(r"[^/]+/([^ ]*)", request_lines[0])

    response = "HTTP/1.1 200 OK\r\n\r\n"  # Header与Body的分隔标识
    if ret.group(1):

        file_name = ret.group(1)
        try:
            f = open(file_name, 'rb')
            data = f.read()
            client_socket.send(response.encode("utf8") + data)

        except Exception as result:
            client_socket.send("HTTP/1.1 404 Not Found1\r\n\r\n".encode("utf8") + "NOT FOUND1".encode("utf8"))  # 序列化
        else:
            f.close()
        finally:
            client_socket.close()

    else:
        with open('index.html', 'rb') as f:
            data = f.read()
        client_socket.send(response.encode('utf8') + data)
        client_socket.close()

    # 2.返回http格式的数据给浏览器
    # 2.1 准备数据  --header

    # print(chardet.detect(send_data.encode()))
    # clietn_socket.send(send_data)

    # 关闭客户套接字


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
        # 创建子进程对象
        p1 = threading.Thread(target=service_client, args=(client_socket,))
        p1.start()

        # client_socket.close()

        # 5.服务
        # service_client(client_socket)
    # 6.关闭套接字

if __name__ == "__main__":
    main()

# 注意，HTTP应答的Header与Body部分的标识符是"\r\n\r\n"