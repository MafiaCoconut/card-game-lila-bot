from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

import time

from icecream import ic

from handlers.intro_messages import start_the_game_handler
from keyboards.inline import create_cards_5_buttons, create_cards_keyboard
from utils.logs import set_func, set_func_and_person, set_inside_func
from utils.bot import bot
from utils.states import EditLastMessageState
from data.cards import cards_list

tag = "cards_handler"


async def send_card_info_handler(call: CallbackQuery, state: FSMContext):
    function_name = "send_card_info_handler"
    set_func_and_person(function_name, tag, call.message)

    await call.answer()
    card_number = call.data[call.data.find('_') + 1:call.data.find(':')]
    card_group = [int(call.data[call.data.find(':') + 1:call.data.find('-')]), int(call.data[call.data.find('-') + 1:])]

    text = f"*{cards_list[card_number]['title']}*\n\n" + cards_list[card_number]['description'].replace('\n', '\n\n')

    try:
        new_card = await call.message.edit_text(
            text=text,
            reply_markup=create_cards_keyboard(start=card_group[0],
                                               end=card_group[1]),
            parse_mode="MARKDOWN")

        await state.update_data(message_id=new_card.message_id)
        await call.message.answer("Проанализируй текст этой карты и запиши ключевые моменты в свой бланк.")
        await start_the_game_handler(call, state)

    except Exception as e:
        set_inside_func(data=e, function=function_name, tag=tag, status="warning")



async def card_pagination_handler(call: CallbackQuery):
    function_name = "card_pagination_handler"
    set_func_and_person(function_name, tag, call.message)

    await call.answer()
    list_of_cards = call.data[call.data.rfind("_") + 1:].split('-')

    await call.message.edit_reply_markup(reply_markup=create_cards_keyboard(start=int(list_of_cards[0]),
                                                                            end=int(list_of_cards[1])))
