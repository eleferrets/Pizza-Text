import os, random, threading, random
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse

app = Flask(__name__)

@app.route("/sms",methods=['GET','POST'])

def sms_reply():
    resp = MessagingResponse()

    resp.message("Response.")
        
    
    #resp.message("Working")
    print("Working")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
