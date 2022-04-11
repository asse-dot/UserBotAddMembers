import ast
import logging
import os
from configparser import ConfigParser
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler


from userbot.userbot import UserBot

# Created logs folder if it is not there. Needed for logging.
# Extra details
__version__ = "0.2.0"
__author__ = "athphane"

UserBot = UserBot(__version__)

# Read from config file
config_file = 'userbot.ini'
config = ConfigParser()
config.read(config_file)


# Global Variables
CMD_HELP = {}
client = None
START_TIME = datetime.now()