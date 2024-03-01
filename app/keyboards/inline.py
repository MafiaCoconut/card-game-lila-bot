from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def get_main_menu():
    main_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='main-menu', callback_data="menu_main")]]
    )
    return main_menu


def get_go_to(where):
    go_to = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='back', callback_data=f"menu_{where}"),
             InlineKeyboardButton(text='to-menu-main', callback_data="menu_main")]
        ]
    )
    return go_to


def get_settings_language_from_start():
    languages = get_main_menu()
    menu_main = get_go_to("main")
    languages.inline_keyboard.append(menu_main.inline_keyboard[0])

    return languages


def create_one_inline_button(text, call_data):
    button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=call_data)]
        ]
    )
    return button


def create_two_inline_buttons(text1, call_data1, text2, call_data2):
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text1, callback_data=call_data1),
             InlineKeyboardButton(text=text2, callback_data=call_data2)]
        ]
    )
    return buttons





