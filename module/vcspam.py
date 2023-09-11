import discord
import sys
sys.dont_write_bytecode = True
import time
import asyncio
import threading
status = False

def start(delay, tokens, serverid, channelid, ffmpeg, voicefile):
    global status
    status = True
    for token in tokens:
        loop = asyncio.new_event_loop()
        threading.Thread(target=voice_spam, args=(token, serverid, channelid, ffmpeg, voicefile, loop)).start()
        time.sleep(float(delay))

def stop():
    global status
    status = False

def voice_spam(token, serverid, channelid, ffmpeg, voicefile, loop):
    global status
    asyncio.set_event_loop(loop)
    client = discord.Client()

    @client.event
    async def on_connect():
        print("Send")
        target_guild = client.get_guild(int(serverid))
        voice_client = await target_guild.get_channel(int(channelid)).connect()
        voice_client.play(discord.FFmpegPCMAudio(
            executable=ffmpeg, options="-af atempo=1.0,volume=20dB", source=(voicefile)), after=print("Done"))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
    client.run(token)
    loop.run_until_complete(loop)