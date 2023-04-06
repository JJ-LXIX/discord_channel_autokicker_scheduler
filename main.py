import discord
import asyncio
import datetime

TOKEN = 'Enter your server ID here'
KICK_TIME = datetime.time(13, 18, 0)

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

indianTimeZone = pytz.timezone("Asia/Kolkata")

async def kick_users():
    now = datetime.datetime.now(indianTimeZone).time()
    if now >= KICK_TIME:
        for voice_channel in client.get_all_channels():
            if isinstance(voice_channel, discord.VoiceChannel):
                voice_states = voice_channel.voice_states
                for member_id in voice_states.keys():
                    member = voice_channel.guild.get_member(member_id)
                    if member is not None:
                        await member.edit(voice_channel=None)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name='the Boys'))
    while True:
        await kick_users()
        await asyncio.sleep(60)  # Check every minute

client.run(TOKEN)


