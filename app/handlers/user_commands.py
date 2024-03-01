from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from utils.logs import set_func, set_func_and_person
from utils.bot import bot
from data.text import text1
from filters.is_admin import IsAdmin
from keyboards.inline import create_one_inline_button
router = Router()
tag = "user_commands"
status = "debug"


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_start_handler"
    set_func(function_name, tag, status)

    await message.answer(text1, reply_markup=create_one_inline_button(text="Запустить",
                                                                      call_data="send_second_message"))


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


@router.message(F.text == '/send_user_logs', IsAdmin())
async def admin_send_user_logs_with_command(message: Message):
    function_name = "admin_send_user_logs_with_command"
    set_func(function_name, tag)

    text = "Пользовательские логи отправлены"

    await message.answer_document(text=text, document=FSInputFile(path='user_data.log'))


@router.message(F.text == '/send_system_logs', IsAdmin())
async def admin_send_system_logs_with_command(message: Message):
    function_name = "admin_send_system_logs_with_command"
    set_func(function_name, tag)

    text = "Логи отправлены"

    await message.answer_document(text=text, document=FSInputFile(path='system_data.log'))


# @router.message(F.text == '/test')
# async def admin_test(message: Message):
#     function_name = "admin_test"
#     set_func(function_name, tag)
#
#     await message.answer(text=str(message.message_id))
#     # text = "Логи отправлены"

    # await message.answer_document(text=text, document=FSInputFile(path='system_data.log'))

