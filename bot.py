import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
    except Exception as e:
        print(e)


def run_bot():
    TOKEN = 'MTAyOTEzNzQyMTc5NjkwNTAwMA.G_Ir2B.8NMh6UKzNZwVuxz5m7WrdkATQSrPEiz6GcoaKc'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, True)
        else:
            await send_message(message, user_message, False)
    client.run(TOKEN)
