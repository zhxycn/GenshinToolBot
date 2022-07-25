"""
用于在控制台输出信息和记录日志至文件.
引用方式:
    from utils.logger import logger

    logger.info("Info")
    logger.error("Error")
    logger.debug("Debug")
    logger.warning("Warning")
    logger.critical("Critical")
输出格式:
    控制台:
        yyyy-MM-dd HH:mm:ss HostName BotName[PID] LogLevel Message
    日志文件:
        [yyyy-MM-dd HH:mm:ss,SSS] [PID] [LogLevel] Message
"""

import os
import logging
import coloredlogs
from logging.handlers import TimedRotatingFileHandler

import config


# 查找 logs 目录是否存在，如果不存在则创建.
if os.path.exists("logs"):
    pass
else:
    os.mkdir("logs")


class GetLogs:
    """获取日志记录."""

    def __init__(self):
        """输出日志, 并按照日期分割日志文件."""
        self.logger = logging.getLogger(f"{config.bot_name}")
        self.logger.setLevel(logging.DEBUG if config.debug else logging.INFO)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
        )
        logs_path = os.path.join("./logs/", 'bot.log')
        file_handler = TimedRotatingFileHandler(
            filename=logs_path, when="midnight", interval=1, encoding="utf-8"
        )
        file_handler.suffix = "%Y%m%d.log"
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG if config.debug else logging.INFO)
        self.logger.addHandler(file_handler)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.DEBUG if config.debug else logging.INFO)
        self.logger.addHandler(console_handler)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        if config.debug:
            coloredlogs.install(level="DEBUG", logger=self.logger)
        else:
            coloredlogs.install(level="INFO", logger=self.logger)

    def info(self, msg):
        """日志级别info."""
        self.logger.info(msg)

    def debug(self, msg):
        """日志级别debug."""
        self.logger.debug(msg, exc_info=True)

    def error(self, msg):
        """日志级别error."""
        self.logger.error(msg, exc_info=True)

    def warning(self, msg):
        """日志级别warning."""
        self.logger.warning(msg, exc_info=True)

    def critical(self, msg):
        """日志级别critical."""
        self.logger.critical(msg, exc_info=True)


log = GetLogs()
