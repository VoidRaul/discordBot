import discord
import asyncio
from discord.ext.commands import Bot

TOKEN = 'NDQxMzQ4MDk1NTU3NjMyMDAw.Dcu98g.09SoVd-Ln67DAYVFkwixBcBIXYE'
admin ='185020327133184000'

channel_id_allenamento='441370906602766350'
channel_id_evento='441261743549972493'

client = discord.Client()

@client.event
async def on_message(message):
    if message.channel.id == channel_id_allenamento or message.channel.id == channel_id_evento :

        # we do not want the bot to reply to itself
        if message.author == client.user:
            return
        #check authority to post event
        if message.author.id == admin :
            if message.content.startswith('!create'):
                list=message.content.split()
                print(list[1])
                msg = list[1].format(message)
                async for message in client.logs_from(message.channel, limit=500):
                    await client.delete_message(message)
                await client.send_message(message.channel, msg)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
