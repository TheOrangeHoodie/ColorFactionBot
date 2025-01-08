import nextcord
from nextcord.ext import commands
import dbManager

admins = [883030668962066452]

class Admin(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.client = bot

    @nextcord.slash_command(name="factioncreate", description="Admin command to create a faction", guild_ids=[1325892979646267404])
    async def factionCreate(self,
                            ctx : nextcord.Interaction,
                            name: str = nextcord.SlashOption(name="name", description="Faction name"),
                            description: str = nextcord.SlashOption(name="description", description="Faction description"),
                            role: nextcord.Role = nextcord.SlashOption(name="role", description="Faction Role")
                            ):
        if ctx.user.id not in admins:
            await ctx.send("You dont have permissions to use this command! If this is a mistake contact TheOrangeHoodie aka Supreme")
            return
        
        confirmEmbed = nextcord.Embed(
            title=f"Faction: {name}",
            description=f"""Faction Description: {description}
                            Role: {role.mention}""",
            color=role.color
        )

        dbManager.addFaction(name, description, role.id)
        await ctx.send("Faction created!", embed=confirmEmbed)

        # try: 
            
        # except:
        #     print()
        #     await ctx.send("Internal error occured!")
        


    

def setup(bot):
    bot.add_cog(Admin(bot))
