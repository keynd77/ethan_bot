# Ethan Bot

A Telegram bot that activates ETHAN MODE with technical/tek terminology and GIF support.

## Setup

1. Get a Telegram bot token from [@BotFather](https://t.me/botfather)
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variable: `export TELEGRAM_BOT_TOKEN='your_token_here'`
4. Run: `python bot.py`

## Commands

- `/click_to_go_crypto_ethan_mode` - Activate ETHAN MODE
- `/ethan_mode_gif` - Get a random GIF with technical response
- `/gif_on` - Enable GIFs for this group
- `/gif_off` - Disable GIFs for this group
- `/settings` - Show current settings
- `/help` - Show help message

## Environment Variables

- `TELEGRAM_BOT_TOKEN` (required) - Your Telegram bot token
- `GIPHY_API_KEY` (optional) - For GIF fetching
- `GIPHY_KEYWORDS` (optional) - Comma-separated keywords (default: "brain")
- `ENABLE_GIFS` (optional) - Enable/disable GIFs globally (default: true)

## Hosting

Deploy to [Render](https://render.com), [Railway](https://railway.app), or any cloud platform that supports Python.
