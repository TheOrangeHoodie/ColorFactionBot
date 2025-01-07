import dotenv
import nextcord
from nextcord.ext import commands

config = dotenv.dotenv_values("./.env")
intents = nextcord.Intents.all()
client = commands.Bot(intents=intents)

testGuilds = [1325892979646267404]

@client.event
async def on_ready():
    print("Logged in as:", client.user)

@client.slash_command(name="ping", description="Shows current latency", guild_ids=testGuilds)
async def ping(ctx: nextcord.Interaction):
    await ctx.response.send_message(f"Pong! Current latency: {round(client.latency * 1000)}ms")

client.run(config["TOKEN"])
