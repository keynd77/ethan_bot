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

# Store group settings (chat_id -> settings dict)
# Format: {chat_id: {'gifs_enabled': True/False}}
group_settings = {}

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


def is_gif_enabled(chat_id: int = None) -> bool:
    """Check if GIFs are enabled for a specific chat (group) or globally"""
    # First check group-specific setting
    if chat_id is not None and chat_id in group_settings:
        return group_settings[chat_id].get('gifs_enabled', True)
    
    # Fall back to environment variable
    gif_setting = os.getenv('ENABLE_GIFS', 'true').strip().lower()
    return gif_setting in ('true', '1', 'yes', 'on')


def set_gif_enabled(chat_id: int, enabled: bool) -> None:
    """Set GIF enabled status for a specific chat (group)"""
    if chat_id not in group_settings:
        group_settings[chat_id] = {}
    group_settings[chat_id]['gifs_enabled'] = enabled


def get_gif_keyword() -> str:
    """Get a random GIF keyword from environment variable or default to 'brain'"""
    # Get keywords from environment variable (comma-separated)
    keywords_env = os.getenv('GIPHY_KEYWORDS', '').strip()
    
    if keywords_env:
        # Parse comma-separated list and clean up
        keywords = [k.strip() for k in keywords_env.split(',') if k.strip()]
        if keywords:
            return random.choice(keywords)
    
    # Default fallback
    return "brain"


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
        chat_id = update.message.chat.id
        
        # Check if GIFs are enabled for this chat
        if is_gif_enabled(chat_id):
            # Get a random keyword from environment variable or use default
            keyword = get_gif_keyword()
            gif_url = await get_gif_from_giphy(keyword)
            
            # Send GIF with text as caption (single message) if GIF available
            if gif_url:
                await update.message.reply_animation(gif_url, caption=response)
                return
        
        # Send text only if GIFs disabled or no GIF available
        await update.message.reply_text(response)
            
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        try:
            await update.message.reply_text("ETHAN MODE ACTIVATED")
        except:
            pass


async def ethan_mode_gif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /ethan_mode_gif command - sends a random GIF with text"""
    try:
        # Get a random technical response
        response = random.choice(ETHAN_MODE_RESPONSES)
        chat_id = update.message.chat.id
        
        # Check if GIFs are enabled for this chat
        if not is_gif_enabled(chat_id):
            await update.message.reply_text(f"{response}\n\n(GIFs are currently disabled for this group)")
            return
        
        # Get a random keyword from environment variable or use default
        keyword = get_gif_keyword()
        gif_url = await get_gif_from_giphy(keyword)
        
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


async def gif_on(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Enable GIFs for this group"""
    try:
        chat_id = update.message.chat.id
        set_gif_enabled(chat_id, True)
        
        chat_type = "group" if update.message.chat.type in ['group', 'supergroup'] else "chat"
        await update.message.reply_text(f"GIFs enabled for this {chat_type}.")
    except Exception as e:
        logger.error(f"Error enabling GIFs: {e}")
        await update.message.reply_text("Error enabling GIFs.")


async def gif_off(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Disable GIFs for this group"""
    try:
        chat_id = update.message.chat.id
        set_gif_enabled(chat_id, False)
        
        chat_type = "group" if update.message.chat.type in ['group', 'supergroup'] else "chat"
        await update.message.reply_text(f"GIFs disabled for this {chat_type}.")
    except Exception as e:
        logger.error(f"Error disabling GIFs: {e}")
        await update.message.reply_text("Error disabling GIFs.")


async def settings_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Show current settings for this group"""
    try:
        chat_id = update.message.chat.id
        gifs_enabled = is_gif_enabled(chat_id)
        
        chat_type = "group" if update.message.chat.type in ['group', 'supergroup'] else "chat"
        status = "enabled" if gifs_enabled else "disabled"
        
        settings_text = f"""
*Settings for this {chat_type}:*

GIFs: {status}

Use /ethan_mode_gif_on or /ethan_mode_gif_off to toggle GIFs for this {chat_type}.
"""
        await update.message.reply_text(settings_text, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Error showing settings: {e}")
        await update.message.reply_text("Error retrieving settings.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /help command - shows all available commands"""
    help_text = """
🤖 *ETHAN MODE Bot Commands*

*Main Commands:*
/ethan_mode_activate - Activate ETHAN MODE with technical response (may include GIF if enabled)

/ethan_mode_gif - Get a random GIF with technical response

*Settings Commands:*
/ethan_mode_gif_on - Enable GIFs for this group
/ethan_mode_gif_off - Disable GIFs for this group
/ethan_mode_settings - Show current settings for this group

/ethan_mode_help - Show this help message

*Note:* Settings are per-group. Each group can have its own GIF settings.
"""
    try:
        await update.message.reply_text(help_text, parse_mode='Markdown')
    except Exception as e:
        logger.error(f"Error sending help: {e}")
        # Fallback without markdown
        help_text_plain = """
ETHAN MODE Bot Commands:

Main Commands:
/ethan_mode_activate - Activate ETHAN MODE with technical response (may include GIF if enabled)

/ethan_mode_gif - Get a random GIF with technical response

Settings Commands:
/ethan_mode_gif_on - Enable GIFs for this group
/ethan_mode_gif_off - Disable GIFs for this group
/ethan_mode_settings - Show current settings for this group

/ethan_mode_help - Show this help message

Note: Settings are per-group. Each group can have its own GIF settings.
"""
        await update.message.reply_text(help_text_plain)


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
    
    # Register command handlers (all prefixed with ethan_mode_ to avoid conflicts)
    application.add_handler(CommandHandler("ethan_mode_activate", click_to_go_crypto_ethan_mode))
    application.add_handler(CommandHandler("ethan_mode_gif", ethan_mode_gif))
    application.add_handler(CommandHandler("ethan_mode_help", help_command))
    application.add_handler(CommandHandler("ethan_mode_gif_on", gif_on))
    application.add_handler(CommandHandler("ethan_mode_gif_off", gif_off))
    application.add_handler(CommandHandler("ethan_mode_settings", settings_command))
    
    # Start the bot
    logger.info("Bot is starting...")
    logger.info("Bot is ready! Add it to your group and use /ethan_mode_activate")
    try:
        application.run_polling(allowed_updates=Update.ALL_TYPES)
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot error: {e}")


if __name__ == '__main__':
    main()
