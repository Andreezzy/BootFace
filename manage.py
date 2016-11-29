import os
from flask import Flask
from flask import request

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/webhook', methods = ['GET'])
def webhook():
	print(app.config['SECRET_KEY'])
	very_token = request.args.get('hub.very_token', '')
	if very_token == app.config['SECRET_KEY']:
		return request.args.get('hub.challenge', '')
	return 'Error'

@app.route('/', methods = ['GET'])
def index():
	return "text"

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)