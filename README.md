# Ethan Bot

A sassy, sarcastic Telegram bot with AI that activates ETHAN MODE when you send the command `/click_to_go_crypto_ethan_mode`. Features crypto/psyop terminology, sarcasm, and AI-powered responses!

## Quick Setup

1. **Get a Telegram Bot Token:**
   - Open Telegram and search for [@BotFather](https://t.me/botfather)
   - Send `/newbot` and follow the instructions
   - Copy the token you receive
   - **Important:** Enable group access by sending `/setjoingroups` to BotFather, then select your bot and enable "Allow Groups"

2. **Enable Group Access:**
   - In BotFather, send `/mybots`
   - Select your bot
   - Go to "Bot Settings" → "Allow Groups?" → Enable it

## Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your bot token:**
   ```bash
   export TELEGRAM_BOT_TOKEN='your_token_here'
   ```

3. **Get OpenAI API Key (for AI features):**
   - Go to [OpenAI Platform](https://platform.openai.com/api-keys)
   - Sign up or log in
   - Create a new API key
   - Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY='your_openai_key_here'
   ```
   - **Note:** The bot works without AI (uses fallback responses), but AI makes it much sassier!

4. **Run the bot:**
   ```bash
   python bot.py
   ```

## Hosting (Required for Group Use)

**Yes, you need to host the bot somewhere for it to work 24/7 in group chats!** Here are free hosting options:

### Option 1: Railway (Recommended - Easiest)

1. Go to [railway.app](https://railway.app) and sign up (free tier available)
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your GitHub account and select this repository
4. Add environment variables:
   - Variable: `TELEGRAM_BOT_TOKEN` → Your bot token from BotFather
   - Variable: `OPENAI_API_KEY` → Your OpenAI API key (optional but recommended)
5. Railway will automatically deploy and keep your bot running!

### Option 2: Render

1. Go to [render.com](https://render.com) and sign up (free tier available)
2. Click "New" → "Background Worker"
3. Connect your GitHub repository
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
   - **Environment Variables:** 
     - `TELEGRAM_BOT_TOKEN` → Your bot token
     - `OPENAI_API_KEY` → Your OpenAI API key (optional but recommended)
5. Click "Create Background Worker" - your bot will be live!

### Option 3: Fly.io

1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Sign up at [fly.io](https://fly.io) (free tier available)
3. Run:
   ```bash
   fly launch
   fly secrets set TELEGRAM_BOT_TOKEN=your_token_here
   fly secrets set OPENAI_API_KEY=your_openai_key_here
   ```
4. Your bot will be deployed and running!

## Adding Bot to a Group

Once your bot is hosted and running:

1. Open your Telegram group
2. Tap the group name at the top
3. Go to "Add Members"
4. Search for your bot by its username (the one you set with BotFather)
5. Add the bot to the group
6. Anyone in the group can now use `/click_to_go_crypto_ethan_mode`!

## Usage

Once the bot is running (locally or hosted):
- Send `/click_to_go_crypto_ethan_mode` to activate ETHAN MODE with a sassy AI response
- In group chats, the bot will occasionally respond to messages with sarcastic crypto commentary (10% chance to avoid spam)
- The bot uses crypto slang, psyop terminology, and lots of sarcasm

## Features

- **AI-Powered Responses:** Uses OpenAI GPT to generate sassy, sarcastic responses
- **Crypto/Psyop Terminology:** Heavy use of terms like "rekt", "moon", "diamond hands", "narrative shift", "whales", etc.
- **Sarcastic Personality:** The bot has an attitude and isn't afraid to show it
- **Group Chat Integration:** Responds to messages in groups (with rate limiting)
- **Fallback Mode:** Works without AI using pre-written sassy responses

## Environment Variables

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token from BotFather (required)
- `OPENAI_API_KEY`: Your OpenAI API key (optional - bot works without it but AI makes it better!)

## Notes

- The bot must be running continuously to respond to commands
- For group use, cloud hosting is recommended
- All hosting options above have free tiers that work perfectly for this bot
