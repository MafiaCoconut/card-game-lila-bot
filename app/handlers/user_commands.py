from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InputFile
from aiogram.fsm.context import FSMContext
from icecream import ic

from utils.logs import set_func, set_func_and_person
from utils.bot import bot

from data.text import introduce_game_basics, start_game
# from data.text_debug import introduce_game_basics, start_game

from utils.states import EditLastMessageState
from filters.is_admin import IsAdmin
from keyboards.inline import create_one_inline_button, create_two_inline_buttons, create_pagination_cards_keyboard

router = Router()
tag = "user_commands"
status = "debug"


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_start_handler"
    set_func(function_name, tag, status)

    await state.set_state(EditLastMessageState.message_id)
    # await bot.send_video_note()
    # new_message = await bot.send_animation(chat_id=message.chat.id, animation=FSInputFile("data/lila_gif(1).gif"),
    #                    caption=introduce_game_basics,
    #                    reply_markup=create_two_inline_buttons(text1="Давай",
    #                                            call_data1="send_second_message",
    #                                            text2="Уже играл",
    #                                            call_data2="start_game"))
    # ic(new_message)
    new_message = await message.answer(
        text=introduce_game_basics,
        reply_markup=create_two_inline_buttons(text1="Давай",
                                               call_data1="send_second_message",
                                               text2="Уже играл",
                                               call_data2="start_game"))

    await state.update_data(message_id=new_message.message_id)


# @router.message(Command("help"))
# async def command_help_handler(message: Message, state: FSMContext) -> None:
#     function_name = "command_help_handler"
#     set_func_and_person(function_name, tag, message)
#
#     await message.answer("Вывод help информации")


# @router.message(Command("send_voice"))
# async def command_send_voice_handler(message: Message, state: FSMContext) -> None:
#     function_name = "command_send_voice_handler"
#     set_func_and_person(function_name, tag, message)
#
#     voice = FSInputFile("path_to_file.ogg")
#     await bot.send_voice(chat_id=message.chat.id, voice=voice, caption='caption')


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


@router.message(Command("main_menu"))
async def command_main_menu_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_main_menu_handler"
    set_func_and_person(function_name, tag, message)
    await message.answer_photo(photo=FSInputFile("app/data/cards_plug.jpg"))
    await message.answer(start_game, reply_markup=create_pagination_cards_keyboard())


async def menu_main_callback_handler(call: CallbackQuery):
    function_name = "command_main_menu_handler"
    set_func_and_person(function_name, tag, call.message)

    await call.message.edit_text(text=start_game, reply_markup=create_pagination_cards_keyboard())
