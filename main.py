from pyrogram import Client

API_ID = 29366148
API_HASH = "cdae9daaa962cfdf1ec88c5333aadedf"
SESSION = "هنا_يضع_المستخدم_جلسة_بايجرام"

DEVELOPER_NAME = "قِٰـِۢــآئــد آلِٰـِۢــشِٰـِۢــيِٰـِۢـآطِٰـِۢـيِٰـِـنَ"
DEVELOPER_USER = "@X_5NN"
SOURCE_CHANNEL = "@C_9KK"

app = Client(session_name=SESSION, api_id=API_ID, api_hash=API_HASH)

@app.on_message()
async def handler(client, message):
    await message.reply_text("البوت يعمل بنجاح ✅")

app.run()