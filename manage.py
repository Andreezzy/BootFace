import os
from flask import Flask
from flask import request

import json
from config import DevelopmentConfig

from handler import recived_message

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/webhook', methods = ['GET'])
def webhook():
	if request.method == 'GET':
		verify_token = request.args.get('hub.verify_token', '')
		if verify_token == app.config['SECRET_KEY']:
			return request.args.get('hub.challenge', '')
		return 'Error'
	elif request.method == 'POST':
		payload = request.get_data()
		data = json.loads(payload)

		for page_entry in data['entry']:
			for message_event in page_entry['messaging']:
				if 'message' in message_event:
					recived_message(message_event, app.config['SECRET_KEY'])
					#evento = message_event['message']
					#print(evento['text'])
		return "ok"

@app.route('/', methods = ['GET'])
def index():
	return "text"

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)