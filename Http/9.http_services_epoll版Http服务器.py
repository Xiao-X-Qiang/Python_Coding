
import socket
import re
import select


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
    # tcp_server.setblocking(False)  # 设置套接字为非阻塞的方式

    # 创建一个poll对象
    epl = select.poll()

    # 将监听套接字注册到poll对象中
    epl.register(tcp_server.fileno(), select.POLLIN)
    fd_event_dict = dict()  # fd:client_socket  套接口描述符：套接字

    while True:
        fd_event_list = epl.poll()  # 默认阻塞，直到OS监测到数据到来时，通过事件通知方式告诉这个程序，此时才会解堵塞
        for fd, event in fd_event_list:
            if fd == tcp_server.fileno():  # 有新的连接请求
                new_socket, client_address = tcp_server.accept()
                epl.register(new_socket.fileno(), select.POLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.POLLIN:  # 己连接套接字有消息收到，要么有数据，要么数据为空,即close()
                recv_data = fd_event_dict[fd].recv(1024).decode("utf8")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]


if __name__ == "__main__":
    main()
