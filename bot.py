import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

CHANNEL_URL = "https://t.me/Expose_Mat_Karo"
GROUP_URL = "https://t.me/Context_Idhar_Hain"
BACKUP_URL = "https://t.me/Mat_Kar_Bhai"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("ভাইরাল ভিডিও 🔥", url=CHANNEL_URL),
            InlineKeyboardButton("বাংলা ভিডিও 🎬", url=GROUP_URL),
        ],
        [
            InlineKeyboardButton("Backup Channel 🛡️", url=BACKUP_URL)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🔥 ভাইরাল সব ভিডিও পেতে আমাদের অফিসিয়াল চ্যানেলগুলোতে এখনই জয়েন করুন! ✅\n\n"
        "👇 নিচের বাটনে ক্লিক করুন 👇",
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
