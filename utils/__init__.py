# -*- coding: utf-8 -*-
"""
@software: PyCharm
@file: __init__.py.py
@time: 2024/6/25 上午11:59
@author SuperLazyDog
"""
from .download import check_file
from .init import (
    logger,
    RootPath,
    RealWidth,
    RealHeight,
    Hwnd,
)
from .config import config, characterIcons, fightTacticsDict, load_characters
from .utils import *
from .control import control
from .map import get_map_info, auto_find_way

__all__ = [
    "logger",
    "RootPath",
    "RealWidth",
    "RealHeight",
    "Hwnd",
    "find_template",
    "screenshot",
    "control",
    "wait_text",
    "get_map_info",
    "auto_find_way",
    "config",
    "characterIcons",
    "load_characters",
    "fightTacticsDict",
]
logger.debug("初始化utils模块完成")

version = "240806"
logger.info(f"当前版本：{version}")
