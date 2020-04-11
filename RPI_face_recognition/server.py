from face_recog_gui import *
import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def launch():
    speech_text = 'Welcome, you can say hello to start a conversation with me, or authenticate to start the authentication process.'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('HelloWorldIntent')
def Hello_World_Intent(status,room):
    speech_text = 'This is no time for a conversation. I have to complete the M P C A project. could you please say authenticate to start the authentication process.'
    return question(speech_text).reprompt(speech_text)

@ask.intent('AuthenticateIntent')
def Authenticate_Intent(status,room):
    app = App()
    app.mainloop()
    return statement('Thankyou for using the two step authentication system')
 
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement('Goodbye!')

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement('Goodbye! Event cancelled!')


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)

