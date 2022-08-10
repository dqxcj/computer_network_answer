from socket import *

serverName = '192.168.56.102'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
while True:
    message = input('me> ')
    if(message == "quit"):
        break
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(2048)
    print(serverName + "> " + modifiedMessage.decode())
clientSocket.close()
