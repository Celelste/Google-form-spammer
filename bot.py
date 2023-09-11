import discord
import responses
from config import *
from multiprocessing import *
from time import sleep

mode = 'none'
loop = True

executor = {}


def whileloop(name):
    while True:
        sleep(1)
        print(f'looping {name}')


async def send_message(message, response, is_private):
    if is_private:
        await message.author.send(response)
    else:
        await message.channel.send(response)


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
        global mode, executor
        if message.author == client.user:
            return
        user_message = str(message.content)

        if user_message == 'cancel':
            mode = 'none'
            await send_message(message, 'cancelled', is_private=True)

            return

        if user_message[0:3] == 'sp.':
            user_message = user_message[3:]
            mode, response = set_mode(message, user_message, is_private=True)
            await send_message(message, response, is_private=True)

            return

        print(mode, user_message)

        if user_message.startswith('stop'):
            current_proc = user_message[5:]
            print(current_proc)
            if current_proc in executor:
                executor[current_proc].terminate()
                del executor[current_proc]
                await send_message(message, f'terminated process {current_proc}', is_private=True)
            else:
                await send_message(message, f'no such process {current_proc}', is_private=True)

            return

        if mode == 'loop':
            executor[user_message] = Process(target=whileloop, args=user_message)
            executor[user_message].start()
            await send_message(message, f'looping as {user_message}', is_private=True)
            mode = 'none'

            return

    client.run(Token)
