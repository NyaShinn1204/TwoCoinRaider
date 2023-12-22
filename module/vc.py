import time
import json
import asyncio
import discord
import websocket
import threading
from discord.ext import commands

def start(delay, tokens, module_status, serverid, channelid, type):
    global status
    status = True
    if type == "join":
        for token in tokens:
            threading.Thread(target=voice_join, args=(token, module_status, serverid, channelid, loop)).start()
            time.sleep(float(delay))
    if type == "leave":
        for token in tokens:
            loop = asyncio.new_event_loop()
            threading.Thread(target=voice_leave, args=(token, module_status, serverid, channelid, loop)).start()
            time.sleep(float(delay))

def voice_join(token, module_status, serverid, channelid, loop):
    asyncio.set_event_loop(loop)
    client = discord.Client()

    @client.event
    async def on_ready():
        print("Send")
        target_guild = client.get_guild(int(serverid))
        voice_client = await target_guild.get_channel(int(channelid)).connect()
        if voice_client:
            module_status(1, 3, 1)
            print(f'{client.user.name}#{client.user.discriminator} has connected to {voice_client}.')
            await voice_client.connect()
        else:
            module_status(1, 3, 2)
            print('Unable to leave.')
    client.run(token)
    loop.run_until_complete(loop)
        
def voice_leave(token, module_status, serverid, channelid, loop):
    asyncio.set_event_loop(loop)
    client = discord.Client()

    @client.event
    async def on_ready():
        print("Send")
        target_guild = client.get_guild(int(serverid))
        voice_client = await target_guild.get_channel(int(channelid)).connect()
        if voice_client:
            module_status(1, 4, 1)
            print(f'{client.user.name}#{client.user.discriminator} connected to {voice_client}. Disconnecting..')
            vc = await voice_client.connect()
            await vc.disconnect()
        else:
            module_status(1, 4, 2)
            print('Unable to leave.')
    client.run(token)
    loop.run_until_complete(loop)