# -*- coding: utf-8 -*-
from wit import Wit

access_token = "SK7OGO5SDYGGQZG34VDWP7NVVH4IRQAO"

client = Wit(access_token)

def wit_response(message_text):
    resp = client.message(message_text)
 
    try:
        intent = resp["intents"][0]["name"]
        entities = resp["entities"]
       
    except:
        pass
    return(intent, entities)

