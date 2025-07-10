from flask import Flask, request, jsonify
from flask_cors import CORS
from DecoderBot import ChatBot
import json

app = Flask(__name__)
CORS(app)

@app.route('/chat')
def chat():
    msg = request.args.get('msg')
    return jsonify({"reply" : bot.get_random_response(msg)})

bot = ChatBot(name="Zen8", threshold=0.5)

def load_data():
	with open("brain.json", "r") as brain:
		return json.load(brain)

bot.train(load_data())
