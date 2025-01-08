import nextcord
from nextcord.ext import commands
import dbManager

admins = [883030668962066452, 1085807943087296553]

class PosterView(nextcord.ui.View):
    def __init__(self, factionInfo):
        super().__init__()
        self.value = None
        self.factionInfo = factionInfo

    @nextcord.ui.button(label="Join", style=nextcord.ButtonStyle.success)
    async def joinButton(self, button: nextcord.ui.Button, ctx: nextcord.Interaction):
        pass


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

        try: 
            dbManager.addFaction(name, description, role.id)
            await ctx.send("Faction created!", embed=confirmEmbed)
        except:
            print("Internal error! Its most likely invalid args")
            await ctx.send("Internal error occured!")

    @nextcord.slash_command(name="createposter", description="Admin command for creating a poster", guild_ids=[1325892979646267404])
    async def createPoster(self,
                           ctx: nextcord.Interaction,
                           factionName: str  = nextcord.SlashOption(name="factionname", description="Faction name to create poster for")):
        if ctx.user.id not in admins:
            await ctx.send("You dont have permissions to use this command! If this is a mistake contact TheOrangeHoodie aka Supreme")
            return
        
        try:
            factionInfo = dbManager.getFactionInfo(factionName)
        except IndexError as e:
            print(e)
            await ctx.send("Invalid faction name provided.")
            return

        view = PosterView(factionInfo)
        roleColor = ctx.guild.get_role(factionInfo["role"]).color
        embed = nextcord.Embed(
            title=f"FACTION: {factionInfo['name']}",
            description=factionInfo["description"],
            color=roleColor,
        ).set_footer(text="Made by The Color Kings")

        await ctx.send(content="", embed=embed, view=view)


    

def setup(bot):
    bot.add_cog(Admin(bot))
