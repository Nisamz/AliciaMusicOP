from os import path

from pyrogram import Client as Aliciabot
from pyrogram.types import Message, Voice

from AliciaMusic.callsmusic import callsmusic, queues

from AliciaMusic.converter import converter
from AliciaMusic.downloaders import youtube

from AliciaMusic.config import BOT_NAME as bn, DURATION_LIMIT, BOT_USERNAME, BOT_PIC
from AliciaMusic.helpers.filters import command, other_filters
from AliciaMusic.helpers.decorators import errors
from AliciaMusic.helpers.errors import DurationLimitError
from AliciaMusic.helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Aliciabot.on_message(command("ply") & other_filters)
@errors
async def play(_, message: Message):

    lel = await message.reply("🔄 **Processing**")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=f"{bn}",
                        url="{BOT_USERNAME}")
                   
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ {DURATION_LIMIT} minute(s) Too long audio! sorry i can't play‼️"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("❗ Please give me audio for play🥲")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        await lel.edit(f"#⃣ **Queued** at position {position}!")
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        await message.reply_photo(
        photo= BOT_PIC,
        reply_markup=keyboard,
        caption="▶️ **Playing** here the song requested by🔥{}!".format(
        message.from_user.mention()
        ),
    )
        return await lel.delete()
