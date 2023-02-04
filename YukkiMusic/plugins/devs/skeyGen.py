import os
import base64
import re
import subprocess
import sys
import traceback
from inspect import getfullargspec
from io import StringIO
from time import time
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from config import OWNER_ID
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from dotenv import load_dotenv
#-----------------------------------------------------------------------------------#


@app.on_message(
    filters.command("skey")
    & filters.user(OWNER_ID)
    & ~filters.forwarded
    & ~filters.via_bot
)
async def skeygenfunction(client, message: Message, _):
	filee = open(".env", "rb")
	skey_gen = base64.b64encode(filee.read()).decode('utf-8')
	skey_file = "Skey_Session.txt"
	await message.reply_document(
            document=skey_file,
            caption=f"Your Skey Session Key Generation •✅",
            quote=False
            )
	os.remove(skey_file)
#------------------------------------------------------------------------------------#

#-------------Credits----------------#
#-------------Ayush
#-------------Harpreet
#-------------Vir