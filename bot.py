from discord.ext import commands
import discord
from os import system
import json
import psycopg2


#custom prefix fetch
"""
def getPrefix(self, message):
    gid = message.guild.id
    with open("keys.json", "r") as pp:
        db = psycopg2.connect(host="localhost",database="villagerbot", user="pi", password=json.load(pp)["postgres"])
    cur = self.db.cursor()
    cur.execute("SELECT prefix FROM prefixes WHERE prefixes.id='"+str(gid)+"'")
    prefix = cur.fetchone()
    if str(type(prefix)) == "<class 'NoneType'>" or str(type(prefix)) == "NoneType":
        cur.execute("INSERT INTO prefixes VALUES ('"+str(gid)+"', '!!')")
        prefix = ('!!',)
    return str(prefix[0])
"""

bot = commands.AutoShardedBot(command_prefix="!!", help_command=None, case_insensitive=True)
cogs = ["cmds", "events", "owner", "msgs",
        "admincmds", "currency", "loops",
        "xenon", "idk"]

#load cogs in cogs list
for cog in cogs:
    bot.load_extension("cogs."+cog)

@bot.check
async def stay_safe(ctx):
    if not bot.is_ready():
        await ctx.send(embed=discord.Embed(color=discord.Color.green(), description="Hold on! Villager Bot is still starting up!"))
        return False
    return ctx.message.author.id is not 639498607632056321 and not ctx.message.author.bot

#actually start bot
key = json.load(open("keys.json", "r"))["discord"]
bot.run(key, bot=True)