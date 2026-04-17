print("Starting bot...")

import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

API_URL = "http://127.0.0.1:8000/generate"
BOT_TOKEN = "7792210648:AAHpQYvzDsnLTAr5opNZ7UiPtXrSW7oIvfQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me a topic 🚀")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    payload = {
        "posts": ["AI is powerful"],
        "topic": user_input,
        "platform": "Twitter"
    }

    response = requests.post(API_URL, json=payload)
    data = response.json()

    reply = "\n".join(data.get("content", []))
    await update.message.reply_text(reply)
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()