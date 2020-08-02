import os, sys
from flask import Flask, request
from pymessenger import Bot
from chatbot import db_response

app = Flask(__name__)
PAGE_ACCESS_TOKEN = "EAARXIlrZAsQ8BAFsPZBIZBbJhMt21HZAvAnXu9FAsZC3U5siwlFkUeg5NtWpZAQZBaqjZAlQdah5tbuBGivf8HTOAH3tks9xZBUVI2UOkt5jrv6DEzn7nKXcCahlmzGtQjNZAgVc5HGyTlZC8ZAslBbrdusQ1sdNgxWhFFXhbI7BZAjYlKgZDZD"
fb = Bot(PAGE_ACCESS_TOKEN)

@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == "hello":
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    user_request = None
    id_sender = None
    response = None
    data = request.get_json()
    log(data)

    id_sender = data["entry"][0]["messaging"][0]["sender"]["id"]
    try:
        user_request = data["entry"][0]["messaging"][0]["message"]["text"]
        response = db_response(user_request)
    except:
        response = "Non ho capito"
    fb.send_text_message(id_sender, response)
    return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()

if __name__ == "__main__":
    app.run(debug = True, port = 80)   
  
