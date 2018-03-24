# @author Jinal Shah

# This is a sms test/template to send texts/sms:
# Twilio is a python package that can allow you to send text messages using code
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3e39b9c7a3716c1cbd1c5e41f326b9eb"
# Your Auth Token from twilio.com/console
auth_token = "2eb462c692c1a5e88ff2ac6cb0d2217a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16099550141",
    from_="+12674940562",
    body="Hello from Python!")

print(message.sid)
