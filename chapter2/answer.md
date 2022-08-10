## 文章中的程序
[UDPClient](https://github.com/dqxcj/computer_network_answer/tree/main/chapter2/UDPClient.py)
[UDPServer](https://github.com/dqxcj/computer_network_answer/tree/main/chapter2/UDPServer.py)
[TCPClient](https://github.com/dqxcj/computer_network_answer/tree/main/chapter2/TCPClient.py)
[TCPServer](https://github.com/dqxcj/computer_network_answer/tree/main/chapter2/TCPServer.py)

## 复习题
### R26
TCP服务器先和客户端创建TCP连接，以对客户端的接触作出反应，再生成一个新的TCP连接用于传输数据。
2n个。 //存疑

### R27
服务器需要对客户端的初次接触作出反应，故需要先于客户端运行。
服务器只需要接受客户端发送的分组，并不需要与客户端连接，故只需要在客户发送的分组到达前运行即可，而不必在客户端运行之前运行。

## 习题
### P28
(a)会报错 “由于目标计算机积极拒绝，无法连接” 。因为TCP需要先建立连接，客户端必须在服务端运行之后再运行

(b)

## 套接字编程作业

## Wireshark 实验