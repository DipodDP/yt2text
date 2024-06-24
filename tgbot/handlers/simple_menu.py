from aiogram import Router, F
from aiogram.types import (
    BufferedInputFile,
    Message,
    ReplyKeyboardRemove,
)
from betterlogging import logging

from tgbot.services.get_transcription import get_id_from_link, get_transcription


logger = logging.getLogger(__name__)

menu_router = Router()


@menu_router.message(F.text)
async def show_menu(message: Message):
    if message.text:
        logger.info(f"Message text: {message.text}")

        video_id = get_id_from_link(message.text)
        logger.debug(f"Video ID {video_id}")

        if not video_id:
            await message.answer(
                "Invalid YouTube URL", reply_markup=ReplyKeyboardRemove()
            )
            return

        transcription = await get_transcription(video_id)

        if transcription:
            logger.debug(f"Transcription: {transcription}")

            if len(transcription) > 4096:
                file_content = transcription.encode("utf-8")
                file = BufferedInputFile(file_content, "transcription.txt")
                await message.answer(
                    "The transcription is too long to display here. It has been sent as a file.",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await message.answer_document(file)
            else:
                await message.answer(
                    "Here's your video transcription:",
                    reply_markup=ReplyKeyboardRemove(),
                )
                await message.answer(transcription)

        else:
            logger.info("Transcription not found")
            await message.answer(
                "Transcription not found for the provided video.",
                reply_markup=ReplyKeyboardRemove(),
            )
