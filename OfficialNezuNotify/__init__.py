from .auth import OfficialNezuAuth
from .config import Config
from .notify import OfficialNezuNotify

__all__ = ["OfficialNezuAuth", "OfficialNezuNotify", "Config"]
__version__ = "0.2.0"

# git関連の情報を更新
__author__ = "neuzmi0627"
__email__ = "neuzmi.0627.dev@gmail.com"
__license__ = "MIT"
__description__ = "LINE Notify公式APIを利用したPython通知管理ライブラリ"
__url__ = "https://github.com/neuzmi0627/OfficialNezuNotify"

# 追加のgit関連情報を更新
__project_name__ = "OfficialNezuNotify"
__repository__ = "https://github.com/neuzmi0627/OfficialNezuNotify.git"
__keywords__ = ["line", "notify", "api", "official", "management", "python", "library"]
__classifiers__ = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Communications :: Chat",
    "Topic :: Utilities",
]
