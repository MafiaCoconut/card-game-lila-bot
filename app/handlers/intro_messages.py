from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

import time

from utils.logs import set_func, set_func_and_person
from utils.bot import bot
from utils.states import EditLastMessageState

# from data.text_debug import (
from data.text import (
    introduce_game_basics, essence_of_the_game, rules_of_the_game,
    forms_for_notes, recommendations, start_game, remaining_time
)
from filters.is_admin import IsAdmin
from keyboards.inline import create_one_inline_button, create_two_inline_buttons, create_cards_5_buttons, \
    create_pagination_cards_keyboard

router = Router()
tag = "intro_messages"


async def introduce_lila_for_self_discovery_handler(call: CallbackQuery, state: FSMContext) -> None:
    function_name = "introduce_lila_for_self_discovery_handler"
    set_func_and_person(function_name, tag, call.message)

    data = await state.get_data()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=data["message_id"], reply_markup=None)
    await call.answer()

    await bot.send_animation(chat_id=call.message.chat.id, animation=FSInputFile("app/data/animation(1).gif"),
                             caption=essence_of_the_game)
    # await call.message.answer(essence_of_the_game)
    await rules_of_the_game_handler(call)
    await forms_for_notes_handler(call, state)


async def rules_of_the_game_handler(call: CallbackQuery) -> None:
    function_name = "rules_of_the_game_handler"
    set_func_and_person(function_name, tag, call.message)

    time_message = await call.message.answer(rules_of_the_game + remaining_time.replace('_', '15'), )

    for i in range(14, -1, -1):
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=time_message.message_id,
                                    text=rules_of_the_game + remaining_time.replace('_', str(i)))
        time.sleep(1)

    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=time_message.message_id,
                                text=rules_of_the_game)


async def forms_for_notes_handler(call: CallbackQuery, state: FSMContext):
    function_name = "forms_for_notes_handler"
    set_func_and_person(function_name, tag, call.message)

    new_message = await call.message.answer_animation(
        caption=forms_for_notes + remaining_time.replace('_', '15'),
        animation=FSInputFile("app/data/animation(1).gif"))

    await call.message.answer_document(document=FSInputFile("app/data/blank_for_notes.jpg"))
    await state.update_data(message_id=new_message.message_id)

    for i in range(14, -1, -1):
        await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=new_message.message_id,
                                       caption=forms_for_notes + remaining_time.replace('_', str(i), ))
        time.sleep(1)

    await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=new_message.message_id,
                                   caption=forms_for_notes,
                                   reply_markup=create_one_inline_button(text="Конечно готов",
                                                                         call_data="send_third_message"))


async def initiate_game_with_personal_request_handler(call: CallbackQuery, state: FSMContext):
    function_name = "initiate_game_with_personal_request_handler"
    set_func_and_person(function_name, tag, call.message)

    await call.answer()
    data = await state.get_data()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=data["message_id"], reply_markup=None)

    new_message = await call.message.answer(recommendations + remaining_time.replace('_', '15'))
    await state.update_data(message_id=new_message.message_id)

    for i in range(14, -1, -1):
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=new_message.message_id,
                                    text=recommendations + remaining_time.replace('_', str(i), ))
        time.sleep(1)

    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=new_message.message_id,
                                text=recommendations + "\n\nТеперь нажимай кнопку «Начать игру»",
                                reply_markup=create_one_inline_button(text="Начать игру", call_data="start_game"))


async def start_the_game_handler(call: CallbackQuery, state: FSMContext):
    function_name = "start_the_game_handler"
    set_func_and_person(function_name, tag, call.message)

    data = await state.get_data()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=data["message_id"], reply_markup=None)
    await state.clear()

    await call.message.answer_photo(photo=FSInputFile('app/data/cards_plug.jpg'))
    await call.message.answer(text=start_game, reply_markup=create_pagination_cards_keyboard())
    await call.answer()
