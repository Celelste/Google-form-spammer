import requests
from form_requests import get_fields


def get_mode(user_message, mode='none'):
    response = ''
    if user_message.startswith('nlink'):
        nlink = user_message[6:]
        nlink_data = get_fields(nlink)
        response = 'creating new link process'
        mode = 'nlink'
    if user_message.startswith('loop'):
        response = 'Name of loop?'
        mode = 'loop'

    return mode, response
