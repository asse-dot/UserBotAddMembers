import asyncio
from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

import humanize
from userbot import UserBot
from userbot.helpers.PyroHelpers import GetChatID, ReplyCheck


AFK = False
AFK_REASON = ""
AFK_TIME = ""
USERS = {}
GROUPS = {}


def subtract_time(start, end):
    """Get humanized time"""
    subtracted = humanize.naturaltime(start - end)
    return str(subtracted)


@UserBot.on_message(
    ((filters.group & filters.mentioned) | filters.private) & ~filters.me & ~filters.service, group=3
)
async def collect_afk_messages(_, message: Message):
    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME)
        is_group = True if message.chat.type in ["supergroup", "group"] else False
        CHAT_TYPE = GROUPS if is_group else USERS

        if GetChatID(message) not in CHAT_TYPE:
            text = (
                f"`Ciao.\n"
                f"Nn sono disponibile ora.\n"
                f"Ultimo accesso: {last_seen}\n"
                f"Motivo rp: ```{AFK_REASON.upper()}```\n"
                f"A dopo.`"
            )
            await UserBot.send_message(
                chat_id=GetChatID(message),
                text=text,
                reply_to_message_id=ReplyCheck(message),
            )
            CHAT_TYPE[GetChatID(message)] = 1
            return
        elif GetChatID(message) in CHAT_TYPE:
            if CHAT_TYPE[GetChatID(message)] == 10:
                text = (
                    f"`CUESTA HE LA SEGRETERIA DI HE RESTINGO\n"
                    f"Pocco dio o quit tg nn vengo on da {last_seen}\n"
                    f"ADDIO.\n"
                    f"QUITTO TG.\n"
                    f"NN SPAMMARMI PLEASE`"
                )
                await UserBot.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=ReplyCheck(message),
                )
            elif CHAT_TYPE[GetChatID(message)] > 50:
                return
            elif CHAT_TYPE[GetChatID(message)] % 5 == 0:
                text = (
                    f"`A scemo nn so ancora tornato.\n"
                    f"Sto thyardando su coralmc, nn rientro da {last_seen}\n"
                    f"He lol xd he restingo : ```{AFK_REASON.upper()}```\n"
                    f"Ci verimm he lokitobaby .`"
                )
                await UserBot.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=ReplyCheck(message),
                )

        CHAT_TYPE[GetChatID(message)] += 1


@UserBot.on_message(filters.command("afk", ".") & filters.me, group=3)
async def afk_set(_, message: Message):
    global AFK_REASON, AFK, AFK_TIME

    cmd = message.command
    afk_text = ""

    if len(cmd) > 1:
        afk_text = " ".join(cmd[1:])

    if isinstance(afk_text, str):
        AFK_REASON = afk_text

    AFK = True
    AFK_TIME = datetime.now()

    await message.delete()


@UserBot.on_message(filters.command("afk", "!") & filters.me, group=3)
async def afk_unset(_, message: Message):
    global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME).replace("ago", "").strip()
        await message.edit(
            f"`Mentre ti stavi segando su martina dell`anna e sei durato (for {last_seen}), hai ricevuto {sum(USERS.values()) + sum(GROUPS.values())} "
            f"messaggi da quei coglioni di  {len(USERS) + len(GROUPS)} chats`"
        )
        AFK = False
        AFK_TIME = ""
        AFK_REASON = ""
        USERS = {}
        GROUPS = {}
        await asyncio.sleep(5)

    await message.delete()


@UserBot.on_message(filters.me, group=3)
async def auto_afk_unset(_, message: Message):
    global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME).replace("ago", "").strip()
        reply = await message.reply(
            f"`Mentre sei stato afk a segarti su Frokie dell anna (e sei durato {last_seen}), hai ricevuto {sum(USERS.values()) + sum(GROUPS.values())} "
            f"messaggi da {len(USERS) + len(GROUPS)} chats`"
        )
        AFK = False
        AFK_TIME = ""
        AFK_REASON = ""
        USERS = {}
        GROUPS = {}
        await asyncio.sleep(5)
        await reply.delete()