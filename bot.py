#!/usr/bin/env python3
"""
Ethan Bot - Telegram bot that activates ETHAN MODE with technical/tek terminology
"""
import os
import logging
import random
import aiohttp
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

# GIF URLs - Add your own GIF URLs here (direct links to .gif files)
# You can find GIFs from Giphy, Tenor, or upload your own
ETHAN_MODE_GIFS = [
    # Add GIF URLs here, for example:
    # "https://media.giphy.com/media/example1.gif",
    # "https://media.giphy.com/media/example2.gif",
    # "https://media.tenor.com/example3.gif",
    # You can add as many as you want
]

# Giphy search terms for random GIFs (used if GIPHY_API_KEY is set)
GIPHY_SEARCH_TERMS = [
    "matrix", "cyberpunk", "neural network", "quantum", "digital", 
    "hacking", "code", "binary", "tech", "futuristic", "ai", 
    "robot", "system", "protocol", "activation"
]




async def get_random_gif_url() -> str:
    """Get a random GIF URL from Giphy API or fallback to list"""
    # First, try to use custom GIF list
    if ETHAN_MODE_GIFS:
        return random.choice(ETHAN_MODE_GIFS)
    
    # If no custom GIFs, try Giphy API
    giphy_key = os.getenv('GIPHY_API_KEY')
    if giphy_key:
        try:
            search_term = random.choice(GIPHY_SEARCH_TERMS)
            async with aiohttp.ClientSession() as session:
                url = f"https://api.giphy.com/v1/gifs/random"
                params = {
                    'api_key': giphy_key,
                    'tag': search_term,
                    'rating': 'g'
                }
                async with session.get(url, params=params) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        if 'data' in data and 'images' in data['data']:
                            # Get the original or downsized_medium GIF
                            gif_data = data['data']['images']
                            gif_url = gif_data.get('original', {}).get('url') or \
                                     gif_data.get('downsized_medium', {}).get('url')
                            if gif_url:
                                return gif_url
        except Exception as e:
            logger.error(f"Error fetching Giphy GIF: {e}")
    
    return None


async def click_to_go_crypto_ethan_mode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /click_to_go_crypto_ethan_mode command"""
    try:
        response = random.choice(ETHAN_MODE_RESPONSES)
        
        # Try to get a GIF
        gif_url = await get_random_gif_url()
        
        # Randomly decide: text only, GIF only, or both (if GIF available)
        if gif_url:
            send_option = random.choice(['text_only', 'gif_only', 'both'])
        else:
            send_option = 'text_only'
        
        if send_option == 'text_only':
            await update.message.reply_text(response)
        elif send_option == 'gif_only':
            await update.message.reply_animation(gif_url, caption=response)
        else:  # both
            await update.message.reply_animation(gif_url)
            await update.message.reply_text(response)
            
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        try:
            await update.message.reply_text("ETHAN MODE ACTIVATED")
        except:
            pass


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
