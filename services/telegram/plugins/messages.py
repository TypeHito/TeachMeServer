from pyrogram import Client
from pyrogram import filters


@Client.on_message(filters.text)
async def message_hello(client, message):
    await message.reply_text("message, hello!")