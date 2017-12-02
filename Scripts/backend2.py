from twilio.rest import Client
from datetime import datetime
from flask import flask
from collections import defaultdict

import random
app = Flask(__name__)
NUMBERS = {}
#DAYS_TO_INTS = {"Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3,"Friday":4, "Saturday":5, "Sunday":6}

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

def pick_random_time(begin:int, end:int, dayStart:str) ->None:
    DAYS_TO_INTS = {"Monday":0, "Tuesday":1, "Wednesday":2,
                    "Thursday":3,"Friday":4, "Saturday":5, "Sunday":6} #set of days that converts it to ints for datetime
    while True:
        if DAYS_TO_INTS[dayStart] == datetime.now().weekday():
            hour = random.randrange(begin,end+1)
            while datetime.now().hour() != hour:
                sleep(30)


    #run Luke's code

    
def store_numbers(number: str) ->None:
    if number not in NUMBERS.keys():
        NUMBERS[number] = set()
    
