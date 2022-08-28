from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('5732803867:AAG3qrs5hMQFjbfEP5Rpb-1tbmmgnIg08fA')
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer("Hi, I am Sokhib.\nLet's see my portfolio!",
                         reply_markup=InlineKeyboardMarkup()
                         .add(InlineKeyboardButton(text="Portfolio",
                                                   web_app=WebAppInfo(url="https://sokhib-portfolio.netlify.app/"))))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

