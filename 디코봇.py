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
    if message.content.startswith('!도움말'):
        await client.send_message(message.channel, "`아직 미게발이에용!(!출석체크)좀 해주세요           `")    
    if message.content.startswith('!도움말'):
        await client.send_message(message.channel, "`(!펫 구워먹기           `")    
    if message.content.startswith('!펫 구워먹기'):
        await client.send_message(message.channel, "진짜 있는줄 암? ㅋㅋㅋ 여윽시 초딩임 ㅋㅋㅋ")  
    if message.content.startswith('!도움말'):
        await client.send_message(message.channel, "`           `")   
    if message.content.startswith('!도움말'):
        await client.send_message(message.channel, "`           `")
    if message.content.startswith('!도움말'):
        await client.send_message(message.channel, "`           `")
    if message.content.startswith('!도움말'):
        await client.send_message(message.channel, "`           `")
    if message.content.startswith('!도움말'):
        await client.send_message(message.channel, "`           `")
    if message.content.startswith('!도움말'):
        await client.send_message(message.channel, "`           `")
    if message.content.startswith('!도움말'):
        await client.send_message(message.channel, "`by,adadadwsx`")    
    


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
