
# By ROlf Kinder Gilet
# calculate Round trip time (RTT) 
# usinge timeout 

# udp_client.py

import time
from socket import *


serverName = 'localhost'
serverPort = 9000
clientSocket = socket(AF_INET, SOCK_DGRAM)


message = "hello"
i = 0
while(i < 10):
    senttime = time.time()
    clientSocket.settimeout(1)
    clientSocket.sendto(message, (serverName, serverPort))
    try:
        modifiedmessage, addr = clientSocket.recvfrom(2048)
    except timeout:
                print "Response timeout"
                i = i + 1
                continue
    print "RTT:",time.time() - senttime , "Response",i,":",modifiedmessage
    i = i + 1
clientSocket.close()
