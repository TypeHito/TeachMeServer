import pyrogram
from services.telegram.utils.const import BOT_TOKEN, api_id, api_hash


plugins = dict(root="plugins")


app = pyrogram.Client('DEVTech', api_id=api_id, api_hash=api_hash,
                      bot_token=BOT_TOKEN, plugins=plugins)

print("Bot started!")
app.run()
