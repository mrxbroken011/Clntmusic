from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.core.call import Anony
from AnonXMusic.utils import bot_sys_stats
from AnonXMusic.utils.decorators.language import language
from AnonXMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]))
@language
async def ping(_, message: Message):
    start_time = datetime.now()
    await message.reply_text("Pong!")
    end_time = datetime.now()
    await Anony(
        message,
        text=f"🏓 **Pong!**\n\n"
             f"🕒 {(end_time - start_time).microseconds / 1000}ms",
        reply_markup=supp_markup(),
        disable_web_page_preview=True
    )
    
