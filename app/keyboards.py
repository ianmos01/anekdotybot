from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def start_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Start")
    return builder.as_markup(resize_keyboard=True)


def example_inline():
    builder = InlineKeyboardBuilder()
    builder.button(text="Press", callback_data="press")
    return builder.as_markup()
