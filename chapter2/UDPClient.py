from socket import *

serverName = '192.168.56.104'
serverPort = 24000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    message = input('me> ')
    if(message == "quit"):
        break
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(serverName + "> " + modifiedMessage.decode())
clientSocket.close()