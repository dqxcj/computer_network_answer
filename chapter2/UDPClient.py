from socket import *

serverName = '192.168.56.102'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', 5432))
while True:
    message = input('me> ')
    if(message == "quit"):
        break
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(serverName + "> " + modifiedMessage.decode())
clientSocket.close()