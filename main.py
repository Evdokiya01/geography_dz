# Загрузите вспомогательную библиотеку https://www.twilio.com/docs/python/install

from twilio.rest import Client

# Ваш аккаунт Sid и Auth Token из twilio.com/console
account_sid = 'ACc3175e8475472fbbc2ab2147a250e8c'
auth_token = 'ec329c0176f329492929b11636f90a7'
client = Client(account_sid, auth_token)

call = client.calls.create(
                         twiml='<Response><Say>Ahoy, World!</Say></Response>',
                         to='+79152382813',
                         from_='+79852680091')

print(call.sid)