# -*- coding: utf-8 -*-
from wit import Wit

access_token = "SK7OGO5SDYGGQZG34VDWP7NVVH4IRQAO"

client = Wit(access_token)

def wit_response(message_text):
    intent = None
    entities = None
    confidence = None
    resp = client.message(message_text)
    print(resp)
    try:
        intent = resp["intents"][0]["name"]
        confidence = resp["intents"][0]["confidence"]
        entities = resp["entities"]
       
    except:
        pass
    return(intent, confidence, entities)

