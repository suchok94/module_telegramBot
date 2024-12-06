from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_feedback_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text='/Оставить_отзыв')
    builder.button(text='/Покажи_отзывы')

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)



def get_scores_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text='1')
    builder.button(text='2')
    builder.button(text='3')
    builder.button(text='4')
    builder.button(text='5')

    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True )

