import os, subprocess, threading
print("Welcome to Text Messenger!")

server = threading.Thread(target=subprocess.call,args=['python recieve_sms.py'])
server.start()

#load contacts
c = {}
#Uses a try and catch exception to handle files
try:
    file = open("contacts.txt","r")
    for line in file:
	#Gets the elements before and after the ',' and stores them in a dictionary
	#First part is for before the comma and second part is for getting after 
	#the comma to the length of the line minus the new line, which is 1 character
        c[line[:line.index(",")]]=line[line.index(",")+1:len(line)-1]
    file.close()
except:
    file = open("contacts.txt",'w')
    file.close()

def deleteContacts():
    response = input("Are you sure? Enter 'yes' to proceed. ")

    if response.lower()=="yes":
        file = open("contacts.txt",'w')
        file.close()
        c={}

def contact(name,number):
    file = open("contacts.txt","a")
    file.write(str(name)+","+str(number)+"\n")
    c[name]=number

#Twilio information to send to a number
def sendText(toNum):
    from twilio.rest import Client
    
    text = input("Message: ")

    # Your Account SID from twilio.com/console
    account_sid = "AC4c4e1052c676a72b5b92c7b8e7d5dd0b"
    # Your Auth Token from twilio.com/console
    auth_token  = "417430b4e40ba1a62c32d837315d0c63"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+"+str(toNum), 
        from_="+12563673601",
        body=text)

    #print(message.sid)
    print("Sent")
