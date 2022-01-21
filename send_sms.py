from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4c4e1052c676a72b5b92c7b8e7d5dd0b"
# Your Auth Token from twilio.com/console
auth_token  = "417430b4e40ba1a62c32d837315d0c63"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17325756420", 
    from_="+12563673601",
    body="hello new world"
)
