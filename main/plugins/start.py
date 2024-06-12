import os

from main.__init__ import bot as TelethonBot
from main.__init__ import SUDO_USERS

from telethon import events, Button

S = '/' + 's' + 't' + 'a' + 'r' + 't'

START_PIC = "https://graph.org/file/4acc1e7a441776e31f883.jpg"
TEXT = "👋 Hi, I am 'Save Restricted Content' bot Made with ❤️ by __**TimmyGahmen**__\n\n✅ Send me the Link of any message of Restricted Channels to Clone it here.\nFor private channel's messages, send the Invite Link first."


# ----------------------
# Thumbnail (set)
# ----------------------

@TelethonBot.on(
    events.callbackquery.CallbackQuery(data="set"))
async def sett(event):
    if event.sender_id in SUDO_USERS:
        TelethonBot = event.client
        button = await event.get_message()
        msg = await button.get_reply_message()
        await event.delete()
        async with TelethonBot.conversation(event.chat_id) as conv:
            xx = await conv.send_message(
                "Send me any image for thumbnail as a `reply` to this message.")
            x = await conv.get_reply()
            if not x.media:
                xx.edit("No media found.")
            mime = x.file.mime_type
            if "png" not in mime and "jpg" not in mime and "jpeg" not in mime:
                return await xx.edit("No image found.")
            await xx.delete()
            
            t = await event.client.send_message(event.chat_id, 'Trying.')
            path = await event.client.download_media(x.media)
            if os.path.exists(f'{event.sender_id}.jpg'):
                os.remove(f'{event.sender_id}.jpg')
            os.rename(path, f'./{event.sender_id}.jpg')
            await t.edit("Temporary thumbnail saved!")
    else:
        await event.answer("You are not authorized to use this feature.")


# ----------------------
# Thumbnail (remove)
# ----------------------

@TelethonBot.on(
    events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):
    if event.sender_id in SUDO_USERS:
        TelethonBot = event.client
        await event.edit('Trying.')
        try:
            os.remove(f'{event.sender_id}.jpg')
            await event.edit('Removed!')
        except Exception:
            await event.edit("No thumbnail saved.")
    else:
        await event.answer("You are not authorized to use this feature.")


# ----------------------
# Menue
# ----------------------

@TelethonBot.on(
    events.NewMessage(incoming=True,
                      #from_users=AUTH,
                      from_users=SUDO_USERS,
                      pattern=f"{S}",
                      func=lambda e: e.is_private))
async def start_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.inline("SET THUMB.", data="set"),
         Button.inline("REM THUMB.", data="rem")],
        [Button.url("Join Channel", url="https://t.me/Tim_Bots")]
    ]
    # Sending photo with caption and buttons
    await TelethonBot.send_file(
        event.chat_id,
        file=START_PIC,
        caption=TEXT,
        buttons=buttons
    )
