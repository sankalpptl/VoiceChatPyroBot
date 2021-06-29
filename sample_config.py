# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 2500594
API_HASH = "6704f1885e4cc07762e1684128da398d"

# Get this from @Botfather
TOKEN = "1890611626:AAGgIHjx8cAX7RCWVHOvX6BfZLGMzvnp8sE"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    255965711,
    158661264
]

# The ID of the group where your bot streams
GROUP = -1001402753006

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Send "now playing" messages to the group
LOG = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 10

# No need to touch the following.
LOG_GROUP = GROUP if LOG else None
SUDO_FILTER = filters.user(SUDO_USERS)
