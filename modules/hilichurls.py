import json
from os import sep

from pyrogram.filters import command

from bot import bot
from utils.logger import log


# 加载数据文件.
# 数据来自 https://wiki.biligame.com/ys .
with open(f"data{sep}hilichurls_dictionary.json", "r", encoding="utf8") as f:
    hilichurls_dictionary = json.load(f)


@bot.on_message(command("hilichurls"))
async def hilichurls(_, message):
    """丘丘语字典."""
    username = \
        str(message.from_user.first_name) + " " + str(message.from_user.last_name)
    userid = message.from_user.id
    try:
        if message.reply_to_message:
            msg = message.reply_to_message.text
        else:
            msg = message.text.split(" ", 1)[1]
    except IndexError:
        log.info(f"用户: {username} [{userid}] 使用了 hilichurls 命令。")
        return await message.reply("请输入要查询的丘丘语。")

    log.info(f"用户: {username} [{userid}] 使用 hilichurls 命令查询了 {msg}。")
    search = str.casefold(msg)  # 忽略大小写以方便查询
    if search not in hilichurls_dictionary:
        return await message.reply(f"在丘丘语字典中未找到 {msg}。")
    result = hilichurls_dictionary[f"{search}"]
    return await message.reply(f"丘丘语: `{search}`\n\n`{result}`")
