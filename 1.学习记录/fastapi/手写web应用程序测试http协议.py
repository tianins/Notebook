import socket

sock = socket.socket()  # 创建一个套接字对象，用于网络通信

sock.bind(("127.0.0.1", 8080))  # 绑定 IP 地址和端口号，设置服务器监听的地址为本地回环地址（127.0.0.1）和端口 8080
sock.listen(5)  # 开始监听连接请求，最多允许 5 个连接请求等待

while True:
    conn, addr = sock.accept()  # 阻塞等待客户端连接，一旦有客户端连接成功，返回连接对象（conn）和客户端地址（addr）
    data = conn.recv(1024)  # 接收客户端发送的数据，最多接收 1024 字节
    print("客户端发送的请求信息:\n", data)  # 打印客户端发送的请求信息

    # 发送 HTTP 响应，包含状态行、响应头和响应体
    # 如果不按照http格式进行输出，浏览器将无法解析输出内容
    # conn.send(b"HTTP/1.1 200 OK\r\nserver:yuan\r\nhello world")  \r\n\r\n 表示换行再空一行，这样才能表示响应头结束
    conn.send(b'HTTP/1.1 200 OK\r\ncontent-type:application/json\r\nserver:yuan\r\nserver2:yuan2\r\n\r\n{"txt":"hello world"}')
    conn.close()  # 关闭当前连接


