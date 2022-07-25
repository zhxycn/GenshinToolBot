"""功能模块."""

from glob import glob
from os import sep
from os.path import dirname, basename, isfile


def __list_modules():
    """遍历模块目录, 返回模块名列表."""
    module_paths = glob(f"{dirname(__file__)}{sep}*.py")
    return [
        basename(file)[:-3]
        for file in module_paths
        if isfile(file)
        and file.endswith(".py")
        and not file.endswith("__init__.py")
    ]


module_list = sorted(__list_modules())
