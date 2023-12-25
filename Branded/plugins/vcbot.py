from .. import *
from ..modules.func import *
from ..modules.utils import *

from pyrogram import *
from pytgcalls import StreamType
from pytgcalls.types.input_stream import *
from pytgcalls.types.input_stream.quality import *


# Audio Stream
@app.on_message(commandz(["ply", "play"]) & SUDOERS)
async def audio_stream(client, message):
    chat_id = message.chat.id
    replied = message.reply_to_message
    audio = (
        (replied.audio or replied.voice or
        replied.video or replied.document)
        if replied else None
    )
    m = await eor(message, "** Processing ...**")
    try:
        if audio:
            await m.edit("** Downloading ...**")
            file = await replied.download()
        else:
            if len(message.command) < 2:
                 return await m.edit("** Give Some Query ...**")
            text = message.text.split(None, 1)[1]
            if "?si=" in text:
                query = text.split("?si")[0]
            else:
                query = text
            await m.edit("** Searching ...**")
            search = get_youtube_video(query)
            stream = search[0]
            file = await get_youtube_stream(stream)
        await m.edit("** Processing ...**")
        check = db.get(chat_id)
        if not check:
            await call.join_group_call(
                chat_id,
                AudioPiped(
                    file,
                    HighQualityAudio(),
                ),
                stream_type=StreamType().pulse_stream
            )
            await put_que(chat_id, file, "Audio")
            await m.edit("** Streaming Started!**")
            await m.delete()
        else:
            pos = await put_que(chat_id, file, "Audio")
            await m.edit(f"** Added To Queue #{pos}**")
            await m.delete()
    except Exception as e:
        await m.edit(f"**Error:** `{e}`")

  
# Video Stream
@app.on_message(commandz(["vply", "vplay"]) & SUDOERS)
async def video_stream(client, message):
    chat_id = message.chat.id
    replied = message.reply_to_message
    video = (
        (replied.audio or replied.voice or
        replied.video or replied.document)
        if replied else None
    )
    m = await eor(message, "** Processing ...**")
    try:
        if video:
            await m.edit("** Downloading ...**")
            file = await replied.download()
        else:
            if len(message.command) < 2:
                 return await m.edit("** Give Some Query ...**")
            text = message.text.split(None, 1)[1]
            if "?si=" in text:
                query = text.split("?si")[0]
            else:
                query = text
            await m.edit("** Searching ...**")
            search = get_youtube_video(query)
            stream = search[0]
            file = await get_youtube_stream(stream)
        await m.edit("** Processing ...**")
        check = db.get(chat_id)
        if not check:
            await call.join_group_call(
                chat_id,
                AudioVideoPiped(
                    file,
                    HighQualityAudio(),
                    HighQualityVideo(),
                ),
                stream_type=StreamType().pulse_stream
            )
            await put_que(chat_id, file, "Video")
            await m.edit("** Streaming Started!**")
            await message.delete()
        else:
            pos = await put_que(chat_id, file, "Video")
            await m.edit(f"** Added To Queue #{pos}**")
            await m.delete()
    except Exception as e:
        await m.edit(f"**Error:** `{e}`")


# Pause Stream
@app.on_message(commandz(["pse", "pause"]) & SUDOERS)
async def pause_stream(client, message):
    chat_id = message.chat.id
    try:
        check = db.get(chat_id)
        if check:
            await call.pause_stream(chat_id)
            return await eor(message, "**Stream Paused !**")
        else:
            return await eor(message, "**Nothing Playing !**")
    except Exception as e:
        await eor(message, f"**Error:** `{e}`")


# Resume Stream
@app.on_message(commandz(["rsm", "resume"]) & SUDOERS)
async def resume_streams(client, message):
    chat_id = message.chat.id
    try:
        check = db.get(chat_id)
        if check:
            await call.resume_stream(chat_id)
            return await eor(message, "**Stream Resumed !**")
        else:
            return await eor(message, "**Nothing Playing !**")
    except Exception as e:
        await eor(message, f"**Error:** `{e}`")
        
        
# Skip To Next Stream
@app.on_message(commandz(["skp", "skip"]) & SUDOERS)
async def change_streams(client, message):
    chat_id = message.chat.id
    try:
        check = db.get(chat_id)
        if check:
            que = db[chat_id]
            que.pop(0)
            if len(que) == 0:
                await call.leave_group_call(chat_id)
                return await eor(message, "Empty Queue !")
            else:
                file = check[0]["file"]
                type = check[0]["type"]
                if type == "Audio":
                    stream = AudioPiped(
                        file,
                        HighQualityAudio(),
                    )
                elif type == "Video":
                    stream = AudioVideoPiped(
                        file,
                        HighQualityAudio(),
                        HighQualityVideo(),
                    )
                await call.change_stream(chat_id, stream)
                return await eor(message, " Skipped !")
        else:
            return await eor(message, "**Nothing Playing ...**")
    except Exception as e:
        await eor(message, f"**Error:** `{e}`")


# Stop/End Stream
@app.on_message(commandz(["stp", "stop", "end"]) & SUDOERS)
async def leave_streams(client, message):
    chat_id = message.chat.id
    try:
        check = db.get(chat_id)
        if check:
            check.pop(0)
            await call.leave_group_call(chat_id)
            return await eor(message, "**Stream Stopped !**")
        else:
            return await eor(message, "**Nothing Playing !**")
    except Exception as e:
        await eor(message, f"**Error:** `{e}`")


__NAME__ = " ᴠᴄʙᴏᴛ "
__MENU__ = """
** 𝗔𝗨𝗗𝗜𝗢 & 𝗩𝗜𝗗𝗘𝗢 𝗣𝗟𝗔𝗬𝗘𝗥 𝗢𝗡𝗟𝗬
𝗙𝗢𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠 𝗚𝗥𝗢𝗨𝗣𝗦 ...**

** 𝗩𝗖𝗕𝗢𝗧 𝗔𝗟𝗟 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦:**
`.play` [name] - 𝗣𝗟𝗔𝗬 𝗔𝗡 𝗔𝗨𝗗𝗜𝗢 
𝗦𝗢𝗡𝗚 𝗕𝗬 𝗚𝗜𝗩𝗜𝗡𝗚 𝗡𝗔𝗠𝗘.

`.vplay` [name] - 𝗣𝗟𝗔𝗬 𝗔𝗡 𝗩𝗜𝗗𝗘𝗢
𝗦𝗢𝗡𝗚 𝗕𝗬 𝗚𝗜𝗩𝗜𝗡𝗚 𝗡𝗔𝗠𝗘.

`.pause` - 𝗧𝗢 𝗣𝗔𝗨𝗦𝗘 𝗦𝗧𝗥𝗘𝗔𝗠.
`.resume` - 𝗧𝗢 𝗥𝗘𝗦𝗨𝗠𝗘 .
`.skip` - 𝗦𝗞𝗜𝗣 𝗧𝗢 𝗡𝗘𝗫𝗧 𝗦𝗢𝗡𝗚.
`.end` - 𝗧𝗢 𝗦𝗧𝗢𝗣 𝗦𝗧𝗥𝗘𝗔𝗠.

** 𝗩𝗖𝗕𝗢𝗧 𝗦𝗛𝗢𝗥𝗧𝗖𝗨𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦:**
=> [ply, vply, pse, rsm, skp, stp]
"""
