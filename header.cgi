
# By Rolf Kinder Gilet 

import sys
import os

print "Content-type: text/html\n\n";

#print my name
print "%s\t <br/>" % ("ROLF KINDER GILET")

#loop and print the selected elements
for name, value in os.environ.items():
        if name == "REMOTE_USER" and value!="":
                print "%s\t= %s <br/>" % (name, value)
        if name == "HTTP_ACCEPT" and value!="":
                print "%s\t= %s <br/>" % (name, value)
        if name == "HTTP_ACCEPT_LANGUAGE" and value!="":
                print "%s\t= %s <br/>" % (name, value)
        if name == "QUERY_STRING" and value!="":
                print "%s\t= %s <br/>" % (name, value)
        if name == "QUERY_STRING" and value=="":
                print "QUERY_STRING ======> is empty<br/>"
        if name == "HTTP_USER_AGENT" and value!="":
                print "%s\t= %s <br/>" % (name, value)
        if name == "REQUEST_METHOD" and value!="":
                print "%s\t= %s <br/>" % (name, value)



#print the entire environment set
#for name, value in os.environ.items():
#	print "%s\t= %s <br/>" % (name, value)


#print "Hello Python"
