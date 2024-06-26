from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from tgbot.messages.handlers_msg import UserHandlerMessages

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply(UserHandlerMessages.GREETINGS)


@user_router.message(Command('help'))
async def help(message: Message):
    await message.reply(UserHandlerMessages.HELP)
