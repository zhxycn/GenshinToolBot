from datetime import datetime

from pyrogram.filters import command
from pyrogram.raw.functions import Ping

from bot import bot
from utils.logger import log


@bot.on_message(command("ping"))
async def ping(_, message):
    """计算服务器和Telegram之间的延迟."""
    username = \
        str(message.from_user.first_name) + " " + str(message.from_user.last_name)
    userid = message.from_user.id
    log.info(f"用户: {username} [{userid}] 使用了 ping 命令。")

    start = datetime.now()
    await bot.invoke(Ping(ping_id=0))
    end = datetime.now()
    ping_duration = (end - start).microseconds / 1000
    start = datetime.now()
    message = await message.reply("Pong!")
    end = datetime.now()
    msg_duration = (end - start).microseconds / 1000
    await message.edit(f"Pong! | PING: {ping_duration} | MSG: {msg_duration}")
