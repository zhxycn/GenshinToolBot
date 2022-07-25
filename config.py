import yaml

from utils import strtobool


def get_config(key):
    """获取配置项."""
    config = yaml.safe_load(open("config.yaml"))
    return config[key]


bot_name = get_config("bot_name")
api_id = get_config("api_id")
api_hash = get_config("api_hash")
bot_token = get_config("bot_token")
debug = strtobool(get_config("debug"))
