#! python3
# textMyself.py - Defines the textmyself() function that texts a message # passed to it as a string.
# Preset values:
accountSID = 'AC918fc60be1c5c45fa0a97f0b023cff93'
authToken = 'b0b44029703da808fc653c3eea6eb366'
myNumber = '+15559998888'
twilioNumber = '+15552225678'
from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
