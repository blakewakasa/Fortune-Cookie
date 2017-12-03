from twilio.rest import Client
from datetime import datetime
from flask import Flask, render_template
from collections import defaultdict
import json
import urllib.parse
import urllib.request
import random

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
VERIFY_KEY = "0dCWkbZaBsyYf6Dq1uDxfhZfiAlZ2t9i"
def build_verification_url():
    response = urllib.request.request("https://api.authy.com/protected/json/phones/verification/start?api_key="+VERIFY_KEY)
    json_text = response.read().decode(encoding = 'utf-8')
    return json.loads(json_text)


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




if __name__ == "__main__":
    build_verification_url()
