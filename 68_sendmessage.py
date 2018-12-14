from twilio.rest import Client
accountSID = 'AC918fc60be1c5c45fa0a97f0b023cff93'
authToken = 'b0b44029703da808fc653c3eea6eb366'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = '+8618535150344'
myCellPhone = '+8618535150344'
message = twilioCli.messages.create(body='Mr. Watson - Come here - I want to see you.', from_=myTwilioNumber, to=myCellPhone)
