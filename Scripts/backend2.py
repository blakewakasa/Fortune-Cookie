from twilio.rest import Client
from datetime import datetime
from random import randrange
from collections import defaultdict
import time

global NUMBERS = {}

# Your Account Sid and Auth Token from twilio.com/user/account

'''
account_sid = "AC14ae6ec84d5319ffbddba8458e574c37"
auth_token = "59fd8fce33615e6113f03dbb5b12c69c"
client = Client(account_sid, auth_token)

message = client.messages.create(
        "+16502075480",
        body="Jenny please?! I love you <3",
        from_="+14243053286")


'''

def pick_random_time(begin:int, end:int) ->None:
    hour = randrange(begin,end+1)
    while datetime.now().hour() != hour:
        sleep(10)

    #run Luke's code
    
def store_numbers(number: str) ->None:
    if number not in NUMBERS.keys():
        NUMBERS[number] = set()
     
     
    
