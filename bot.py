# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
import os
from hydrogram import Client, filters
from config import Config


bot = Client(name="Tested-Botz",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
          #  plugins={"root": "plugins"},
            sleep_threshold=15)

@bot.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def download_media_test(bot, message):
    user_id = message.from_user.id
    rkn_botz = await message.reply("`Tʀʏ Tᴏ Dᴏᴡɴʟᴏᴀᴅ....`")
    new_filename = f"rkn_botz_testedbotz_digital_botz.mkv"
    try:
        # file downloading started...
        downloading = f"downloads/{user_id}/rkn{new_filename}"
        path = await bot.download_media(message=file, file_name=downloading)#, progress=progress_for_pyrogram, progress_args=("ᴅᴏᴡɴʟᴏᴀᴅ sᴛᴀʀᴛᴇᴅ....", ms, time.time()))                    
    except Exception as e:
     	return await rkn_botz.edit(e)
     	     
    # file downloading path
    file_path = f"downloads/{user_id}/{new_filename}"
	
    os.rename(path, file_path)
    await rkn_botz.edit('Try To Uploading')
    await bot.send_video(video=file_path)
    await rkn_botz.edit('Your Files Successfully Uploaded')
    os.remove(file_path)

bot.run()
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
