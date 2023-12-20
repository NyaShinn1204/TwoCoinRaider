import sys
import time
import discord
import asyncio
from discord.ext import commands

args = sys.argv

token_folder = args[1]
voicefile = args[5]
serverid = args[2]
channelid = args[3]
ffmpeg = args[4]
print(serverid)
print(channelid)

with open(token_folder,'r') as f:
    lines = []
    for line in f:
        lines.append(line.strip())

async def login(token):
    client = commands.Bot(command_prefix="!", self_bot=False)
    try:
        @client.event
        async def on_ready():
            print(f"Logges as {client.user}")
        @client.event
        async def on_connect():
            print("Send")
            target_guild = client.get_guild(int(serverid))
            voice_client = await target_guild.get_channel(int(channelid)).connect()
            if voice_client:
                print("Succsess Join")
                voice_client.play(discord.FFmpegPCMAudio(
                    executable=ffmpeg, options="-af atempo=1.0,volume=20dB", source=(voicefile)), after=print("Done"))
                voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
            else:
                print('Unable to join.')          
        await client.start(token)
    except:
        print("Failed to login: "+ token + "\n")
    finally:
        await client.close()

async def main():
    tasks = []
    for token in lines:
        tasks.append(asyncio.create_task(login(token)))
    await asyncio.gather(*tasks) 
    
asyncio.run(main())   