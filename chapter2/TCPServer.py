from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, clientAddress = serverSocket.accept()
    sentence = connectionSocket.recv(2048).decode()
    print(str(clientAddress[0]) + "> " + sentence)
    modifiedMessage = input("me> ")
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()
