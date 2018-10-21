import os
import quoteRetriever
from flask import Flask, request
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

from twilio.twiml.voice_response import Gather, VoiceResponse, Say
import optionsJ
import stringSanitize

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

tik = ""
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


@app.route('/', methods=['GET', 'POST'])
def welcome():
  resp = VoiceResponse()
  resp.say("Welcome to StockBot, what stock would you like to know about?")
  resp.redirect("/exampleVoice")
  return str(resp)


@app.route('/exampleVoice', methods=['GET', 'POST'])
def exampleVoice():
    response = VoiceResponse()
    gather = Gather(input='speech', action='/printSpeech', method = 'GET', speechTimeout = 1)
    response.append(gather)
    return str(response)

@app.route('/printSpeech', methods=['GET', 'POST'])
def printSpeech():
    response = VoiceResponse()
    global tik
    s = request.args.get("SpeechResult")
    print(s)
    s = stringSanitize.stringClean(s)
    tik = s

    res, succ = quoteRetriever.getQuote(s)
    output = ""

    if succ:
      output = "Stock summary: " + str(res) #callinge external function based on request data
      response.say(output)
      response.redirect('/takeInput')
    else:
      output = "Couldn't find stock named" + str(s) + " . Please try again."
      response.say(output)
      response.redirect('/exampleVoice')

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

    gather = Gather(input='speech', action='/textParse', hints = "stock, options", method = 'GET', speechTimeout = 2)
    #resp.append(gather)

    #gather = Gather(num_digits=1, action = '/textParse', method = 'GET')
    gather.say('To check another stock, say stock. To check near the money options for this stock, say options.')
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/takeInput')

    return str(resp)

@app.route('/textParse', methods=['GET', 'POST'])
def textParse():
  response = VoiceResponse()
  #print(request.args['Digits'])

 # gather = Gather(action = '/')

  #print(request.args['Digits'] == "1")
  s = request.args.get("SpeechResult")
  print(s)
  print("WE printing here bois")

  if s == 'options':
    response.say('Some near the money options are: ')
    response.redirect('/handleOption')
  if s == 'stock':
    response.say('What stock would you like to know about?')
    response.redirect('/exampleVoice')
  else:
    response.say("Sorry but I do not recognize " + str(s) + " as a valid command. Try again.")
    response.redirect('/takeInput')

  return str(response)

@app.route('/handleOption', methods=['GET', 'POST'])
def handleOption():
  response = VoiceResponse()

  name, price = quoteRetriever.getTik()
  callList, putList = optionsJ.getNearMoneyOptions(optionsJ.getOptions(name), price)
  response.say(optionsJ.generateOptionsString(callList,putList))

  response.redirect('/takeInput')

  return str(response)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port, debug=True)
