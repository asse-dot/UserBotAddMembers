from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import ChatSendStickersForbidden
from userbot import UserBot

SETS = {
    1: [
        'CAACAgUAAxkDAAI4IGEOvOVBnkzKf6MQCgvsJuGk5PRbAAKYAgACf1BBV4xU-M-oahBJHgQ',
        'CAACAgUAAxkDAAI4IWEOvOZKgAYskiJ3gcu6InBogwnkAAJKAwACmd1BV4c0knnsItszHgQ',
        'CAACAgUAAxkDAAI4ImEOvOmcilCfnLmTxOGZj5Liv0t5AAIVBAACvM9BV9WweboNia0rHgQ'
    ],
    2: [
        'CAACAgUAAxkDAAI4J2EOvtgOW67X-ozbSRS_0ubjEJEMAAIbAwACcYtQV1-l_18Yq80SHgQ',
        'CAACAgQAAxkBAAEEdqRiV0O7VFdEhhNt2C2TfTWKtSnl8gACNgcAAosRdwZvrf6KzTIhjiME',
        'CAACAgUAAxkDAAI4KWEOvtkP_NTgkg4GobiDa9pNJPfXAAI9AwACrd9RVx3nZiYeQ4PeHgQ'
    ],

    3: [
        'CAACAgIAAxkBAAEEdqZiV0RRN9kWq6l2e9a065vEhnb0JQAC-hAAAqHHKEg5ZXbrk1gHoyME'
    ],

    4: [
        "ciao"
    ]
}


@UserBot.on_message(filters.command(["sticker"], ".") & filters.me)
async def sticker_sender(bot: UserBot, message: Message):
    if len(message.command) > 1:
        set_to_send = message.command[1]

        if type(set_to_send) == str:
            set_to_send = int(set_to_send)

        stickers = SETS[set_to_send]

        for x in stickers:
            try:
                await bot.send_sticker(message.chat.id, x)
            except ChatSendStickersForbidden:
                await message.edit("```Cannot send stickers here```")
                await message.delete()
                return

        await message.delete()


