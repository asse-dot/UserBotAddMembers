import asyncio
import time
from datetime import datetime
from platform import python_version

from pyrogram import filters
from pyrogram.types import Message
from pyrogram import __version__

from userbot import UserBot, START_TIME



@UserBot.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, message: Message):
    txt = (
        f"**{UserBot.__class__.__name__}** ```RUNNING```\n"
        f"-> Current Uptime: `{str(datetime.now() - START_TIME).split('.')[0]}`\n"
        f"-> Python: `{python_version()}`\n"
        f"-> Pyrogram: `{__version__}`"
    )
    await message.edit(txt)

@UserBot.on_message(filters.me & filters.command('prova', '.'))
def prova(_, message: Message):
    UserBot.delete_messages(message.chat.id, message.message_id)
    for member in UserBot.iter_chat_members(message.chat.id, 30):
        try:
            UserBot.add_chat_members(-1001693987391, member.user.id)
            time.sleep(5)
        except Exception as e:
            print(e)


