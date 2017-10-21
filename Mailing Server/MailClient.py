#!/usr/bin/python

# modified by Rolf K Gilet
import socket
import time
import ssl
import base64

def send_recv(socket, msg, code):
    if msg != None:
        print "<xmp> Sending==> ", msg, "</xmp>"
        print "</br>"
        socket.send(msg + '\r\n')

    recv = socket.recv(2048)
    print "<xmp> <==Received: ", recv, "</xmp>"
    print "</br>"
    if recv[:3]!=code:
        print '%s reply not received from server.' % code
    return recv

def send(socket, msg):
    print "Sending ==> ", msg
    socket.send(msg + '\r\n')
    
def send_mail(fromName,fromServer,toNameVar,toServerVar,subject, message):
    serverName = 'smtp.cis.fiu.edu'
    serverPort = 25

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    recv = send_recv(clientSocket, None, '220')

    clientName = 'Rolf K Gilet'
    userName = fromName
    userServer = fromServer
    toName = toNameVar
    toServer = toServerVar

    #Send HELO command and print server response.
    heloCommand='EHLO %s' % clientName
    recvFrom = send_recv(clientSocket, heloCommand, '250')

    #Send MAIL FROM command and print server response.
    fromCommand='MAIL FROM: <%s@%s>' % (userName, userServer)
    recvFrom = send_recv(clientSocket, fromCommand, '250')

    #Send RCPT TO command and print server response.
    rcptCommand = 'RCPT TO: <%s@%s>' % (toName, toServer)
    recvRcpt = send_recv(clientSocket, rcptCommand, '250')
    
    #Send DATA command and print server response.
    dataCommand = 'DATA'
    dataRcpt = send_recv(clientSocket, dataCommand, '354')

    #Send message data.
    send(clientSocket, "Date: %s" % time.strftime("%a, %d %b %Y %H:%M:%S -0400", time.localtime()));
    send(clientSocket, "From: Rolf K Gilet <%s@%s>" % (userName, userServer));
    send(clientSocket, "Subject: %s" % subject);
    send(clientSocket, "To: %s@%s" % (toName, toServer));
    send(clientSocket, ""); #End of headers
    send(clientSocket, message);
    #Message ends with a single period.
    send_recv(clientSocket, ".", '250');
    #Send QUIT command and get server response.
    quitCommand = 'QUIT'
    quitRcpt = send_recv(clientSocket, quitCommand, '221')
