from pyrogram import filters
from pyrogram.types import Message
from pyrogram import *

from YukkiMusic import app, userbot, SUDOERS
from config import OWNER_ID

USER_ONE = userbot.one     #ASSISTANT ACCOUNT ONE
USER_TWO = userbot.two     #ASSISTANT ACCOUNT TWO
USER_THREE = userbot.three #ASSISTANT ACCOUNT THREE
USER_FOUR = userbot.four   #ASSISTANT ACCOUNT FOUR
USER_FIVE = userbot.five   #ASSISTANT ACCOUNT FIVE


#------------------------------AYUSH-ZEUS--------------------------------#


@app.on_message(filters.command(["setdp"]) & filters.user(OWNER_ID)
async def set_pfp(_, message: Message):
	if message.reply_to_message.photo:
		replytext = await message.reply_text("» Updating Profile Pic Of Assistant...")
		img = await message.reply_to_message.download()
		try:
			await USER_ONE.set_profile_photo(photo=img)
			return await replytext.edit_text(f"» Successfully Changed Profile.")
		except:
			return await replytext.edit_text("» Failed To Changing Profile.")
	else:
		await message.reply_text("» Reply To A Photo Lomde.")

#------------------------------------------------------------------------#
@app.on_message(filters.command(["setdp2"]) & filters.user(OWNER_ID)
async def set_pfp(_, message: Message):
	if message.reply_to_message.photo:
		replytext = await message.reply_text("» Updating Profile Pic Of Assistant 2...")
		img = await message.reply_to_message.download()
		try:
			await USER_TWO.set_profile_photo(photo=img)
			return await replytext.edit_text(f"» Successfully Changed Profile 2.")
		except:
			return await replytext.edit_text("» Failed To Changing Profile.")
	else:
		await message.reply_text("» Reply To A Photo Lomde.")
#------------------------------------------------------------------------#

@app.on_message(filters.command(["setdp3"]) & filters.user(OWNER_ID)
async def set_pfp(_, message: Message):
	if message.reply_to_message.photo:
		replytext = await message.reply_text("» Updating Profile Pic Of Assistant 3...")
		img = await message.reply_to_message.download()
		try:
			await USER_THREE.set_profile_photo(photo=img)
			return await replytext.edit_text(f"» Successfully Changed Profile 3.")
		except:
			return await replytext.edit_text("» Failed To Changing Profile.")
	else:
		await message.reply_text("» Reply To A Photo Lomde.")

#--------------------------------------------------------------------------#

@app.on_message(filters.command(["setdp4"]) & filters.user(OWNER_ID)
async def set_pfp(_, message: Message):
	if message.reply_to_message.photo:
		replytext = await message.reply_text("» Updating Profile Pic Of Assistant 4...")
		img = await message.reply_to_message.download()
		try:
			await USER_FOUR.set_profile_photo(photo=img)
			return await replytext.edit_text(f"» Successfully Changed Profile 4.")
		except:
			return await replytext.edit_text("» Failed To Changing Profile.")
	else:
		await message.reply_text("» Reply To A Photo Lomde.")

#------------------------------------------------------------------------#

@app.on_message(filters.command(["setdp5"]) & filters.user(OWNER_ID)
async def set_pfp(_, message: Message):
	if message.reply_to_message.photo:
		replytext = await message.reply_text("» Updating Profile Pic Of Assistant 5...")
		img = await message.reply_to_message.download()
		try:
			await USER_FIVE.set_profile_photo(photo=img)
			return await replytext.edit_text(f"» Successfully Changed Profile 5.")
		except:
			return await replytext.edit_text("» Failed To Changing Profile.")
	else:
		await message.reply_text("» Reply To A Photo Lomde.")

#-------------------------------------------------------------------------#


###########################################################################


@app.on_message(filters.command(["deldp"]) & filters.user(OWNER_ID)
async def del_pfp(_, message: Message):
	try:
		pfp = [p async for p in USER_ONE.get_chat_photos("me")]
		await USER_ONE.delete_profile_photos(pfp[0].file_id)
		return await message.reply_text("» Successfully Deleted.")
	except Exception as ayush:
		print(ayush)
		await message.reply_text("» Failed To Delete Profile.")

#-------------------------------------------------------------------------#


@app.on_message(filters.command(["deldp2"]) & filters.user(OWNER_ID)
async def del_pfp(_, message: Message):
	try:
		pfp = [p async for p in USER_TWO.get_chat_photos("me")]
		await USER_TWO.delete_profile_photos(pfp[0].file_id)
		return await message.reply_text("» Successfully Deleted.")
	except Exception as ayush:
		print(ayush)
		await message.reply_text("» Failed To Delete Profile 2.")

#-------------------------------------------------------------------------#


@app.on_message(filters.command(["deldp3"]) & filters.user(OWNER_ID)
async def del_pfp(_, message: Message):
	try:
		pfp = [p async for p in USER_THREE.get_chat_photos("me")]
		await USER_THREE.delete_profile_photos(pfp[0].file_id)
		return await message.reply_text("» Successfully Deleted 3.")
	except Exception as ayush:
		print(ayush)
		await message.reply_text("» Failed To Delete Profile.")

#-------------------------------------------------------------------------#


@app.on_message(filters.command(["deldp4"]) & filters.user(OWNER_ID)
async def del_pfp(_, message: Message):
	try:
		pfp = [p async for p in USER_FOUR.get_chat_photos("me")]
		await USER_FOUR.delete_profile_photos(pfp[0].file_id)
		return await message.reply_text("» Successfully Deleted 4.")
	except Exception as ayush:
		print(ayush)
		await message.reply_text("» Failed To Delete Profile.")

#-------------------------------------------------------------------------#


@app.on_message(filters.command(["deldp5"]) & filters.user(OWNER_ID)
async def del_pfp(_, message: Message):
	try:
		pfp = [p async for p in USER_FIVE.get_chat_photos("me")]
		await USER_FIVE.delete_profile_photos(pfp[0].file_id)
		return await message.reply_text("» Successfully Deleted 5.")
	except Exception as ayush:
		print(ayush)
		await message.reply_text("» Failed To Delete Profile.")

#-------------------------------------------------------------------------#
###########################################################################
