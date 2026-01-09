#!/usr/bin/env python3
"""
Ethan Bot - Telegram bot that activates ETHAN MODE
"""
import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def click_to_go_crypto_ethan_mode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /click_to_go_crypto_ethan_mode command"""
    try:
        await update.message.reply_text("ETHAN MODE ACTIVATED")
    except Exception as e:
        logger.error(f"Error sending message: {e}")


def main() -> None:
    """Start the bot"""
    # Get bot token from environment variable
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable is not set!")
        logger.error("Please set it using: export TELEGRAM_BOT_TOKEN='your_token_here'")
        return
    
    # Create the Application
    application = Application.builder().token(token).build()
    
    # Register command handler
    application.add_handler(CommandHandler("click_to_go_crypto_ethan_mode", click_to_go_crypto_ethan_mode))
    
    # Start the bot
    logger.info("Bot is starting...")
    logger.info("Bot is ready! Add it to your group and use /click_to_go_crypto_ethan_mode")
    try:
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot error: {e}")


if __name__ == '__main__':
    main()
