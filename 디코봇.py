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
        await client.send_message(message.channel, "`아직 미게발이에용!(!출석체크)좀 부탁요`")    
    if message.content.startswith('!추석날 이밴트'):
        await client.send_message(message.channel, "`감사합니다 돈을 드릴게요.`:moneybag::moneybag::moneybag::moneybag::moneybag:`됐죠?`")
    if message.content.startswith('!펫 소환하기'):
        await client.send_message(message.channel, "펫은 무제한 소환가능합니다`kimeqmon이 나타낫다``잡을까?``말까`")     
    


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
