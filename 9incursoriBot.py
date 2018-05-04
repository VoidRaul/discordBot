import discord
import asyncio
from discord.ext.commands import Bot



client = discord.Client()
#listenfor client new message
@client.event
async def on_message(message):
    if message.channel.id == channel_id_allenamento :
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return
        #check authority to post event
        if message.author.id == admin :
            if message.content.startswith('!create'):
                list=message.content.split('"')
                #just remove this two lines
                msg = list[1].format(message)
                msg=msg+"\n"+list[2].format(message)
                async for messages in client.logs_from(message.channel, limit=500):
                    await client.delete_message(messages)
                embed = discord.Embed(title=list[1]+" "+list[2], description=list[3], color=color_n)
                embed.add_field(name=presenze,value=0,inline=False)
                embed.add_field(name="Operatori", value="===========================================", inline=False)
                await client.send_message(message.channel, embed=embed)
        else:
            await client.delete_message(message)

    if message.channel.id == channel_id_evento :
        if message.content.startswith('!create'):
            #do something
            await client.delete_message(message)
        else:
            await client.delete_message(message)

#Commit#

#listen for message reaction
@client.event
async def on_reaction_add(reaction,user):
    #print(reaction.emoji)
    if (reaction.message.channel.id == channel_id_allenamento or reaction.message.channel.id == channel_id_evento) and reaction.emoji=='👌':
        for embeds in reaction.message.embeds:
            # print(embeds)
            embed = discord.Embed(title=embeds['title'], description=embeds['description'], color=color_n)
            for field in embeds['fields']:
                if field['name']==presenze:
                    embed.add_field(name=field['name'],value=reaction.count,inline=False)
                else:
                    embed.add_field(name=field['name'],value=field['value'],inline=False)
            embed.add_field(name=user.display_name, value='\u200b',inline=False)
            await client.edit_message(reaction.message,new_content=None,embed=embed)

#👌🏻
#listen for message reaction remove
@client.event
async def on_reaction_remove(reaction,user):
    if (reaction.message.channel.id == channel_id_allenamento or reaction.message.channel.id == channel_id_evento) and reaction.emoji=='👌':
        # print(reaction.emoji)
        for embeds in reaction.message.embeds:
            # print(embeds)
            embed = discord.Embed(title=embeds['title'], description=embeds['description'], color=color_n)
            for field in embeds['fields']:
                if (field['name']!=user.display_name and field['name']!=presenze):
                    embed.add_field(name=field['name'],value=field['value'],inline=False)
                if field['name']==presenze:
                    embed.add_field(name=field['name'],value=reaction.count,inline=False)
            await client.edit_message(reaction.message,new_content=None,embed=embed)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
