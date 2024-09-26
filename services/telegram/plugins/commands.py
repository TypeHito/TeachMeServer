from pyrogram import Client
from pyrogram import filters


@Client.on_message(filters.command("hello"))
async def command_hello(client, message):
    await message.reply_text("command, world!")