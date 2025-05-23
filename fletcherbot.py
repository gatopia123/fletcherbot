import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
IMAGE_PATH = "image.jpg"  # Local image path

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_number = int(context.args[0])
        if not 1 <= user_number <= 6:
            await update.message.reply_text("Choose a number between 1 and 6.")
            return
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /play <number 1-6>")
        return

    bot_number = random.randint(1, 6)
    if user_number == bot_number:
        await update.message.reply_photo(photo=open(IMAGE_PATH, 'rb'))
    else:
        await update.message.reply_text("Click. You survived...")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("play", play))
    app.run_polling()
