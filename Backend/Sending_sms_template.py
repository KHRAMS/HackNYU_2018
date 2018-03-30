# @author Jinal Shah

# This is a sms test/template to send texts/sms:
# Twilio is a python package that can allow you to send text messages using code
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Your Account SID goes here"
# Your Auth Token from twilio.com/console
auth_token = "Your Auth Token Goes here"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="Number you have applied in twilio(should be your own cell phone number)",
    from_="twilio number",
    body="Hello from Python!")

print(message.sid)
