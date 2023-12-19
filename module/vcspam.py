import sys

args = sys.argv
count = len(args) - 1

print(args) # ['commandArgs.py', 'apple', 'orange', 'banana']
print(type(args)) # <class 'list'>
print(count) # 3

import discord
import time
import asyncio
import threading

def start(delay, token, serverid, channelid, ffmpeg, voicefile):
    global status
    status = True
    loop = asyncio.new_event_loop()
    threading.Thread(target=voice_spam, args=(token, serverid, channelid, ffmpeg, voicefile, loop)).start()
    time.sleep(float(delay))

def voice_spam(token, serverid, channelid, ffmpeg, voicefile, loop):
    asyncio.set_event_loop(loop)
    class vcspam(discord.Client):
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
    client = vcspam()
    client.run(token)
    loop.run_until_complete(loop)
    
start(args[0],args[1],args[2],args[3],args[4],args[5])


import threading
import discord
import asyncio
from discord.ext import commands

async def login(token, serverid, channelid, ffmpeg, voicefile):
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

async def main(delay, token, serverid, channelid, ffmpeg, voicefile):
    tasks = []
    tasks.append(asyncio.create_task(login(delay, token, serverid, channelid, ffmpeg, voicefile)))
    await asyncio.gather(*tasks) 
    time.sleep(delay)
    
asyncio.run(start(args[0],args[1],args[2],args[3],args[4],args[5]))   