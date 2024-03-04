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


def create_cards_5_buttons():
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1", callback_data="card_1"),
             InlineKeyboardButton(text="2", callback_data="card_2"),
             InlineKeyboardButton(text="3", callback_data="card_3"),
             InlineKeyboardButton(text="4", callback_data="card_4"),
             InlineKeyboardButton(text="5", callback_data="card_5")]
        ]
    )
    return buttons


def create_pagination_cards_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1-10", callback_data="list_of_cards_1-10"),
             InlineKeyboardButton(text="11-20", callback_data="list_of_cards_11-20"),
             InlineKeyboardButton(text="21-30", callback_data="list_of_cards_21-30"),
             InlineKeyboardButton(text="31-40", callback_data="list_of_cards_31-40")],
            [InlineKeyboardButton(text="41-50", callback_data="list_of_cards_41-50"),
             InlineKeyboardButton(text="51-60", callback_data="list_of_cards_51-60"),
             InlineKeyboardButton(text="61-72", callback_data="list_of_cards_61-72"),
             ]
        ]
    )
    return keyboard


def create_cards_keyboard(start: int, end: int):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[], [], []]
    )

    if start == 61:
        n, m = 5, 9
    else:
        n, m = 4, 8
    count_val = 1
    k = 0
    for i in range(start, end+1):
        if count_val == n or count_val == m:
            k += 1

        count_val += 1
        keyboard.inline_keyboard[k].append(InlineKeyboardButton(text=str(i), callback_data=f"card_{i}:{start}-{end}"))

    keyboard.inline_keyboard.append([InlineKeyboardButton(text="В главное меню", callback_data="to_menu_main")])
    return keyboard




"""
1 2 3 4 5 6 7 8 9 10
11 12 13 14 15 16 17 18 19


1-10 11-20 21-30 31-40 41-50 51-60 61-70 71-72
1-8 9-16 17-26 27-36 37-46 47-56 57-66 67-72
1-9 10-19 20-29 30-39 40-49 50-59 60-69 

"""