## 文章中的程序
[UDPClient](https://github.com/dqxcj/computer_network_answer/tree/main/chapter2/UDPClient.py)

[UDPServer](https://github.com/dqxcj/computer_network_answer/tree/main/chapter2/UDPServer.py)

[TCPClient](https://github.com/dqxcj/computer_network_answer/tree/main/chapter2/TCPClient.py)

[TCPServer](https://github.com/dqxcj/computer_network_answer/tree/main/chapter2/TCPServer.py)


## 复习题
### R1
web: HTTP   文件传输: FIP   电子邮件: SMTP  远程终端访问: Telent    流式多媒体: HTTP  

### R2
网络体系结构是固定的，其使用分层的体系结构；应用程序体系结构由应用程序研发者设计，规定了如何在各种端系统上组织该应用程序。

### R3
总是保持打开的那个进程是服务器，另一个是客户。

### R5
IP地址和端口号。

### R6
UDP。UDP没有拥塞控制机制，运输速率更快。

### R10
握手协议可以提醒客户和服务器，让它们为大量分组的到来做好准备。

### R11
HTTP、SMART和POP3都不能容忍数据丢失。

### R12
>1. 用户注册该网站时，网站服务器为该用户提供一个cookie标识码用于唯一标识该用户；
>2. 用户购买物品时，服务器将用户的购买记录与cookie标识码绑定并保存在服务器后端数据库中；
>3. 用户再次登录时，服务器会匹配请求报文中的cookie: 首部行来在后端数据库中查找该用户的购买记录并返回。

### R13
web缓存器可以保存用户最近请求的对象，当用户再次请求或其他用户请求该对象时，web缓存器可以直接将自己存储的该对象返回，省去了与服务器的连接和传输过程（与web缓存器的连接和传输过程比与服务器的连接和传输过程更节省时间）。

### R18



### R26
TCP服务器先和客户端创建TCP连接，以对客户端的接触作出反应，再生成一个新的TCP连接用于传输数据。

2n个。 //存疑

### R27
服务器需要对客户端的初次接触作出反应，故需要先于客户端运行。

服务器只需要接受客户端发送的分组，并不需要与客户端连接，故只需要在客户发送的分组到达前运行即可，而不必在客户端运行之前运行。

## 习题

### P1
>a. 错误。请求和响应必定成对。
>b. 正确。
>c. 错误。
>d. 错误。Date指响应报文的产生并发送的时间，Last-Modified才是响应中对象最后一次修改的时间。
>e. 错误。比如请求的文档不在服务器上响应报文的实体体就是空的

### P3
应用层: HTTP, DNS  运输层: TCP(运行HTTP)， UDP(运行DNS) 


### P28
(a)会报错 “由于目标计算机积极拒绝，无法连接” 。因为TCP需要先建立连接，客户端必须在服务端运行之后再运行

(b)正常运行

(c)
>TCP:由于目标计算机积极拒绝，无法连接
>UDP:客户端能运行，但不能将信息发送到服务端

原因在于端口号的作用是辨识服务端是目的主机上的哪一个进程，如果服务端和客户端的端口号不一致，则服务端的信息无法送至服务端。

### P29 (不会)




## 套接字编程作业

## Wireshark 实验