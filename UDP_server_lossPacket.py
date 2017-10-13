#By Rolf Kinder Gilet
#Simulate packets loss


from socket import*
import random

serverPort =9000
servername = 'hostname'
serverSocket =socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"

while True:
	try:
            	randnum = random.randint(0,10)
                message, clientAdress= serverSocket.recvfrom(2048)
                print message
                modifiedMessage = message.upper()
                if randnum< 5:
                        continue
                serverSocket.sendto(modifiedMessage, clientAdress)
        except KeyboardInterrupt:
                print "\nInterrupted by CTRL-C"
                break
serverSocket.close()
