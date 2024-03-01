from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)

rkr = ReplyKeyboardRemove()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Главное меню")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Запустить")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)


def create_one_reply_button(text: str):
    button = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text)],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        selective=True
    )
    return button


def create_two_reply_button(text1: str, text2: str):
    buttons = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text1), KeyboardButton(text=text2)],
        ],
        resize_keyboard=True,
        one_time_keyboard=True,
        selective=True
    )
    return buttons