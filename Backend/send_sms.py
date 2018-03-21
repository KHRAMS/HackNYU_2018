# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC6dbc3c285f3007f66e6620e6ee692436"
auth_token = "3a9afd3d87f73426240b38fcc6b7a4c7"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+16099554715",
    from_="+12678438073",
    body="Test")
