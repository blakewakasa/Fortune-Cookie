from twilio.rest import Client
from datetime import datetime
import random
from collections import defaultdict
import time
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('initial.html')

@app.route('/send', methods=['GET', 'POST'])
def parse_number():
    number = request.form["number"]
    print(number)
   
    return render_template('verify.html')

@app.route("/submit", methods=['GET', 'POST'])
def parse_code():
    code = request.form["code"]
    print(code)
    return render_template('settings.html')
    
NUMBERS = {}

KEY = 'AC14ae6ec84d5319ffbddba8458e574c37'
AUTH_TOKEN = '59fd8fce33615e6113f03dbb5b12c69c'

QUOTES = {"Try to be a rainbow in someone's cloud. - Maya Angelou",
          "Belive you can and you're halfway there. - Theodore Roosevelt",
          "If opportunity doesn't knock, build a door. - Milton Berle",
          "No matter how slow you go, you are still lapping everyone on the couch.",
          "It always gets better, just keep pressing forward.",
          "You can do it!",
          "Failure is only the opportunity to begin again. Only this time, more wisely. - Uncle Iroh",
          "It does not matter how slowly you go as long as you do not stop. - Confucius",
          "Good, better, best. Never let it rest. 'Til your good is better and your better is best. - St. Jerome",
          "Don't get lost in the sauce. - Usher",
          "You miss 100% of the shots you don’t take. –Wayne Gretzky",
          "Free is free. - Blake Wakasa",
          "You gotta constantly push. - Blake Wakasa",
          
          }

def send_message(phone: str):
    message = pick_message(phone)
    client = Client(KEY, AUTH_TOKEN)
    message = client.messages.create(
        phone,
        body=message,
        from_="+14243053286")
    
def pick_message(phone: str) -> str:
    if NUMBERS[phone] == QUOTES:
        NUMBERS[phone] = set()
    message = random.choice(QUOTES.difference(NUMBERS[phone]))
    NUMBERS[phone].add(message)
    return message

def store_numbers(number: str) ->None:
    if number not in NUMBERS.keys():
        NUMBERS[number] = set()

if __name__ == '__main__':
    app.run()
