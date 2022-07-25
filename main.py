from importlib import import_module

from pyrogram import idle

from bot import bot
from modules import module_list
from utils.logger import log


async def main():
    """启动程序并加载模块."""
    await bot.start()
    log.info("程序已启动")
    for module_name in module_list:
        try:
            import_module(f"modules.{module_name}")
            log.info(f"已加载模块 {module_name}")
        except BaseException as e:
            log.error(f"{module_name} 模块加载失败。 原因: {e}")

    await idle()
    await bot.stop()
    log.info("程序已停止")


bot.run(main())
