import dotenv
import nextcord
from nextcord.ext import commands
import os

config = dotenv.dotenv_values("./.env")
intents = nextcord.Intents.all()
client = commands.Bot(intents=intents, command_prefix="o!")

# On start
@client.event
async def on_ready():
    print("Logged in as:", client.user)

# Loading the cogs
for fn in os.listdir("./modules"):
    if fn.endswith(".py"):
        client.load_extension(f"modules.{fn[:-3]}")

@client.command()
async def load(ctx, extenstion):
    if not ctx.author.id == 883030668962066452:
        ctx.send("You dont have permissions to use this command!")
        return
    client.load_extension(extenstion)
    await ctx.send(f"Loaded extension: {extenstion}")

@client.command()
async def unload(ctx, extenstion):
    if not ctx.author.id == 883030668962066452:
        ctx.send("You dont have permissions to use this command!")
        return
    client.unload_extension(extenstion)
    await ctx.send(f"Unloaded extension: {extenstion}")

@client.command()
async def reload(ctx, extenstion):
    if not ctx.author.id == 883030668962066452:
        ctx.send("You dont have permissions to use this command!")
        return
    client.reload_extension(extenstion)
    await ctx.send(f"Reloaded extension: {extenstion}")



client.run(config["TOKEN"])
