from pyrogram import Client

import config

bot = Client(
    config.bot_name,
    api_id=config.api_id,
    api_hash=config.api_hash,
    bot_token=config.bot_token,
)
