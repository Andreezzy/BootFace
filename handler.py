

def recived_message(event):
	sender_id = event['sender']['id']
	recipient_id = event['recipient']['id']
	time_message = event['timestamp']
	message = event['message']
	text = message['text']

	print(sender_id)
	print(recipient_id)
	print(time_message)
	print(message)
	print(text)