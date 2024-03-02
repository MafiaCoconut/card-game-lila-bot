from aiogram import Dispatcher, F

from handlers import bot_messages, user_commands, intro_messages

dp = Dispatcher()
# dp.message.middleware(SomeMiddleware())
# dp.callback_query.outer_middleware(SomeMiddleware())


def include_routers():
    dp.include_routers(
        user_commands.router,
        bot_messages.router,
        intro_messages.router,
    )


def register_all_callbacks():

    dp.callback_query.register(intro_messages.introduce_lila_for_self_discovery_handler, F.data == "send_second_message")
    dp.callback_query.register(intro_messages.initiate_game_with_personal_request_handler, F.data == "send_third_message")
    dp.callback_query.register(intro_messages.start_the_game_handler, F.data == "start_game")
