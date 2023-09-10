import requests
from formsubmissions import get_fields, get_payload

def get_response(user_message):
    if user_message.startswith("https://docs.google.com/forms/"):
        get_fields(user_message)
