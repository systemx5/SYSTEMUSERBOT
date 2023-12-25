from .. import *

@app.on_message(commandx(["alive"]))
async def alive_check(client, message):
    await message.reply_text("** 𝗜 𝗔𝗠 𝗔𝗟𝗜𝗩𝗘 𝗠𝗬 𝗗𝗘𝗔𝗥 𝗦𝗬𝗦𝗧𝗘𝗠 𝗞𝗜𝗡𝗚 𝗠𝗔𝗦𝗧𝗘𝗥 ...**")



__NAME__ = " ᴀʟɪᴠᴇ "
__MENU__ = f"""
** 𝗖𝗛𝗘𝗖𝗞 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗪𝗢𝗥𝗞𝗜𝗡𝗚
𝗢𝗥 𝗡𝗢𝗧 ..**

**Example:** `.alive`
"""
