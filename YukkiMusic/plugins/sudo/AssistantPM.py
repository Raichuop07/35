import asyncio
from pyrogram import Client
from pyrogram import filters
from pyrogram.filters import command
from pyrogram.types import Message
from YukkiMusic import userbot

#----------------------IMPORTING DONE OF MODULES------------------------#

USER_ONE = userbot.one     #ASSISTANT ACCOUNT ONE
USER_TWO = userbot.two     #ASSISTANT ACCOUNT TWO
USER_THREE = userbot.three #ASSISTANT ACCOUNT THREE
USER_FOUR = userbot.four   #ASSISTANT ACCOUNT FOUR
USER_FIVE = userbot.five   #ASSISTANT ACCOUNT FIVE

###########################ASSISTANT_PLACED##############################

GUARD = "True"


@USER_ONE.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmguard(client: USER_ONE, message: Message):
	if GUARD == "True":
		chat_id = message.chat.id
		await USER.send_message(message.chat.id,f"Hello {message.from_user.mention()} •✅\n PLease Join >> https://t.me/life_codes \n\n\n\n NEVER DM/PM TO BOT's ASSISTANTS ⚠")
		return

@USER_TWO.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmguard(client: USER_TWO, message: Message):
	if GUARD == "True":
		chat_id = message.chat.id
		await USER.send_message(message.chat.id,f"Hello {message.from_user.mention()} •✅\n PLease Join >> https://t.me/life_codes \n\n\n\n NEVER DM/PM TO BOT's ASSISTANTS ⚠")
		return

"""#@USER_THREE.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmguard(client: USER_THREE, message: Message):
	if GUARD == "True":
		chat_id = message.chat.id
		await USER.send_message(message.chat.id,f"Hello {message.from_user.mention()} •✅\n PLease Join >> https://t.me/life_codes \n\n\n\n NEVER DM/PM TO BOT's ASSISTANTS ⚠")
		return

#@USER_FOUR.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmguard(client: USER_FOUR, message: Message):
	if GUARD == "True":
		chat_id = message.chat.id
		await USER.send_message(message.chat.id,f"Hello {message.from_user.mention()} •✅\n PLease Join >> https://t.me/life_codes \n\n\n\n NEVER DM/PM TO BOT's ASSISTANTS ⚠")
		return

#@USER_FIVE.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmguard(client: USER_FIVE, message: Message):
	if GUARD == "True":
		chat_id = message.chat.id
		await USER.send_message(message.chat.id,f"Hello {message.from_user.mention()} •✅\n PLease Join >> https://t.me/life_codes \n\n\n\n NEVER DM/PM TO BOT's ASSISTANTS ⚠")
		return"""