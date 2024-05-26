import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit , usertype,addpre
ADMIN = int(os.environ.get("ADMIN", 6976445947))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔") 


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("Select Plan.........",quote=True,reply_markup=InlineKeyboardMarkup([
		           [
				   InlineKeyboardButton("🪙 𝐒𝐢𝐥𝐯𝐞𝐫 𝐓𝐢𝐞𝐫 🪙", callback_data="vip1")
				   ], [
					InlineKeyboardButton("💫 𝐆𝐨𝐥𝐝 𝐓𝐢𝐞𝐫 💫", callback_data="vip2")
				   ], [
					InlineKeyboardButton("💎 𝐃𝐢𝐚𝐦𝐨𝐧𝐝 𝐓𝐢𝐞𝐫 💎", callback_data="vip3")
					]]))
        			

@Client.on_message((filters.channel | filters.private) & filters.user(ADMIN) & filters.command(["resetpower"]))
async def resetpower(bot, message):
	    await message.reply_text(text=f"ᴅᴏ  ʏᴏᴜ  ʀᴇᴀʟʟʏ  ᴡᴀɴᴛ  ᴛᴏ  ʀᴇꜱᴇᴛ  ʜɪꜱ  ʟɪᴍɪᴛ.",quote=True,reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton(" 𝐘𝐞𝐬   ✅ ",callback_data = "dft")],
				   [InlineKeyboardButton(" 𝐍𝐨   ❌ ",callback_data = "cancel")]
				   ]))

@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 21474836480
	uploadlimit(int(user_id),6976445947)
	usertype(int(user_id),"🪙 𝐒𝐢𝐥𝐯𝐞𝐫 𝐓𝐢𝐞𝐫 🪙")
	addpre(int(user_id))
	await update.message.edit("ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ  ɪɴᴄʀᴇᴀꜱᴇᴅ  ᴛᴏ  20 ɢʙ  ᴘᴇʀ  ᴅᴀʏ.")
	await bot.send_message(user_id,"Hey you are Upgraded To 🪙 𝐒𝐢𝐥𝐯𝐞𝐫 𝐓𝐢𝐞𝐫 🪙. check your plan here /myplan")
	await bot.send_message(log_channel,f"⚡️ Plan Upgraded successfully 💥\n\nHey you are Upgraded To 🪙 𝐒𝐢𝐥𝐯𝐞𝐫 𝐓𝐢𝐞𝐫 🪙. check your plan here /myplan")
@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 53687091200
	uploadlimit(int(user_id),6976445947)
	usertype(int(user_id),"💫 𝐆𝐨𝐥𝐝 𝐓𝐢𝐞𝐫 💫")
	addpre(int(user_id))
	await update.message.edit("ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ  ɪɴᴄʀᴇᴀꜱᴇᴅ  ᴛᴏ  50 ɢʙ  ᴘᴇʀ  ᴅᴀʏ.")
	await bot.send_message(user_id,"Hey you are Upgraded To 💫 𝐆𝐨𝐥𝐝 𝐓𝐢𝐞𝐫 💫. check your plan here /myplan")
@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 1073741824000
	uploadlimit(int(user_id), 6976445947)
	usertype(int(user_id),"💎 𝐃𝐢𝐚𝐦𝐨𝐧𝐝 𝐓𝐢𝐞𝐫 💎")
	addpre(int(user_id))
	await update.message.edit("ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ  ɪɴᴄʀᴇᴀꜱᴇᴅ  ᴛᴏ  Unlimited  ᴘᴇʀ  ᴅᴀʏ.")
	await bot.send_message(user_id,"Hey you are Upgraded To 💎 𝐃𝐢𝐚𝐦𝐨𝐧𝐝 𝐓𝐢𝐞𝐫 💎. check your plan here /myplan")

@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
	id = update.message.reply_to_message.text.split("/resetpower")
	user_id = id[1].replace(" ", "")
	inlimit = 1073741824
	uploadlimit(int(user_id), 6976445947)
	usertype(int(user_id),"🦋 𝐅𝐫𝐞𝐞 𝐏𝐥𝐚𝐧 𝐔𝐬𝐞𝐫 🦋")
	addpre(int(user_id))
	await update.message.edit("ᴜꜱᴇʀ  ʟɪᴍɪᴛ  ʜᴀꜱ  ʙᴇᴇɴ  ʀᴇꜱᴇᴛ  ꜱᴜᴄᴄᴇꜱꜱꜱꜰᴜʟʟʏ.")
	await bot.send_message(user_id,"ʏᴏᴜʀ  ʟɪᴍɪᴛ  ʜᴀꜱ  ʙᴇᴇɴ  ʀᴇꜱᴇᴛ  ꜱᴜᴄᴄᴇꜱꜱꜱꜰᴜʟʟʏ.\n\nᴄᴏɴᴛᴀᴄᴛ  <a href='https://t.me/MrSagar0'>**ᴏᴡɴᴇʀ**</a>  ꜰᴏʀ  ᴍᴏʀᴇ  ᴅᴇᴛᴀɪʟꜱ.")

