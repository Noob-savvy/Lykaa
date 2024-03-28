import logging 
import time
from Abg import patch

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram import filters

import config

#logger

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

# exporting of modules

logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)
boot = time.time()
mongo = MongoCli(config.MONGO_DB_URL)
db = mongo.Anonymous
Mongo = MongoCli(config.MONGO_URL)
Db = Mongo.divu
OWNER = config.OWNER_ID
filters = filters  # This re-exports filters
LOGGER_ID = config.LOGGER_ID

#bot client

class savvychat(Client):
    def __init__(self):
        super().__init__(
            name="savvychat",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            lang_code="en",
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.DEFAULT,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention


    async def stop(self):
        await super().stop()


savvychat = savvychat()
