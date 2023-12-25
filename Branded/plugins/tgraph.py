import os

from .. import *
from telegraph import Telegraph, upload_file


telegraph = Telegraph()
filesize = 5242880 #[5MB]


@app.on_message(commandx("tl"))
async def telegraph_uploader(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    replied = message.reply_to_message
    m = await eor(message, "** Processing ...**")
    if replied:
        text_msg = replied.text
        animates = replied.animation
        media = (replied.animation or replied.photo
              or replied.video or replied.document)
        sticker =  replied.sticker
    else:
        return await m.edit(f"** Please Reply To A Media\nOr Text To Generate Telegraph\nLink...**")
    try:
        if text_msg:
            telegraph.create_account(short_name=f"{message.from_user.first_name}")
            author_name = str(message.from_user.first_name)
            author_url = f"https://t.me/{message.from_user.username}" if message.from_user.username else "https://t.me/BLACKx_GOD"
            if len(message.command) > 1:
                text_title = ' '.join(message.command[1:])
            else:
                text_title = str(message.from_user.first_name + " " + (message.from_user.last_name or ""))
            await m.edit("** Uploading ...**")
            response = telegraph.create_page(title=text_title, html_content=text_msg, author_name=author_name, author_url=author_url)
            upload_link = f"https://telegra.ph/{response['path']}"
            return await m.edit(
                text=f"** Uploaded To Telegraph.**\n\n `{upload_link}`",
                disable_web_page_preview=True,
            )
        elif media:
            if media.file_size <= filesize:
                await m.edit("** Downloading ...**")
                local_path = f"./downloads/{user_id}_{media.file_unique_id}/"
                local_file = await replied.download(local_path)
            else:
                return await m.edit("` File Size is Too Big...`")
        elif sticker:
            return await m.edit("` Sorry, Sticker Upload\nNot Allowed...`")
        else:
            return
        await m.edit("** Uploading ...**")
        upload_path = upload_file(local_file)
        upload_link = f"https://telegra.ph{upload_path[0]}"
        await m.edit(
            text=f"** Uploaded To Telegraph.**\n\n `{upload_link}`",
            disable_web_page_preview=True,
        )
        os.system(f"rm -rf {local_path}")
    except Exception as e:
        await m.edit(f"** Error:** `{e}`")
        pass


__NAME__ = " ᴛɢʀᴀᴘʜ "
__MENU__ = """**𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗣𝗛 𝗨𝗣𝗟𝗢𝗔𝗗𝗘𝗥:**

`.tl` - 𝗥𝗘𝗣𝗟𝗬 𝗧𝗛𝗜𝗦 𝗖𝗢𝗠𝗠𝗔𝗡𝗗 T𝗢
𝗔𝗡𝗬 𝗧𝗘𝗫𝗧 𝗢𝗥 𝗠𝗘𝗗𝗜𝗔 𝗧𝗢 𝗖𝗥𝗘𝗔𝗧𝗘
𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗣𝗛 𝗟𝗜𝗡𝗞.

`.tl` [title]” - 𝗦𝗘𝗧 𝗖𝗨𝗦𝗧𝗢𝗠 𝗧𝗜𝗧𝗟𝗘
𝗢𝗡 𝗬𝗢𝗨𝗥 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗣𝗛 𝗣𝗢𝗦𝗧.

(𝗪𝗢𝗥𝗞𝗜𝗡𝗚 𝗢𝗡𝗟𝗬 𝗢𝗡 𝗧𝗘𝗫𝗧 𝗣𝗢𝗦𝗧).

**𝗘𝗫:-** `/tl  My Note `
"""
