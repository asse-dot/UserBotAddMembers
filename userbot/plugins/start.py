import asyncio
import time
from datetime import datetime
from platform import python_version

from pyrogram import filters
from pyrogram.types import Message
from pyrogram import __version__

from userbot import UserBot, START_TIME, id_group, id_channel



@UserBot.on_message(filters.command("alive", ".") & filters.me)
async def alive(_, message: Message):
    txt = (
        f"**{UserBot.__class__.__name__}** ```RUNNING```\n"
        f"-> Current Uptime: `{str(datetime.now() - START_TIME).split('.')[0]}`\n"
        f"-> Python: `{python_version()}`\n"
        f"-> Pyrogram: `{__version__}`"
    )
    await message.edit(txt)

@UserBot.on_message(filters.me & filters.command('add_c', '.'))
async def add_channel(_, message: Message):
    await UserBot.delete_messages(message.chat.id, message.message_id)
    async for member in UserBot.iter_chat_members(message.chat.id, 200):
        try:
            await UserBot.add_chat_members(id_channel, member.user.id)
            await asyncio.sleep(12)
        except Exception as e:
            print(e)

@UserBot.on_message(filters.me & filters.command('add_g', '.'))
async def add_group(_, message: Message):
    await UserBot.delete_messages(message.chat.id, message.message_id)
    async for member in UserBot.iter_chat_members(message.chat.id, 20):
        try:
            await UserBot.add_chat_members(id_group, member.user.id)
            await asyncio.sleep(10)
        except Exception as e:
            print(e)


@UserBot.on_message(filters.me & filters.command('send_message', '.'))
async def send_private_message(_, message: Message):
    await UserBot.delete_messages(message.chat.id, message.message_id)
    async for member in UserBot.iter_chat_members(message.chat.id):
        try:
            await UserBot.send_message(member.user.id, "Ciao! ti consiglio un gruppo che parla di scienza, tecnologia e ingegneria. Se vuoi entrare: @TecnologiaPUBIT")
            await asyncio.sleep(2)
        except Exception as e:
            print(str(e))