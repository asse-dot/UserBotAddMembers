import asyncio
import os
import sys
from configparser import ConfigParser

from pyrogram import Client
from pyrogram.raw import functions
from pyrogram.raw.all import layer
from pyrogram.types import Message


class UserBot(Client):
    def __init__(self, version='0.0.0'):
        self.bio = None
        self.version = version
        self.name = name = self.__class__.__name__.lower()
        config_file = 'config.ini'

        self.config = ConfigParser().read(config_file)

        super().__init__(
            name,
            api_id = '15073774',
            api_hash=  'f0d9876395c19d51bbd0da0ac86d71f0',
            config_file=config_file,
            plugins=dict(root=f"{name}/plugins"),
            workdir="./",
            app_version=self.version
        )

    async def start(self):
        await super().start()

        restart_reply_details = super().search_messages("me", query="#userbot_restart")
        async for x in restart_reply_details:
            _, chat_id, message_id = x.text.split(", ")

            try:
                await super().edit_message_text(
                    int(chat_id), int(message_id), "`Userbot Restarted!`"
                )

                await super().delete_messages("me", x.message_id)
            except Exception as c_e:
                print(c_e)

            break

        await self.load_bio()

        me = await self.get_me()
        print(f"{self.__class__.__name__} v{self.version} (Layer {layer}) started on @{me.username}.\n"
              f"Hi!")

    async def load_bio(self):
        my_chat = await self.get_chat('self')
        self.bio = my_chat.description

    async def unload_bio(self):
        await self.send(functions.account.UpdateProfile(
            about=self.bio
        ))

    async def stop(self, *args):
        await self.unload_bio()

        await super().stop()
        print(f"{self.__class__.__name__} v{self.version} Stopped. Bye.")

    async def restart(self):
        await self.stop()



    @staticmethod
    async def extract_command_text(message: Message, error_message=None):
        """
        Extracts the command text. Either command params passed to the message
        or replied to message text.
        """
        if not error_message:
            error_message = 'No input text provided'

        cmd = message.command

        command_text = ""
        if len(cmd) > 1:
            command_text = " ".join(cmd[1:])
        elif message.reply_to_message and len(cmd) == 1:
            command_text = message.reply_to_message.text
        elif not message.reply_to_message and len(cmd) == 1:
            await message.edit(error_message)
            await asyncio.sleep(2)
            await message.delete()
            return

        return command_text
