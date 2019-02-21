import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("--------------")
    await client.change_presence(game=discord.Game(name='!도움말 ㄱㄱ', type=1))

@client.event
async def on_message(message):
    if message.content.startswith('!출석체크'):
        await client.send_message(message.channel, ":heart: 오늘도 출석체크 감사합니다 :heart: ")       
    if message.content.startswith('!'):
        await client.send_message(message.channel, " @~~ 테스트 ")  
    


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
