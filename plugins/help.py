from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"ඔබගේ Youtube Video එකේ Link එක මාහට ලබාදෙන්න.(Playlist links දාන්න එපා😑)"
    await message.reply_text(helptxt)
