from nextcord.ext import commands
import nextcord

class PingDylan(commands.Cog, name="PingDylan"):
    """Receives ping commands"""

    COG_EMOJI = "🏓"

    def __init__(self, bot: commands.Bot):
        self._bot = bot

    @commands.command(hidden=True)
    async def pingDylan(self, ctx: commands.Context, member: nextcord.Member ):
        """Checks for a response from the bot"""
        await ctx.send(member.mention)

def setup(bot: commands.Bot):
    bot.add_cog(PingDylan(bot))