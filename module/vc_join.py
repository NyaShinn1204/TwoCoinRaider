import time
import websocket
import threading

video = True
mic_mute = True
speaker_mute = True
keep = True

status = True

def status():
    global status
    return status

def stop():
    global status
    status = False

def start(delay, tokens, module_status, serverid, channelid):
    global status
    status = True
    for token in tokens:
        if status:
            threading.Thread(target=join_vc, args=(token, module_status, serverid, channelid, video, mic_mute, speaker_mute, keep)).start()
            if not keep:
                time.sleep(0.1)
        else:
            break

def join_vc(token, module_status, serverid, channelid, video, mic_mute, speaker_mute, keep):
    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?encoding=json&v=9&compress=zlib-stream")
    ws.send(f'{{"op":2,"d":{{"token":"{token}","capabilities":16381,"properties":{{"os":"Windows","browser":"Chrome","device":"","system_locale":"ja","os_version":"10","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_event_source":null}},"presence":{{"status":"online","since":0,"activities":[],"afk":false}},"compress":false,"client_state":{{"guild_versions":{{}},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1,"private_channels_version":"0","api_code_version":0}}}}}}')
    ws.send(f'{{"op":4,"d":{{"guild_id":"{serverid}","channel_id":"{channelid}","self_mute":{mic_mute},"self_deaf":{speaker_mute},"self_video":{video},"flags":2}}}}'.replace('True','true').replace('False','false'))