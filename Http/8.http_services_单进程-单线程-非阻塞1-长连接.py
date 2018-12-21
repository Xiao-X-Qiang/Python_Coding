
import socket
import time
import re


def service_client(client_socket, request):
    """为客户端返回数据"""

    # 1.接受浏览器的请求
    # request = client_socket.recv(1024).decode("utf8")  # 反序列化
    # print(request)
    request_lines = request.split('\r\n')
    print(request_lines)
    # GET /index.html HTTP/1.1
    ret = re.match(r"[^/]+/([^ ]*)", request_lines[0])

    response = "HTTP/1.1 200 OK\r\n"

    if ret.group(1):

        file_name = ret.group(1)
        try:  # 文件是否存在
            f = open(file_name, 'rb')
            data = f.read()
            response += 'Content-Length:%d\r\n\r\n' % len(data)
            client_socket.send(response.encode("utf8") + data)

        except Exception as result:  # 请求的页面不存在
            client_socket.send("HTTP/1.1 404 Not Found1\r\n".encode("utf8")
                               +"Content-Length:%d\r\n\r\n".encode("utf8") %len("NOT FOUND1")
                               + "NOT FOUND1".encode("utf8"))  # 序列化
        else:
            f.close()
        finally:
            pass

    else:   # 默认网页
        with open('index.html', 'rb') as f:
            data = f.read()
        response += 'Content-Length:%d\r\n\r\n' % len(data)
        client_socket.send(response.encode('utf8') + data)
        # client_socket.close()


def main():
    client_list = list()  # 用于保存与客户端相连的套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_server.bind(("", 8080))
    tcp_server.listen()
    tcp_server.setblocking(False)  # 设置套接字为非阻塞的方式

    while True:
        try:
            new_socket, new_addr = tcp_server.accept()
        except Exception as ret:
            pass
        else:
            client_list.append(new_socket)
            new_socket.setblocking(False)

        for client_socket in client_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf8")  # 解阻塞，要么有数据，要么客户端发起close()

            except Exception as ret:
                pass
            else:
                if recv_data:
                   service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_list.remove(client_socket)


if __name__ == "__main__":
    main()