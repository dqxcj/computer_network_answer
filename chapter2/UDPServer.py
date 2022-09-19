from socket import *

serverPort = 24000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(str(clientAddress[0]) + "> " + message.decode())
    modifiedMessage = input("me> ")
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
