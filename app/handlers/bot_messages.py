from aiogram import Router, types, F
from aiogram.types import Message
import os
from utils.logs import set_func, set_func_and_person
from handlers import auxiliary
from keyboards import reply, inline
from utils.bot import bot

tag = "bot_messages"
router = Router()


@router.message(F.voice)
# @router.message(F.content_type.in_({'sticker'}))
async def echo_handler(message: Message) -> None:
    """Функция вывода заглушки на необъявленное сообщение/команду"""
    # send_log(message.text, message.chat.username)

    for i in range(1, 73):

        if os.path.isfile(f"data/{i}.ogg"):
            pass
            # await message.answer(f"Карточка с номером {i} уже существует")

            # print()

        else:
            file = await bot.get_file(message.voice.file_id)
            fp = file.file_path

            await bot.download_file(fp, destination=f"data/{i}.ogg")
            await message.answer(f"Добавлена карточка с номером {i} уже существует")

            # print(f"Добавлена карточка с номером {i} уже существует")
            break



@router.message()
# @router.message(F.content_type.in_({'sticker'}))
async def echo_handler(message: Message) -> None:
    """Функция вывода заглушки на необъявленное сообщение/команду"""
    # send_log(message.text, message.chat.username)
    await message.answer("Команды не найдено. Повторите попытку ввода.")





