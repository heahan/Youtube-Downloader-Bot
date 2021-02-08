from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("👻Telegram Group👻", url="https://t.me/SL_Dark_Hackers")],
        [InlineKeyboardButton(
            "🤗ඔබගේ ගැටලු යොමුකරන්න🤗", url="https://t.me/A_T_Heshan0")],
        [InlineKeyboardButton("🤬My Master🤬", url="https://t.me/A_T_Heshan0")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
