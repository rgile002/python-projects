
#!/usr/bin/python

# By Rolf K Gilet

import mod_html
import sys
import os
import MailClientOcelot

# allow to see any erros that are generated   
# allow	to see all output from script
sys.stderr = sys.stdout
print "Content-type: text/html\n"

#email form
def html(method,value):
    print """<!DOCTYPE HTML> <html>
  <head>
    <meta charset="utf-8">
    <title>First Form</title>
  </head>
  <body>

    <form action="" method="{1}">
      <p>
	Enter email in From<br>
        Enter email in To<br>
        Fill Subject and Message fields<br>
        Click Send or Go Back
      <p>
	FROM:<br>
         <input type="text" name="from" value=""><br>
        TO:<br>
        <input type="text" name="to" value=""><br>
        SUBJECT:<br>
        <input type="text" name="subject" value=""><br>
        MESSAGE:<br>
        <textarea name="message" rows="10" cols="30">  </textarea><br>
        <input type="button" onclick="location.href='http://ocelot.aul.fiu.edu/~rgile002/index.html';" value="Go Back">
        <input type="submit" name="submit" value="Send">
    </form>
  </body> </html>
""".format(value,method)

def main():
    # set visited to true and call    
    # parser to	retrive	data from form
    value = ""
    visited = True;
    parsed = mod_html.parse()
    if parsed is None:
        visited = False;
        parsed = {}
    # create place holder for data we have to retrive 
    fromVar = ""
    fromName = ""
    fromServer = ""
    toVar = ""
    toName = ""
    toServer = ""
    subjectVar = ""
    messageVar = ""

    # get send user name
    # get sender server name
    if "from" in parsed:
        fromVar = parsed['from']
        temp = fromVar.split('@')
        fromName = temp[0]
        fromServer = temp[1]
    
    # get recipient user name
    # get reciepient server name   
    if "to" in parsed:
        toVar = parsed['to']
        temp = toVar.split('@')
        toName = mod_html.decode(temp[0])
        toServer = mod_html.decode(temp[1])

    # get subject from the form
    if "subject" in parsed:
        subjectVar = parsed['subject']
        subjectVar = mod_html.decode(subjectVar)
    
    # get the message from the form
    if "message" in parsed:
        messageVar = parsed['message']
        messageVar = mod_html.decode(messageVar)

    # check if we actually get the data
    # for debugging 
    print fromVar,toVar,subjectVar,messageVar

    # call the form method 
    html("POST",value)
    #call the method to send the email 
    if visited:
        MailClient.send_mail(fromName,fromServer,toName,toServer,subjectVar,messageVar)

main()
