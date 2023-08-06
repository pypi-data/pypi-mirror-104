
# PYTHON ORANGE SMS GATE WAY

Orange provides API to send SMS to some countries around the world, but using the API may take you a few hours.


if you are python developer don't waste your time use our package to save time


## INSTALL

```sh
pip install python-orange-sms
```

## GET CREDENTIALS

1. Go to https://developer.orange.com/ and login or create a new account

2. Go to **my apps**
   
3. Selecte your app or create a new **app**
   
4. Get your  **Client ID**

## USAGE

```py
from python_orange_sms import utils

AUTH_TOKEN = 'Client ID' #  Client ID from orange
message = "Your Message" # Your message
to='+243xxxxxxxxx' # Receiver
from_='+243xxxxxxxxx' # Sender (your phone number)

sms = utils.SMS(AUTH_TOKEN)
res = sms.send(from_=from_, to=to, message=message)

print(res)  

if res.status_code == 201:
    print('AVERY THING RIGHT : ', res.text) # SMS sent
else:
    print('SAME THING WRONG')
```