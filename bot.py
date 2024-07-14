# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support

import os, math, time, re
from datetime import datetime
from pytz import timezone
from hydrogram import Client, filters
from config import Config, rkn
from hydrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from hydrogram.file_id import FileId

bot = Client(name="Tested-Botz",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
          #  plugins={"root": "plugins"},
            sleep_threshold=15)

dc_bot = Client(name="Dc-Tested-Botz",
            api_id=Config.DC_API_ID,
            api_hash=Config.DC_API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
          #  plugins={"root": "plugins"},
            sleep_threshold=15)


async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 5.00) == 0 or current == total:        
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "{0}{1}".format(
            ''.join(["▣" for i in range(math.floor(percentage / 5))]),
            ''.join(["▢" for i in range(20 - math.floor(percentage / 5))])
        )            
        tmp = progress + rkn.RKN_PROGRESS.format( 
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),            
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text=f"{ud_type}\n\n{tmp}",               
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✖️ 𝙲𝙰𝙽𝙲𝙴𝙻 ✖️", callback_data="close")]])                                               
            )
        except:
            pass

def humanbytes(size):    
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'ʙ'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "ᴅ, ") if days else "") + \
        ((str(hours) + "ʜ, ") if hours else "") + \
        ((str(minutes) + "ᴍ, ") if minutes else "") + \
        ((str(seconds) + "ꜱ, ") if seconds else "") + \
        ((str(milliseconds) + "ᴍꜱ, ") if milliseconds else "")
    return tmp[:-2] 

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60      
    return "%d:%02d:%02d" % (hour, minutes, seconds)
	
@bot.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def download_media_test(bot, message):
    user_id = message.from_user.id
    rkn_botz = await message.reply("`Tʀʏ Tᴏ Dᴏᴡɴʟᴏᴀᴅ....`")
    new_filename = f"rkn_botz_testedbotz_digital_botz.mkv"
    try:
        # file downloading started...
        rkn_file = getattr(message, message.media.value)
        dcv = """5"""
        dc_id = """5"""
        dcid = FileId.decode(rkn_file.file_id).dc_id
        if str(dcid) in int(dc_id):
            downloading = f"downloads/{user_id}/rkn{new_filename}"
            path = await dc_bot.download_media(message=message, file_name=downloading, progress=progress_for_pyrogram, progress_args=("Download Started....", rkn_botz, time.time()))
        else:
            downloading = f"downloads/{user_id}/rkn{new_filename}"
            path = await bot.download_media(message=message, file_name=downloading, progress=progress_for_pyrogram, progress_args=("Download Started....", rkn_botz, time.time()))
    except Exception as e:
     	return await rkn_botz.edit(e)
     	     
    # file downloading path
    file_path = f"downloads/{user_id}/{new_filename}"
	
    os.rename(path, file_path)
    caption = f"**{new_filename}**"
    ph_path = None
    duration = 0
    try:
        parser = createParser(file_path)
        metadata = extractMetadata(parser)
        if metadata.has("duration"):
            duration = metadata.get('duration').seconds
        parser.close()
    except:
        pass
    await rkn_botz.edit('Try To Uploading')
    await bot.send_video(
                    user_id,
                    video=file_path,
                    caption=caption,
                    thumb=ph_path,
                    duration=duration,
                    progress=progress_for_pyrogram,
                    progress_args=('Upload Started....', rkn_botz, time.time()))
    
    await rkn_botz.edit('Your Files Successfully Uploaded')
    os.remove(file_path)

bot.run()
dc_bot.run
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Bots
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
