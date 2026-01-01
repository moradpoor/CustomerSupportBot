TOKEN = "8221391584:AAEr7eEQAJeOkJyFb4iKzqvhe_KLJsxQ13k"
ADMIN = 75136055

from aiogram import Bot, Dispatcher, filters
from aiogram.types import Message
import asyncio
import json


bot = Bot(TOKEN)
dp = Dispatcher()

start_text = """
سلام به ربات پشتیبانی مشتریان خوش آمدید
 لطفا پیامتون رو ارسال کنید

"""

@dp.message(filters.Command("start"))
async def StartHandler(m: Message):
    await m.reply(
        start_text
    )

@dp.message()
async def Messagehandler(m: Message):
    usr = m.from_user
    if usr.id == ADMIN and m.reply_to_message:
        try:
            caption = m.reply_to_message.text
            data = json.loads(caption)
            UserId = data.get("user_id")
            MsgId = data.get("msgdid")
            await m.copy_to(UserId,reply_to_message_id=MsgId)
            await m.reply("پیام برای کاربر ارسال شد .")
        except Exception as OOHH:
            await m.reply(f"OOOOH : {str(OOHH)}")
        return
    msgid = m.message_id
    log = await m.forward(ADMIN)
    data = {
        "user_id" : usr.id,
        "full_name" : usr.full_name,
        "msgdid" : msgid,
        "username" : f"@{usr.username}" if usr.username else "None"
    }
    caption = json.dumps(data)
    await log.reply(caption)
    await m.reply(
        "پیام شما دریافت شد و بزودی به آن پاسخ میدهیم ."
    )

async def main():
    await dp.start_polling(bot)


asyncio.run(main())