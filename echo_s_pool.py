import socket
import queue
from select import select

SERVER_IP = ('', 9998)

# 保存客户端发送过来的消息,将消息放入队列中
message_queue = {}
input_list = []
output_list = []

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(SERVER_IP)
    server.listen(10)
    # 设置为非阻塞,False非阻塞，True阻塞
    server.setblocking(False)

    # 初始化将服务端加入监听列表
    input_list.append(server)

    while True:
        # 开始 select 监听,对input_list中的服务端server进行监听
        stdinput, stdoutput, stderr = select(input_list, output_list, input_list)

        # 循环判断是否有客户端连接进来,当有客户端连接进来时select将触发
        for obj in stdinput:
            # socket的三种情况①判断当前触发的是不是服务端对象, 当触发的对象是服务端对象时,说明有新客户端连接进来了
            if obj == server:
                # 接收客户端的连接, 获取客户端对象和客户端地址信息
                conn, addr = server.accept()
                print("Client {0} connected! ".format(addr))
                # 新的套接字加入input_list(),发送数据是可以被检测
                conn.setblocking(False)
                input_list.append(conn)

                # 为连接的客户端单独创建一个消息队列，用来保存客户端发送的消息
                message_queue[conn] = queue.Queue()

            else:
                # ②判断是否为已连接的socket发送数据，如果是，recv接收
                recv_data = obj.recv(1024)
                if recv_data:
                    # 客户端未断开
                    print('Received  "%s" from %s' % (recv_data.decode(), obj.getpeername()))
                    # 将收到的消息放入到各客户端的消息队列中
                    message_queue[obj].put(recv_data)

                    # 将回复操作放到output列表中，让select监听
                    if obj not in output_list:
                        output_list.append(obj)
                else:
                    # ③客户端断开连接了，将客户端的监听从input列表中移除
                    print("Client  {0} disconnected\n".format(obj.getpeername()))
                    if obj in output_list:
                        output_list.remove(obj)
                    input_list.remove(obj)
                    # 移除客户端对象的消息队列
                    del message_queue[obj]
                    obj.close()

        # 如果现在没有客户端请求,也没有客户端发送消息时,开始对发送消息列表进行处理,是否需要发送消息
        for sendobj in stdoutput:
            # 如果消息队列中有消息,从消息队列中获取要发送的消息
            if not message_queue[sendobj].empty():
                # 从该客户端对象的消息队列中获取要发送的消息
                send_data = message_queue[sendobj].get()
                sendobj.sendall(send_data)
                print('ehco > ',send_data.decode())
            else:
                # 将监听移除等待下一次客户端发送消息
                output_list.remove(sendobj)



