import discord
import time
import asyncio
import threading

def start(delay, tokens, module_status, serverid, channelid, ffmpeg, voicefile):
    global status
    status = True
    for token in tokens:
        loop = asyncio.new_event_loop()
        threading.Thread(target=voice_spam, args=(token, module_status, serverid, channelid, ffmpeg, voicefile, loop)).start()
        time.sleep(float(delay))

def voice_spam(token, module_status, serverid, channelid, ffmpeg, voicefile, loop):
    asyncio.set_event_loop(loop)
    class vcspam(discord.Client):
        async def on_connect():
            print("Send")
            target_guild = client.get_guild(int(serverid))
            voice_client = await target_guild.get_channel(int(channelid)).connect()
            if voice_client:
                module_status(2, 6, 1)
                voice_client.play(discord.FFmpegPCMAudio(
                    executable=ffmpeg, options="-af atempo=1.0,volume=20dB", source=(voicefile)), after=print("Done"))
                voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
            else:
                module_status(2, 6, 2)
                print('Unable to join.')
    client = vcspam()
    client.run(token)
    loop.run_until_complete(loop)