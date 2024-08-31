from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import F, Router
from filters.chat_filters import ChatTypeFilter
import requests
import random
from aiogram import Bot, types

user_privat_router = Router()
user_privat_router.message.filter(ChatTypeFilter(['private']))

    
@user_privat_router.message(Command('generate_password'))
async def generate_password_handler(message: Message):
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c= "0123456789"
    d = "[]{}()*'/,_-!?"
    all = a+b+c+d
    length = 16    
    password = "".join(random.sample (all, length))
    await message.answer(f"Your random password: {password}")



@user_privat_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello {message.from_user.full_name} i can help you make a new password")