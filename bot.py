import asyncio
import random
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

stickdict = {
    '1': {'CAACAgIAAxkBAAECSUFlbi5MZcY6SLooI4QVK7bhIcpBRQAC9S8AAuvCaEiGJlj2aFBJ2TME'},
    '2': {'CAACAgIAAxkBAAECSUNlbi5PLFMaE4FFKAABx84p9pVGPFkAAogUAALdVIhIauZXg0ZJaDgzBA'},
    '3': {'CAACAgIAAxkBAAECSUVlbi5QHmm61NecjbLr4th_5p_DeAACmRMAAkHl-Uj-G83s7D1abzME'}
}

kb = [
    [types.KeyboardButton(text="Рандомный стикер")]
]

keyboard = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True
)

bot = Bot(token='')
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет", reply_markup=keyboard)


@router.message(F.text.lower() == "рандомный стикер")
async def randstick(message: types.Message):
    sticker_id = stickdict[random.choice(list(stickdict.keys()))]
    sticker_id = ''.join(sticker_id)
    await bot.send_sticker(message.chat.id, sticker=r'{sticker_id}'.format(sticker_id=sticker_id),
                           reply_markup=keyboard)


if __name__ == "__main__":
    asyncio.run(main())
