#!/usr/bin/env python3
"""
Ethan Bot - Telegram bot that activates ETHAN MODE with technical/tek terminology
"""
import os
import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Technical/tek responses
ETHAN_MODE_RESPONSES = [
    "Digitalising complete. ETHAN MODE active.",
    "Neural pathways initialized. ETHAN MODE online.",
    "Protocol activation successful. ETHAN MODE engaged.",
    "System override complete. ETHAN MODE operational.",
    "Binary synchronization achieved. ETHAN MODE activated.",
    "Quantum state resolved. ETHAN MODE active.",
    "Matrix protocols engaged. ETHAN MODE initialized.",
    "Neural network connection established. ETHAN MODE online.",
    "Data stream processing complete. ETHAN MODE active.",
    "Code execution successful. ETHAN MODE engaged.",
    "System initialization complete. ETHAN MODE operational.",
    "Protocol engaged. ETHAN MODE activated.",
    "Digital transformation finalized. ETHAN MODE online.",
    "Neural interface connected. ETHAN MODE active.",
    "Quantum entanglement synchronized. ETHAN MODE engaged.",
    "Algorithmic processing complete. ETHAN MODE operational.",
    "System architecture loaded. ETHAN MODE activated.",
    "Neural link established. ETHAN MODE online.",
    "Digital consciousness awakened. ETHAN MODE active.",
    "Matrix connection verified. ETHAN MODE engaged.",
    "Quantum processing initialized. ETHAN MODE operational.",
    "Binary code compiled. ETHAN MODE activated.",
    "Data matrix resolved. ETHAN MODE online.",
    "Neural network synchronized. ETHAN MODE active.",
    "System protocol engaged. ETHAN MODE operational.",
    "Digital interface connected. ETHAN MODE activated.",
    "Neural pathways optimized. ETHAN MODE online.",
    "Quantum state matrix loaded. ETHAN MODE active.",
    "Binary data stream established. ETHAN MODE engaged.",
    "System core initialized. ETHAN MODE operational.",
    "Neural processing unit active. ETHAN MODE activated.",
]




async def click_to_go_crypto_ethan_mode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /click_to_go_crypto_ethan_mode command"""
    try:
        response = random.choice(ETHAN_MODE_RESPONSES)
        await update.message.reply_text(response)
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        await update.message.reply_text("ETHAN MODE ACTIVATED")


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
