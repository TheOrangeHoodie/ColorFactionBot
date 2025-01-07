import nextcord
from nextcord.ext import commands
from dotenv import dotenv_values

class Tests(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.client = bot

    @commands.command()
    async def ping(self, ctx: nextcord.Interaction):
        await ctx.send(f"🏓 Pong! Current latency: {round(self.client.latency * 1000)}ms")

def setup(bot):
    bot.add_cog(Tests(bot))
