from pyrogram import Client, filters


sepratelogin = Client("dmdemo",
	api_id=int(API_ID),
	api_hash=str(API_HASH),
	session_string=str(STRING1),
	no_updates=False)





@sepratelogin.on_message(filters.text & filters.private)
async def demo(client, message):
	await message.reply("https://t.me/MusicLover_xd")

sepratelogin.run()
