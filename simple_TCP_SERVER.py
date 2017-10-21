# By Rolf Kinder Gilet
# send file requested by cliente if not send 404.html (Not found page) 

from socket import socket, SOCK_STREAM, AF_INET
import os

#create a TCP server with the given port number
def openTCPSocket(portNum):
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', portNum))
        serverSocket.listen(1)
        return serverSocket

# send the file requested 
def sendFile(connectionSocket, filename, type):
        file = open(filename,"r")
        length = str(os.path.getsize(filename))
        message = "HTTP/1.1 200 OK\r\nContent Type: " + type +"\r\nContent Length: " + length+ "\r\n\r\n" + file.read()
        connectionSocket.send(message)

#send not found 404 eror message 
def sendError(connectionSocket, errorCode, message):
        file = open("404.html","r")
        length = str(os.path.getsize("404.html"))
        print length
        errormessage = "HTTP/1.1 " + errorCode + " " + message + "\r\nContent Type: text/html"+"\r\nContent Length: "+length+ "\r\n\r\n" + file.read()
        connectionSocket.send(errormessage)

def main():
    serverSocket = openTCPSocket(9000)
    print "Interrupt with CTRL-C"
    while True:
        try:
            #Establish the connection
            print 'Ready to serve...'
            connectionSocket, addr = serverSocket.accept()
            message = connectionSocket.recv(4096)
            print message
            filename = message.split()[1].partition("/")[2]
            sendFile(connectionSocket, filename, "text/plain")
            connectionSocket.close()
        except IOError:
            print "Not found %s" % filename
            sendError(connectionSocket, '404', 'Not Found')
            connectionSocket.close()
        except KeyboardInterrupt:
            print "\nInterrupted by CTRL-C"
            break
    serverSocket.close()
main()
    
