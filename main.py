import logging
import os
import json

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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message:
        await update.message.reply_text("Hello! I'm alive.")


application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

_initialized = False


def main() -> None:
    if not WEBHOOK_URL:
        raise RuntimeError("WEBHOOK_URL environment variable not set")
    # Set up the webhook and run the web server for local development
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}",
    )


async def handler(event, context):
    """Yandex Cloud Functions entry point."""
    global _initialized
    if not _initialized:
        await application.initialize()
        _initialized = True

    if event.get("httpMethod") == "POST" and event.get("body"):
        if event.get("path", "/").lstrip("/") != TOKEN:
            return {"statusCode": 403, "body": "forbidden"}
        update = Update.de_json(json.loads(event["body"]), application.bot)
        await application.process_update(update)
    return {
        "statusCode": 200,
        "body": "ok",
    }


if __name__ == "__main__":
    main()
