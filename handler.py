import requests
import json

def recived_message(event, token):
	sender_id = event['sender']['id']
	recipient_id = event['recipient']['id']
	time_message = event['timestamp']
	message = event['message']
	text = message['text']

	typing = typing_message(sender_id)
	call_send_API(typing, token)

	message = text_message(sender_id, text)
	call_send_API(message, token)

def typing_message(recipient_id):
	message_data = {
		'recipient': { 'id' : recipient_id },
		'sender_action' : 'typing_on'
	}
	return message_data

def text_message(recipient_id, message_text):
	message_data = {
		'recipient': { 'id' : recipient_id },
		'message' : { 'text' : message_text }
	}
	return message_data

def call_send_API( data, token ):
	res = requests.post('https://graph.facebook.com/v2.6/me/messages',
					params = {'access_token': token },
					data = json.dumps(data),
					headers = { 'Content-type': 'application/json' }
					)
	if res.status_code == 200:
		print("El mensaje fue enviado exitosamente!")