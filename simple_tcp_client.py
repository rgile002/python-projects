#By Rolf Kinder Gilet


from socket import socket, AF_INET, SOCK_STREAM

serverName = 'localhost'
serverPort = 9000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = "GET /helloworld.txt HTTP/1.1\r\nHost: ocelot.aul.fiu.edu:9000\r\n"
clientSocket.send(message)
modifiedMessage = clientSocket.recv(2048)
print 'localhost 9000\n', modifiedMessage
clientSocket.close()

