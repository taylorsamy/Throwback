from nextcord.ext import commands
import nextcord

class Logging(commands.Cog, name="logging"):
    """Receives ping commands"""

    COG_EMOJI = "🏓"

    def __init__(self, bot: commands.Bot):
        self._bot = bot

    @commands.command(hidden=True)
    async def mention(self, ctx: commands.Context, member: nextcord.Member ):
        """Checks for a response from the bot"""
        await ctx.send(member.mention)

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
      if not message.author.bot:
        print(f"{message.author.name} said: {message.content}")
        if  '```' in message.content:
          print ('code')




def setup(bot: commands.Bot):
    bot.add_cog(Logging(bot))