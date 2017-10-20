#TCP_server with conditional get

from socket import socket, SOCK_STREAM, AF_INET
import os
import time

#create and retuns socket
def openTCPSocket(portNum):
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(('', portNum))
        serverSocket.listen(1)
        return serverSocket

#send requested file
def sendFile(connectionSocket, filename, type):
        file = open(filename,"r")
        length = str(os.path.getsize(filename))
        message = "HTTP/1.1 200 OK\r\nContent Type: " + type +"\r\nContent Length: " + length+ "\r\n\r\n" + file.read()
        connectionSocket.send(message)

#send 404 error html page
def sendError(connectionSocket, errorCode, message):
        file = open("404.html","r")
        length = str(os.path.getsize("404.html"))
        print length
        errormessage = "HTTP/1.1 " + errorCode + " " + message + "\r\nContent Type: text/html"+"\r\nContent Length: "+length+ "\r\n\r\n" + file.read()
        connectionSocket.send(errormessage)

# send 304 not modified message
def send304(connectionSocket, errorCode, message):
        errormessage = "HTTP/1.1 304 Not Modified"
        connectionSocket.send(errormessage)

# get last modified time from file
def getlastmodified(filename):
        milisecTime = os.path.getmtime(filename)
        #convert milisec time to needed format
        lastModifiedTime = time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime(milisecTime))
        formatedtime = time.strptime(lastModifiedTime, '%a, %d %b %Y %H:%M:%S GMT')
        return formatedtime

#assuming that if there is an If Modified since in the header
# it is not null
def getIfModTime(message):
    # look for if modified since in the message header
    offset = message.find("If-Modified-Since: ")
    #check if modified since was found
    if offset > 0:
        #retrive the date from the  the message's header
        dateFromRequest = message[offset + 19:offset + 48]
        # convert the date string into a time instance
        requestDateTime = time.strptime(dateFromRequest, '%a, %d %b %Y %H:%M:%S GMT')
        return requestDateTime
    # if modified wasn't found return 0
    return 0

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
            # try to get if mod time from message header
            request_mod_Time = getIfModTime(message)
            # check if there was an if mod
            if (request_mod_Time != 0):
                # try to open the file
                # if file not exist will trigger IOError
                # which will send 404 not found message
                file = open(filename, "r")
                # so file exist we can get the date from the file
                lastModified = getlastmodified(filename)
                # compare the dates and see if we should send the file or not
                if lastModified < request_mod_Time:
                    print "Not Modified %s" % filename
                    send304(connectionSocket, '303', 'Not Modified')
                    connectionSocket.close()
                    continue
            # send the file if the server have the most recent one
            sendFile(connectionSocket, filename, "text/plain")
            connectionSocket.close()
        #error detection section
        except IOError:
            print "Not found %s" % filename
            sendError(connectionSocket, '404', 'Not Found')
            connectionSocket.close()
        except KeyboardInterrupt:
            print "\nInterrupted by CTRL-C"
            break
    serverSocket.close()
main()


