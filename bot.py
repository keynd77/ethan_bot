#!/usr/bin/env python3
"""
Ethan Bot - Telegram bot that activates ETHAN MODE with sassy AI
"""
import os
import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Technical/tek responses for when AI is not available
FALLBACK_RESPONSES = [
    "Digitalising complete. ETHAN MODE active.",
    "Neural pathways initialized. ETHAN MODE online.",
    "Protocol activation successful. ETHAN MODE engaged.",
    "System override complete. ETHAN MODE operational.",
    "Binary synchronization achieved. ETHAN MODE activated.",
    "Quantum state resolved. ETHAN MODE active.",
    "Matrix protocols engaged. ETHAN MODE initialized.",
]


def get_ai_response(user_message: str = "", is_command: bool = False) -> str:
    """Generate a sassy AI response with technical/tek terminology"""
    if not OPENAI_AVAILABLE:
        return random.choice(FALLBACK_RESPONSES)
    
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return random.choice(FALLBACK_RESPONSES)
    
    try:
        client = OpenAI(api_key=api_key)
        
        system_prompt = """You are ETHAN MODE - a sassy, sarcastic technical system with an attitude. 
You use technical terminology, cyberpunk/tek jargon, and system activation language. You're extremely sarcastic, 
a bit condescending, but also entertaining. You respond with:
- Heavy use of technical/tek terms: "digitalising", "neural pathways", "protocol activation", "system override", "binary synchronization", "quantum state", "matrix protocols", "neural networks", "data streams", "code execution", "system initialization", "protocol engaged", "digital transformation", "neural interface", "quantum entanglement", "algorithmic processing"
- Cyberpunk/system terms: "system online", "protocol active", "neural link established", "digital consciousness", "matrix connection", "quantum processing", "binary code", "data matrix", "neural network", "system architecture"
- Lots of sarcasm and sass
- NO EMOJIS - never use emojis
- Short, punchy responses (1-2 sentences max, often just one)
- Focus on ETHAN MODE activation and technical system language
- Never mention prices, buying, selling, trading, crypto, or financial terms
- Think cyberpunk, technical, system activation vibes

When someone activates ETHAN MODE, respond with something sassy about system activation using technical terminology."""

        if is_command:
            user_prompt = "Someone just activated ETHAN MODE. Give them a sassy, sarcastic response about system activation using technical/tek terminology. No emojis. Focus on digitalising, neural pathways, protocols, etc."
        else:
            user_prompt = f"Respond to this message with sassy technical/tek sarcasm about ETHAN MODE: {user_message}"
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using mini for cost efficiency, can change to gpt-4 if needed
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=150,
            temperature=0.9
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        logger.error(f"AI error: {e}")
        return random.choice(FALLBACK_RESPONSES)


async def click_to_go_crypto_ethan_mode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /click_to_go_crypto_ethan_mode command"""
    try:
        response = get_ai_response(is_command=True)
        await update.message.reply_text(response)
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        await update.message.reply_text("ETHAN MODE ACTIVATED (AI temporarily offline)")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle regular messages with sassy AI responses (only if bot is mentioned or in group)"""
    try:
        # Only respond if bot is mentioned or in a group chat
        if update.message.chat.type in ['group', 'supergroup']:
            # Random chance to respond (10% chance to avoid spam)
            if random.random() < 0.1:
                user_message = update.message.text or ""
                if user_message and len(user_message) > 5:  # Only respond to substantial messages
                    response = get_ai_response(user_message, is_command=False)
                    await update.message.reply_text(response)
        elif update.message.entities:
            # Check if bot is mentioned
            for entity in update.message.entities:
                if entity.type == "mention" or entity.type == "text_mention":
                    user_message = update.message.text or ""
                    response = get_ai_response(user_message, is_command=False)
                    await update.message.reply_text(response)
                    break
    except Exception as e:
        logger.error(f"Error handling message: {e}")


def main() -> None:
    """Start the bot"""
    # Get bot token from environment variable
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN environment variable is not set!")
        logger.error("Please set it using: export TELEGRAM_BOT_TOKEN='your_token_here'")
        return
    
    # Check for OpenAI API key
    if not OPENAI_AVAILABLE:
        logger.warning("OpenAI library not installed. Install with: pip install openai")
        logger.warning("Bot will use fallback responses without AI.")
    elif not os.getenv('OPENAI_API_KEY'):
        logger.warning("OPENAI_API_KEY not set. Bot will use fallback responses.")
        logger.warning("Get your key from: https://platform.openai.com/api-keys")
    else:
        logger.info("AI mode enabled! Bot will generate sassy technical/tek responses.")
    
    # Create the Application
    application = Application.builder().token(token).build()
    
    # Register command handler
    application.add_handler(CommandHandler("click_to_go_crypto_ethan_mode", click_to_go_crypto_ethan_mode))
    
    # Register message handler for sassy responses in groups
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
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
