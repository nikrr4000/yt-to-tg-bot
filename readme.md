# Telegram Webhook Bot

This project contains a minimal Telegram bot using the `python-telegram-bot` library.
The bot runs using a webhook so it can receive updates from Telegram via an HTTP
endpoint.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set the following environment variables:
   - `TELEGRAM_BOT_TOKEN` – your bot token from BotFather.
   - `WEBHOOK_URL` – the public URL where Telegram can reach your bot
     (for example, `https://example.com/webhook`).
   - `PORT` *(optional)* – port for the local web server (defaults to `8443`).
3. Run the bot:
   ```bash
   python main.py
   ```

The bot registers the webhook automatically and starts an HTTP server to
receive updates.
