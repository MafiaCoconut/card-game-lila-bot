from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from utils.logs import set_func, set_func_and_person
from utils.bot import bot
from data.text import text2, essence_of_the_game, rules_of_the_game, forms_for_notes, recommendations, start_game
from filters.is_admin import IsAdmin
from keyboards.inline import create_one_inline_button, create_two_inline_buttons

router = Router()
tag = "intro_messages"


async def introduce_game_basics(call: CallbackQuery):
    function_name = "introduce_game_basics"
    set_func_and_person(function_name, tag, call.message)

    await call.message.answer(text2,
                              reply_markup=create_two_inline_buttons(text1="Давай", call_data1="send_third_message",
                                                                     text2="Уже играл", call_data2="start_game"), )
    await call.answer()


async def introduce_lila_for_self_discovery(call: CallbackQuery):
    function_name = "introduce_lila_for_self_discovery"
    set_func_and_person(function_name, tag, call.message)

    await call.message.answer(essence_of_the_game)
    await call.message.answer(rules_of_the_game)

    # TODO добавить таймер на 15 секунд

    await call.message.answer(forms_for_notes, reply_markup=create_one_inline_button(text="Конечно готов",
                                                                                     call_data="send_fourth_message"))
    await call.answer()


async def initiate_game_with_personal_request(call: CallbackQuery):
    function_name = "initiate_game_with_personal_request"
    set_func_and_person(function_name, tag, call.message)

    await call.message.answer(recommendations, reply_markup=create_one_inline_button(text="Начать игру",
                                                                                     call_data="start_game"))
    await call.answer()


async def start_the_game(call: CallbackQuery):
    function_name = "start_game"
    set_func_and_person(function_name, tag, call.message)

    await call.message.answer(start_game)
    await call.answer()



