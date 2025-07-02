import logging
import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
PORT = int(os.environ.get("PORT", 8443))

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN environment variable not set")
if not WEBHOOK_URL:
    raise RuntimeError("WEBHOOK_URL environment variable not set")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text("Hello! I'm alive.")


def main() -> None:
    if (not TOKEN):    
        raise Exception("NO TOKEN PROVIDED")
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    # Set up the webhook and run the web server
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}",
    )


if __name__ == "__main__":
    main()
