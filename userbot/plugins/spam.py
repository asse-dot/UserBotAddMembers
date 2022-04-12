import asyncio

from pyrogram import filters
from pyrogram.types import Message
from userbot import UserBot
from userbot.helpers.PyroHelpers import ReplyCheck

RUN = False

@UserBot.on_message(filters.command("spam", ".") & filters.me)
async def spam(_, message: Message):
    global RUN
    # Get current chat and spam to there.
    # if in group and replied to user, then spam replying to user.
    
    if len(message.command) <= 1:
        await message.edit_text("Serve TEMPO - INTERVALLLO - MESSAGGIO DA INVIARE")
        await asyncio.sleep(3)
        await message.delete()
        return
    
    times = message.command[1]
    interval = message.command[2]
    to_spam = " ".join(message.command[3:])
    
    if not interval.isnumeric() and not times.isnumeric():
        return
    RUN = True
    if message.chat.type in ["supergroup", "group"]:
        for _ in range(int(times)):
           if not RUN:
                break
                
            await UserBot.send_message(
                message.chat.id, to_spam, reply_to_message_id=ReplyCheck(message)
            )
            await asyncio.sleep(int(interval))

    if message.chat.type == "private":
        for _ in range(int(times)):
            if not RUN:
                break
                
            await UserBot.send_message(message.chat.id, to_spam)
            await asyncio.sleep(int(interval))
            
    
@UserBot.on_message(filters.command("stop", ".") & filters.me)
async def stop(_, message: Message):
    global RUN
    if RUN:
        RUN = False
