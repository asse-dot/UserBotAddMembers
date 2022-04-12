
from configparser import ConfigParser
from datetime import datetime



from userbot.userbot import UserBot

# Created logs folder if it is not there. Needed for logging.
# Extra details
__version__ = "0.0.0"
__author__ = "asse"

UserBot = UserBot(__version__)


# Read from config file
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)


# Global Variables
CMD_HELP = {}
client = None
START_TIME = datetime.now()

id_channel = -1001572336038
id_group = -1001693987391