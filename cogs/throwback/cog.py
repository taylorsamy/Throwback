from nextcord.ext import commands
import nextcord

class Throwback(commands.Cog, name="throwback"):
    """Receives ping commands"""

    COG_EMOJI = "🏓"

    def __init__(self, bot: commands.Bot):
        self._bot = bot

    @commands.command(hidden=True)
    async def throwback(self, ctx: commands.Context):
        """Checks for a response from the bot"""
        await ctx.send("I do things the old way")

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):

        if message.author.id != self._bot.user.id:
            if "ship" in message.content.lower() and "friendship" not in message.content.lower()\
            and "partnership" not in message.content.lower() and "companionship" not in message.content.lower():
                await message.channel.send(message.author.mention +  " Don't you mean token?") 
            if "colony" in message.content.lower():
                await message.channel.send(message.author.mention +  " Don't you mean base?")
            if "encounter" in message.content.lower():
                await message.channel.send(message.author.mention +  " Don't you mean challenge?")
            if "artifact" in message.content.lower():
                await message.channel.send(message.author.mention +  " Don't you mean edict?")
            if "hyperspace gate" in message.content.lower():
                await message.channel.send(message.author.mention +  " Don't you mean the cone?")
            if "compensation" in message.content.lower():
                await message.channel.send(message.author.mention +  " Don't you mean consolation?")
            if "negotiate" in message.content.lower():
                await message.channel.send(message.author.mention +  " Don't you mean compromise?")    

def setup(bot: commands.Bot):
    bot.add_cog(Throwback(bot))

