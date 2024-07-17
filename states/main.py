from aiogram.dispatcher.filters.state import State, StatesGroup


class Example(StatesGroup):
    change_leangue = State()
    change_about = State()
    back = State()
    