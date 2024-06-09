import os

from dotenv import load_dotenv

load_dotenv(
    "config.env" if os.path.isfile("config.env") else "sample_config.env"
)

BOT_TOKEN = os.environ.get("6370891060:AAHjFCrStAuz7ng0bpAUJDrqxJhnL_e9a1k")
API_ID = int(os.environ.get(24638763))
SESSION_STRING = os.environ.get("BABO-fIWQP2VSTFEHEBdMhJ9PufWtuo7FrLaqhhGglOmYpJ7HG4RL0wkrmXmqHXzRqh6PQcLIbpXWPliOhuCIpgPXYdlaFGvNV3e4HxAMcqd49grz2tjykvLnpxnrf44byHQ5qxjLYX0GsJb84PFnBvt2P-OmaBlW-hKvqf_A4twGG_ZrOdaTsbfvR92lbnevb5LnLcYL6M4fPVsCQQjBkxIo7R5LCJeGnfJO0kXFkiPkkqWFUC-wi0ElZ6C1b1uZCTaKG4ldiVBN9xilbIUYInxgDseE5t12_W_wJYDHZ1vYnhV72NheXn5oamUyh4_Aypl28lEyu3PD_oOkA_us5_AAAAAAVO5jmQA", "")
API_HASH = os.environ.get("e02a72843ababb75de3c4f3aa2ce8d75")
USERBOT_PREFIX = os.environ.get("USERBOT_PREFIX", ".")
PHONE_NUMBER = os.environ.get("+989999135956")
SUDO_USERS_ID = list(map(int, os.environ.get("SUDO_USERS_ID", "").split()))
LOG_GROUP_ID = int(os.environ.get("LOG_GROUP_ID"))
GBAN_LOG_GROUP_ID = int(os.environ.get("GBAN_LOG_GROUP_ID"))
MESSAGE_DUMP_CHAT = int(os.environ.get("MESSAGE_DUMP_CHAT"))
WELCOME_DELAY_KICK_SEC = int(os.environ.get("WELCOME_DELAY_KICK_SEC", 600))
MONGO_URL = os.environ.get("MONGO_URL")
ARQ_API_KEY = os.environ.get("ARQ_API_KEY")
ARQ_API_URL = os.environ.get("ARQ_API_URL", "https://arq.hamker.dev")
LOG_MENTIONS = os.environ.get("LOG_MENTIONS", "True").lower() in ["true", "1"]
RSS_DELAY = int(os.environ.get("RSS_DELAY", 300))
PM_PERMIT = os.environ.get("PM_PERMIT", "True").lower() in ["true", "1"]
