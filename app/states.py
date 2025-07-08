from aiogram.fsm.state import State, StatesGroup


class SampleState(StatesGroup):
    waiting_for_input = State()
