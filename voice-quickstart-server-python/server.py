import os
from flask import Flask, request
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

from twilio.twiml.voice_response import Gather, VoiceResponse, Say


ACCOUNT_SID = 'AC8de93a520b00a4cf5cdae9c5d28989b8'
API_KEY = 'SKcc80d07d4a30523fd2d02a67646de63b'
API_KEY_SECRET = 'h6D7ve022JoKC3Hz91AmdI1RLb6fvAtH'
PUSH_CREDENTIAL_SID = 'CR***'
APP_SID = 'AP769dda7c8d0845f08e2d095dbbd59700'

"""
Use a valid Twilio number by adding to your account via https://www.twilio.com/console/phone-numbers/verified
"""
CALLER_NUMBER = '1234567890'

"""
The caller id used when a client is dialed.
"""
CALLER_ID = 'client:quick_start'
IDENTITY = 'alice'


app = Flask(__name__)

"""
Creates an access token with VoiceGrant using your Twilio credentials.
"""
@app.route('/accessToken', methods=['GET', 'POST'])
def token():
  account_sid = os.environ.get("ACCOUNT_SID", ACCOUNT_SID)
  api_key = os.environ.get("API_KEY", API_KEY)
  api_key_secret = os.environ.get("API_KEY_SECRET", API_KEY_SECRET)
  push_credential_sid = os.environ.get("PUSH_CREDENTIAL_SID", PUSH_CREDENTIAL_SID)
  app_sid = os.environ.get("APP_SID", APP_SID)

  grant = VoiceGrant(
    push_credential_sid=push_credential_sid,
    outgoing_application_sid=app_sid
  )

  identity = request.values["identity"] \
          if request.values and request.values["identity"] else IDENTITY
  token = AccessToken(account_sid, api_key, api_key_secret, identity=identity)
  token.add_grant(grant)

  return token.to_jwt()

"""
Creates an endpoint that plays back a greeting.
"""
@app.route('/incoming', methods=['GET', 'POST'])
def incoming():
  resp = VoiceResponse()
  resp.say("Congratulations! You have received your first inbound call! Good bye.")
  return str(resp)


@app.route('/', methods=['GET', 'POST'])
def welcome():
  resp = VoiceResponse()
  resp.say("Welcome to Twilio")
  return str(resp)


@app.route('/exampleVoice', methods=['GET', 'POST'])
def exampleVoice():
    response = VoiceResponse()
    gather = Gather(input='speech', action='/printSpeech', method = 'GET', speechTimeout = 2)

    gather.say('Welcome to Twilio, please tell us why you\'re calling')
    response.append(gather)
    #response.say(gather)
    #print(response)
    return str(response)

@app.route('/printSpeech', methods=['GET', 'POST'])
def printSpeech():
    response = VoiceResponse()

    print(request.args.get("SpeechResult"))

    output = "some output" #callinge external function based on request data

    response.say(output)

    response.say("Do you want to check another stock? Press the pound sign.")

    response.redirect('/takeInput')
    return str(response)

# @app.route('/takeInput', methods = ['GET', 'POST'])
# def takeInput():
#     resp = VoiceResponse()
#     gather = Gather(num_digits=1, action = '/textParse', method = 'GET', timeout = 5)
#     return str(resp)

@app.route("/takeInput", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a menu of options"""
    # Start our TwiML response
    resp = VoiceResponse()

    # Start our <Gather> verb
    gather = Gather(num_digits=1, action = '/textParse', method = GET)
    gather.say('For sales, press 1. For support, press 2.')
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/takeInput')

    return str(resp)

@app.route('/textParse', methods=['GET', 'POST'])
def textParse():
  response = VoiceResponse()
  print(request.args + "Poundededded")
  return str(response)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
