from pyrogram import Client, filters
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")

DEVELOPER_NAME = "قِٰـِۢــآئــد آلِٰـِۢــشِٰـِۢــيِٰـِۢـآطِٰـِۢـيِٰـِـنَ"
DEVELOPER_USER = "@X_5NN"
SOURCE_CHANNEL = "@C_9KK"

app = Client(name=SESSION, api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

@app.on_message(filters.command("start") & filters.private)
async def start_handler(_, message):
    await message.reply_text(
        f"🎯 سورس جلسة Runs داخل حسابك\n"
        f"👤 المطور: [{DEVELOPER_NAME}](https://t.me/{DEVELOPER_USER.strip('@')})\n"
        f"📣 القناة: {SOURCE_CHANNEL}"
    )

app.run()
