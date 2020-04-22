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
    embed.add_field(name='Rank:', value=role, inline=True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text='Made by Rogue#2208')

    await ctx.channel.send(embed=embed)

@bot.command()
async def ban(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        embed = discord.Embed(name='You cannot ban yourself!', description='Why would you even want to?')
        embed.set_footer(text='Made by Rogue#2208')
        
        await ctx.channel.send(embed=embed)
        return

    if reason == None:
        reason = 'no reason at all!'

    embed = discord.Embed(name=f'{member} has been banned!', description=f'For: {reason}')
    embed.set_footer(text='Made by Rogue#2208')

    message = f'You have been banned from {ctx.guild.name} for {reason}!'
    await member.send(message)
    await ctx.guild.ban(member)
    await ctx.channel.send(embed=embed)

@bot.command()
async def kick(ctx, member:discord.User = None, reason = None):
    if member == None or member == ctx.message.author:
        embed = discord.Embed(title=config.botname)
        embed.add_field(name='You cannnot kick youself!')
        embed.set_footer(text='Made by Rogue#2208')
        
        await ctx.channel.send(embed=embed)
        return

    if reason == None:
        reason = 'no reason at all!'

    embed = discord.Embed(title=config.botname)
    embed.add_field(name=f'Kicked: {member}', value=f'For: {reason}')
    embed.set_footer(text='Made by Rogue#2208')

    message = f'You have been kicked from {ctx.guild.name} for {reason}!'
    await member.send(message)
    await ctx.guild.kick(member)
    await ctx.channel.send(embed=embed)

@bot.command()
async def botinfo(ctx):
    embed = discord.Embed(title=config.botname)
    embed.add_field(name='Prefix', value=config.prefix)
    embed.add_field(name='Logging', value='True')
    embed.set_footer(text='Made by Rogue#2208')

    await ctx.channel.send(embed=embed)

@bot.command()
async def sourcecode(ctx):
    embed = discord.Embed(title='CustomBOT')
    embed.add_field(name='GitHub', value='https://www.github.com/RogueSoldier777/CustomBOT.')
    embed.set_footer(text='Made by Rogue#2208')

    await ctx.channel.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    textchannels = len(ctx.guild.channels) - len(ctx.guild.voice_channels)

    embed = discord.Embed(title=ctx.guild.name)
    embed.add_field(name='Name:', value=ctx.guild.name, inline=True)
    embed.add_field(name='Members:', value=ctx.guild.member_count)
    embed.add_field(name='Owner:', value=ctx.guild.owner, inline=True)
    embed.add_field(name='Server ID:', value=ctx.guild.id)
    embed.add_field(name='Channels:', value=len(ctx.guild.channels))
    embed.add_field(name='Text Channels:', value=textchannels)
    embed.add_field(name='Voice Channels:', value=len(ctx.guild.voice_channels))

    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_footer(text='Made by Rogue#2208')

    await ctx.channel.send(embed=embed)


bot.run(config.token)