from twilio.rest import Client
import urllib.request
import json

KEY = 'AC14ae6ec84d5319ffbddba8458e574c37'
AUTH_TOKEN = '59fd8fce33615e6113f03dbb5b12c69c'

quotes = {"Try to be a rainbow in someone's cloud.",
          "Belive you can and you're halfway there.",
          "If opportunity doesn't knock, build a door.",
          "No matter how slow you go, you are still lapping everyone on the couch.",
          "It always gets better, just keep pressing forward.",
          "You can do it.",
          "Failure is only the opportunity to begin again. Only this time, more wisely."}


def open_url(url: str) -> dict:
    '''returns a dict representing the json response of the given url'''
    response = urllib.request.urlopen(url)
    json_text = response.read().decode(encoding = 'utf-8')
    return json.loads(json_text)

def send_message(message: str, phone: str):
    client = Client(KEY, AUTH_TOKEN)
    message = client.messages.create(
        phone,
        body=message,
        from_="+14243053286")


