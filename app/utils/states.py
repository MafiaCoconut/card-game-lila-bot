from aiogram.fsm.state import StatesGroup, State


class ExampleState(StatesGroup):
    example_state = State()


class EditLastMessageState(StatesGroup):
    message_id = State()



