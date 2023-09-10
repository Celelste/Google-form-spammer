import requests
from formsubmissions import get_fields, prepare_payload


def get_mode(user_message, mode='none'):
    if user_message.startswith('nlink'):
        nlink = user_message[6:]
        nlink_data = get_fields(nlink)
        mode = 'nlink'
    if user_message.startswith('loop'):
        mode = 'loop'

    return mode
