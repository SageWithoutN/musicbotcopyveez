import os
import shutil
import sys
import traceback
from functools import wraps
from os import environ, execle

import heroku3
import psutil
from config import (
    BOT_USERNAME,
    GROUP_SUPPORT,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    HEROKU_URL,
    OWNER_ID,
    U_BRANCH,
    UPSTREAM_REPO,
)
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from handlers.song import get_text, humanbytes
from handlers import __version__
from helpers.database import db
from helpers.dbtools import main_broadcast_handler
from helpers.decorators import sudo_users_only
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.private
    & filters.command("broadcast")
    & filters.user(OWNER_ID)
    & filters.reply
)
async def broadcast_handler_open(_, m: Message):
    await main_broadcast_handler(m, db)

