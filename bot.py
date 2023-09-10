import discord
import responses
from config import *
from concurrent.futures import ProcessPoolExecutor

mode = 'none'


def whileloop():
    while True:
        print('looping')


def set_mode(message, user_message, is_private):
    try:
        response = responses.get_mode(user_message)
        return response
    except Exception as e:
        print(e)


def run_bot():
    intents = discord.Intents().all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')
        print(f'invite bot with {invite_link}')

    @client.event
    async def on_message(message):
        global mode
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)

        if user_message[0:3] == 'sp.':
            user_message = user_message[3:]
            print(user_message)
            mode = set_mode(message, user_message)

    client.run(Token)
