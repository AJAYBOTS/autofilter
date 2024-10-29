import sys
import glob
import importlib
from pathlib import Path
import logging
import logging.config
import asyncio
from datetime import date, datetime
import pytz
from aiohttp import web
from pyrogram import Client, idle, __version__
from pyrogram.raw.all import layer
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from plugins import web_server
from opleechbot import OpleechAngelBot
from util.keepalive import ping_server
from opleechbot.clients import initialize_clients

# Configure logging
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

# Load plugin files
plugin_files = glob.glob("plugins/*.py")

async def Opleech_start():
    """Initialize the autofilter."""
    print('\nInitializing autofilter...')
    
    # Get bot info
    bot_info = await autofilterAngel.get_me()
    autofilterAngel.username = bot_info.username
    
    # Initialize clients and load plugins
    await initialize_clients()
    await load_plugins(plugin_files)
    
    # Ping server if on Heroku
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    
    # Fetch banned users and chats
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    await Media.ensure_indexes()
    
    # Store bot's user info
    me = await autofilterAngel.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    autofilterAngel.username = '@' + me.username
    
    # Log bot start information
    logging.info(f"{me.first_name} started for Pyrogram v{__version__} (Layer {layer}) as {me.username}.")
    logging.info(LOG_STR)
    logging.info(script.LOGO)
    
    # Send restart message to log channel
    await send_restart_message()
    
    # Set up and run web server
    await setup_web_server()

async def load_plugins(files):
    """Load plugins from the specified file list."""
    for file_path in files:
        with open(file_path) as file:
            plugin_name = Path(file.name).stem
            import_path = f"plugins.{plugin_name}"
            spec = importlib.util.spec_from_file_location(import_path, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            sys.modules[import_path] = module
            print(f"Opleech Imported => {plugin_name}")

async def send_restart_message():
    """Send a restart message to the log channel."""
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time_str = now.strftime("%H:%M:%S %p")
    message = script.RESTART_TXT.format(today, time_str)
    await OpleechAngelBot.send_message(chat_id=LOG_CHANNEL, text=message)

async def setup_web_server():
    """Set up and start the web server."""
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()

if __name__ == '__main__':
    try:
        asyncio.run(Opleech_start())
    except KeyboardInterrupt:
        logging.info('Service Stopped. Bye 👋')
