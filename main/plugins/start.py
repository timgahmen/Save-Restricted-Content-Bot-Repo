import os
from .. import bot as TelethonBot
from telethon import events, Button
from telethon.tl.types import InputMediaPhoto
from .. import SUDO_USERS

# S = '/' + 's' + 't' + 'a' + 'r' + 't'
S = "/start"

START_PIC = "https://graph.org/file/01200b16e83fe87987d4e.jpg"
TEXT = "👋 Hi, I am 'Save Restricted Content' bot Made with ❤️ by __**TimmyGahmen**__\n\n✅"


def is_set_button(data):
    return data == "set"

def is_rem_button(data):
    return data == "rem"

@TelethonBot.on(events.CallbackQuery(pattern=b"set"))
async def sett(event):    
    TelethonBot = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with TelethonBot.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("Send me any image for thumbnail as a `reply` to this message.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
            return
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("Temporary thumbnail saved!")

@TelethonBot.on(events.CallbackQuery(pattern=b"rem"))
async def remt(event):  
    TelethonBot = event.client            
    await event.edit('Trying... to save Bamby ... Wait')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        



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
        [Button.inline("SET THUMB", data="set"),
         Button.inline("REM THUMB", data="rem")],
        [Button.url("Join Channel", url="https://telegram.dog/dev_gagan")]
    ]

    # Sending photo with caption and buttons
    await TelethonBot.send_file(
        event.chat_id,
        file=START_PIC,
        caption=TEXT,
        buttons=buttons
    )

