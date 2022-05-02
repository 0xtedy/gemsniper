import discord
print("loading")
secret_token = "OTU0NzM4ODkyNzM5ODU4NDYy.YjXf4g.c3ssnmnFvavTssp-9B9mcVJYxV0"

client = discord.Client()

client.run(secret_token)
print("loading")

@client.event
async def on_ready():
    print("Le bot est prêt !")