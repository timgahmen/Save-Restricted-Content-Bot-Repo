import os

from main.__init__ import bot as TelethonBot
from main.__init__ import SUDO_USERS
from telethon import events, Button


# ----------------------
# Nuke (restart bot)
# ----------------------

@TelethonBot.on(
    events.NewMessage(incoming=True,
                      from_users=SUDO_USERS,
                      pattern="/nuke",
                      func=lambda e: e.is_private))
async def shutdown(event):
    if event.sender_id in SUDO_USERS:
        await event.reply("Exited.")
        os._exit(1)
    else:
        await event.answer("You are not authorized to use this feature.")