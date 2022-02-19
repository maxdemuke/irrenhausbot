from discord.channel import VoiceChannel
from discord.ext import commands
import asyncio, discord

intents = discord.Intents.all()
prefix = "&"
client = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)
client.remove_command('help')
client.load_extension('cogs.main')
    

@client.event
async def on_ready():
    print('Bot is online.')
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name="im Irrenhaus"))

@client.command()
async def help(ctx):
    commands = '''
`&help` -> Zeigt dir dies.
Zeigt dir alle verfügbaren Befehle an und weitere relevante Informationen.

`&level` -> Zeigt dein Level an.
Du erhälst Level indem du Nachrichten auf dem Discord versendest.

`&giveaway <#channel> <gewinner> <Gewinn>` -> Startet ein Giveaway.
!!Nur für Teammitglieder nutzbar!!.
'''

    helpEmbed = discord.Embed(title='Hilfe', description=f'Alle verfügbaren Befehle:\n\n{commands}')

    await ctx.send(embed=helpEmbed)

# Run
client.run(open('token.txt').readline())