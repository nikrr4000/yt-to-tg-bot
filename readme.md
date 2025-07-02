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

## Local testing with webhooks

If you want to run the bot locally before deploying it, you need a public
URL that Telegram can reach. The easiest approach is to use a tunneling
service like **ngrok**.

1. [Download and install ngrok](https://ngrok.com/).
2. Start a tunnel to the port your bot listens on (by default `8443`):

   ```bash
   ngrok http 8443
   ```

   Copy the HTTPS URL shown in the ngrok output (for example
   `https://abc123.ngrok.io`).
3. Set `WEBHOOK_URL` to the HTTPS address from step 2.
4. Run the bot as described above. Telegram will deliver updates to your
   local instance through the tunnel.
