import re
from os import environ, getenv
from Script import script 

# ID pattern for validating numeric IDs
id_pattern = re.compile(r'^\d+$')

# Function to determine if a setting is enabled based on string input
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', "True"), True)

PICS = environ.get('PICS', 'https://graph.org/file/8a783d2331c9b62205308.jpg').split()  # Sample picture
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/62efbcc4e7580b76530ba.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/33ff45785b855453f29f1.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/9133dc596eabc73750774.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) for admin in environ.get('ADMINS', '1170337923').split() if id_pattern.match(admin)]
CHANNELS = [int(ch) for ch in environ.get('CHANNELS', '-1002103097924').split() if id_pattern.match(ch)]
auth_users = [int(user) for user in environ.get('AUTH_USERS', '-1001961465245').split() if id_pattern.match(user)]
AUTH_USERS = auth_users + ADMINS if auth_users else []
PREMIUM_USER = [int(user) for user in environ.get('PREMIUM_USER', '').split() if id_pattern.match(user)]
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.match(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001961465245')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002103097924')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.match(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.match(support_chat_id) else None
NO_RESULTS_MSG = is_enabled(environ.get("NO_RESULTS_MSG", "False"), False)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://AJAYBOTS:AJAYBOTS@cluster0.tagclvq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Other configurations
VERIFY = is_enabled(environ.get('VERIFY', "False"), False)
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'gyanilinks.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '1fa3b4cd965dc758f0086b99d18aa0df31ac2571')
IS_SHORTLINK = is_enabled(environ.get('IS_SHORTLINK', "False"), False)
DELETE_CHANNELS = [int(dch) for dch in environ.get('DELETE_CHANNELS', '0').split() if id_pattern.match(dch)]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled(environ.get('MAX_BTN', "True"), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+lULqM33QsWMxNThl')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/MZ_OFCL')
TUTORIAL = environ.get('TUTORIAL', '')
IS_TUTORIAL = is_enabled(environ.get('IS_TUTORIAL', "True"), True)
MSG_ALRT = environ.get('MSG_ALRT', 'HELLO MAWA❤️')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002137243887'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'MOVIEZONECHAT1')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
AUTO_FFILTER = is_enabled(environ.get('AUTO_FFILTER', "True"), True)
AUTO_DELETE = is_enabled(environ.get('AUTO_DELETE', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in environ.get('FILE_STORE_CHANNEL', '-1002045014432').split() if id_pattern.match(ch)]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

# Supported languages and seasons
LANGUAGES = ["malayalam", "mal", "tamil", "tam", "english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = [f"season {i}" for i in range(1, 11)]

# Online Stream and Download settings
NO_PORT = is_enabled(environ.get('NO_PORT', "False"), False)
APP_NAME = environ.get('APP_NAME', 'opleech') if 'DYNO' in environ else None
ON_HEROKU = 'DYNO' in environ
BIND_ADDRESS = getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0')
FQDN = getenv('FQDN', BIND_ADDRESS) if not ON_HEROKU or getenv('FQDN') else f"{APP_NAME}opleech"
URL = f"https://opleech-filter-bot-fg4c.onrender.com/" if ON_HEROKU or NO_PORT else f"https://opleech-filter-bot-fg4c.onrender.com/"
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = environ.get('SESSION_NAME', 'opleechbot')
MULTI_CLIENT = False
name = environ.get('name', 'OpleechAngel')
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes

# SSL settings
HAS_SSL = is_enabled(getenv('HAS_SSL', "False"), False)
URL = f"https://opleech-filter-bot-fg4c.onrender.com/" if HAS_SSL else URL

# Logging configuration
LOG_STR = "Current Customized Configurations are:\n"
LOG_STR += "IMDB Results are enabled, Bot will be showing IMDb details for your queries.\n" if IMDB else "IMDb Results are disabled.\n"
LOG_STR += "P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending files directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled; files will be sent in PM.\n"
LOG_STR += "SINGLE_BUTTON is found; filename and file size will be shown in a single button instead of two separate buttons.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled; filename and file size will be shown as different buttons.\n"
LOG_STR += f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}; your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION found; default captions of the file will be used.\n"
LOG_STR += "Long IMDb storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled; plot will be shorter.\n"
LOG_STR += "Spell Check Mode is enabled; the bot will be suggesting related movies if the movie is not found.\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled.\n"
LOG_STR += f"MAX_LIST_ELM found; long list will be shortened to the first {MAX_LIST_ELM} elements.\n" if MAX_LIST_ELM else "Full list of casts and crew will be shown in IMDb template; restrict them by adding a value to MAX_LIST_ELM.\n"
LOG_STR += f"Your current IMDb template is {IMDB_TEMPLATE}.\n"
