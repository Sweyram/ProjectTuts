from trello import TrelloClient
from flask import Flask, request,redirect
from twilio.twiml.messaging_response import MessagingResponse
import random


app = Flask(__name__)

if __name__ == "__main__":
	app.run(debug=True)
