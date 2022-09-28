import os
try:
    import discord
except:
    os.system("pip install discord")
    import discord

#Configs
prefix = "!"
bot_token = "[TOKEN]"


#Discord Client
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot started. Logged in on Discord BOT Client as {client.user}.')
    activity = discord.Game(name=prefix+"clean")
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix+"clean"):
        await command_clean(message,client)
            
#Commands
async def command_clean(message,client):
    if not message.author.guild_permissions.administrator:
        await message.channel.send("Permission insuffisante.")
        return
    await message.channel.send("Starting to clean raider...")

    kick_list = []
    for member in message.guild.members:
        passed = False
        try:
            if len(member.roles) > 0:
                if len(member.roles) == 1:
                    if not member.roles[0].is_default():
                        passed = True
                else:
                    passed = True
        except:
            pass
        if not passed:
            kick_list.append(member)

    if len(kick_list)>0:
        await message.channel.send("Preparing to kick {} raiders".format(len(kick_list)))
        for raider in kick_list:
            try:
                await raider.kick()
                await message.channel.send("Kicked "+raider.display_name)
            except:
                await message.channel.send("Failed to kick "+raider.display_name)
    else:
        await message.channel.send("No raider detected to kick")
                
            

# Run the bot
client.run(bot_token)
