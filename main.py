import discord, config
from discord.ext import commands

print(f'Loading {config.botname}...')
bot = commands.Bot(command_prefix=config.prefix, status=discord.Status.idle, activity=discord.Game(name='Booting...'))

bot.remove_command('help')

@bot.event
async def on_ready():
    servers = len(bot.guilds)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f'Currently serving: {servers} servers!'))

    if servers == 0:
        print(f'Hi! My name is: {config.botname}!')
        print("Looks like I'm in no servers :( Try add me to yours at: https://www.discordapp.com/developers/applications/me")
    if servers == 1:
        print(f'Hi! My name is: {config.botname}!')
        print('I am currently in one server! Talk about loyalty!')
    if servers > 1:
        print(f'Hi! My name is: {config.botname}!')
        print(f'I am currently in {servers} servers!')

@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    embed=discord.Embed(title="Pong!", description=f"This took: `{ping}ms`!")
    embed.set_footer(text="Made by Rogue#2208")
    await ctx.channel.send(embed=embed)

@bot.command()
async def user(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.message.author
        pronoun = 'Your'
    else:
        pronoun = 'Their'
    
    name = f'{member.name}#{member.discriminator}'
    status = member.status
    joined = member.joined_at
    role = member.top_role

    embed = discord.Embed(tite='User Info', description=f"Here's what I could find on {member.name}")
    embed.add_field(name='Name:', value=member.name, inline=True)
    embed.add_field(name='Status:', value=status, inline=True)
    embed.add_field(name='Joined At:', value=joined, inline=True)
    embed.set_footer(text='Made by Rogue#2208')
    embed.add_field(name='Rank:', value=role, inline=True)

    await ctx.channel.send(embed=embed)

bot.run(config.token)