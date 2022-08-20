from nextcord.ext import commands
import nextcord
import asyncio, random

class Throwback(commands.Cog, name="throwback"):
    """Receives ping commands"""

    COG_EMOJI = "🏓"
    

    def __init__(self, bot: commands.Bot):
        self._bot = bot
        self.__cooldown = []

    @commands.command(hidden=True)
    async def throwback(self, ctx: commands.Context):
        """Checks for a response from the bot"""
        await ctx.send("I do things the old way")

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):

        if message.author.id != self._bot.user.id:
            items = []
            if " ship" in message.content.lower() or message.content.startswith("ship"):
                if "ships" in message.content.lower():
                    items.append("tokens")
                else:
                    items.append("token")
            if "colony" in message.content.lower():
                if "colonies" in message.content.lower():
                    items.append("bases")
                else:
                    items.append("base")
            if "encounter" in message.content.lower():
                if "encounters" in message.content.lower():
                    items.append("challenges")
                else:
                    items.append("challenge")
            if "artifact" in message.content.lower():
                if "artifacts" in message.content.lower():
                    items.append("edicts")
                else:
                    items.append("edict")
            if "hyperspace gate" in message.content.lower():
                items.append("cone")
            if "compensation" in message.content.lower():
                items.append("consolation")
            if "negotiate" in message.content.lower():
                items.append("compromise")

            if items and self.__cooldown.count(message.author.id) < 1:
                # exit 25% of the time
                if random.randint(1, 4) == 1:
                    return
                
                response = "Don't you mean " + ", ".join(items) + "?"
                await message.channel.send(response)
                self.__cooldown.append(message.author.id)
                await asyncio.sleep(300)
                self.__cooldown.remove(message.author.id)
                # print (response)

            


def setup(bot: commands.Bot):
    bot.add_cog(Throwback(bot))

