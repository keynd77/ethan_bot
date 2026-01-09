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
# How to get GIFs from giphy.com:
# 1. Go to https://giphy.com/ and find a GIF you like
# 2. Click on the GIF to open it
# 3. Right-click the GIF → "Copy image address" or "Copy image link"
# 4. Paste the URL here (should look like: https://media.giphy.com/media/XXXXX/giphy.gif)
# 
# You can also use Giphy page URLs (like https://giphy.com/gifs/XXXXX) - they'll be converted automatically
ETHAN_MODE_GIFS = [
    # Add GIF URLs here, for example:
    # "https://media.giphy.com/media/example1/giphy.gif",
    # "https://giphy.com/gifs/example2",  # Page URL - will be converted automatically
    # "https://media.tenor.com/example3.gif",
    # You can add as many as you want
]

# Giphy search terms for random GIFs (used if GIPHY_API_KEY is set)
GIPHY_SEARCH_TERMS = [
    "matrix", "cyberpunk", "neural network", "quantum", "digital", 
    "hacking", "code", "binary", "tech", "futuristic", "ai", 
    "robot", "system", "protocol", "activation"
]




def convert_giphy_url_to_direct(url: str) -> str:
    """Convert Giphy page URL to direct GIF URL"""
    # If it's already a direct media URL, return as is
    if "media.giphy.com" in url and url.endswith(('.gif', '.mp4')):
        return url
    
    # If it's a Giphy page URL, try to extract the ID and convert
    # Giphy page URLs look like: https://giphy.com/gifs/XXXXX or https://giphy.com/gifs/category-XXXXX
    if "giphy.com/gifs" in url:
        # Extract the GIF ID (last part of the URL)
        parts = url.rstrip('/').split('/')
        gif_id = parts[-1].split('-')[-1]  # Get last part, handle category-XXXXX format
        # Convert to direct URL
        return f"https://media.giphy.com/media/{gif_id}/giphy.gif"
    
    # If it's already a direct URL or unknown format, return as is
    return url


async def get_gif_from_giphy(keyword: str) -> str:
    """Get a random GIF URL from Giphy API with a specific keyword"""
    giphy_key = os.getenv('GIPHY_API_KEY')
    if not giphy_key:
        return None
    
    try:
        async with aiohttp.ClientSession() as session:
            url = f"https://api.giphy.com/v1/gifs/random"
            params = {
                'api_key': giphy_key,
                'tag': keyword,
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


async def get_random_gif_url() -> str:
    """Get a random GIF URL from Giphy API or fallback to list"""
    # First, try to use custom GIF list
    if ETHAN_MODE_GIFS:
        gif_url = random.choice(ETHAN_MODE_GIFS)
        # Convert Giphy page URLs to direct URLs if needed
        return convert_giphy_url_to_direct(gif_url)
    
    # If no custom GIFs, try Giphy API
    search_term = random.choice(GIPHY_SEARCH_TERMS)
    return await get_gif_from_giphy(search_term)


async def click_to_go_crypto_ethan_mode(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /click_to_go_crypto_ethan_mode command"""
    try:
        response = random.choice(ETHAN_MODE_RESPONSES)
        
        # Try to get a GIF
        gif_url = await get_random_gif_url()
        
        # Always send GIF with text as caption (single message) if GIF available
        if gif_url:
            await update.message.reply_animation(gif_url, caption=response)
        else:
            # Fallback to text only if no GIF available
            await update.message.reply_text(response)
            
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        try:
            await update.message.reply_text("ETHAN MODE ACTIVATED")
        except:
            pass


async def ethan_mode_gif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /ethan_mode_gif command - sends a random brain GIF with text"""
    try:
        # Get a random technical response
        response = random.choice(ETHAN_MODE_RESPONSES)
        
        # Fetch a GIF with "brain" keyword
        gif_url = await get_gif_from_giphy("brain")
        
        if gif_url:
            # Send GIF with text as caption (single message)
            await update.message.reply_animation(gif_url, caption=response)
        else:
            # Fallback if Giphy API is not available
            await update.message.reply_text(response)
            
    except Exception as e:
        logger.error(f"Error sending GIF: {e}")
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
    
    # Register command handlers
    application.add_handler(CommandHandler("click_to_go_crypto_ethan_mode", click_to_go_crypto_ethan_mode))
    application.add_handler(CommandHandler("ethan_mode_gif", ethan_mode_gif))
    
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
