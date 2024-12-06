from aiogram import Router
from aiogram.filters import Command
from aiogram import types
from aiogram import F
import datetime

router = Router()

@router.message(Command('weekday'))
async def weekday_handler(message: types.Message):
    weekday = datetime.datetime.today().weekday()