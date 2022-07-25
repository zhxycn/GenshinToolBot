"""自定义软件包."""


def strtobool(value):
    """将表示是/否的字符串转换为布尔值."""
    if value in ("True", "true", "Yes", "yes", "T", "t", "Y", "y", "1"):
        return True
    if value in ("False", "false", "No", "no", "F", "f", "N", "n", "0"):
        return False
    raise ValueError("Invalid boolean string")
