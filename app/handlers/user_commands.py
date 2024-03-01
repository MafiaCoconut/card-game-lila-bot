import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from utils.logs import set_func, set_func_and_person
from utils.bot import bot

router = Router()
tag = "user_commands"
status = "debug"


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_start_handler"
    set_func(function_name, tag, status)

    await message.answer("Добро пожаловать!")


@router.message(Command("help"))
async def command_help_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_help_handler"
    set_func_and_person(function_name, tag, message)

    await message.answer("Вывод help информации")


@router.message(Command("send_voice"))
async def command_send_voice_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_send_voice_handler"
    set_func_and_person(function_name, tag, message)

    voice = FSInputFile("path_to_file.ogg")
    await bot.send_voice(chat_id=message.chat.id, voice=voice, caption='caption')



