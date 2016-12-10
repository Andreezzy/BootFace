import requests
import json

from structs import typing_message, text_message

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



def call_send_API( data, token ):
	res = requests.post('https://graph.facebook.com/v2.6/me/messages',
					params = {'access_token': token },
					data = json.dumps(data),
					headers = { 'Content-type': 'application/json' }
					)
	if res.status_code == 200:
		print("El mensaje fue enviado exitosamente!")