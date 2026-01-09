# Ethan Bot

A Telegram bot that activates ETHAN MODE when you send the command `/click_to_go_crypto_ethan_mode`.

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

3. **Run the bot:**
   ```bash
   python bot.py
   ```

## Hosting (Required for Group Use)

**Yes, you need to host the bot somewhere for it to work 24/7 in group chats!** Here are free hosting options:

### Option 1: Railway (Recommended - Easiest)

1. Go to [railway.app](https://railway.app) and sign up (free tier available)
2. Click "New Project" → "Deploy from GitHub repo"
3. Connect your GitHub account and select this repository
4. Add environment variable:
   - Variable: `TELEGRAM_BOT_TOKEN`
   - Value: Your bot token from BotFather
5. Railway will automatically deploy and keep your bot running!

### Option 2: Render

1. Go to [render.com](https://render.com) and sign up (free tier available)
2. Click "New" → "Background Worker"
3. Connect your GitHub repository
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python bot.py`
   - **Environment Variable:** Add `TELEGRAM_BOT_TOKEN` with your token
5. Click "Create Background Worker" - your bot will be live!

### Option 3: Fly.io

1. Install Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Sign up at [fly.io](https://fly.io) (free tier available)
3. Run:
   ```bash
   fly launch
   fly secrets set TELEGRAM_BOT_TOKEN=your_token_here
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

Once the bot is running (locally or hosted), send `/click_to_go_crypto_ethan_mode` in any chat with the bot, and it will respond with "ETHAN MODE ACTIVATED".

## Environment Variables

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token from BotFather (required)

## Notes

- The bot must be running continuously to respond to commands
- For group use, cloud hosting is recommended
- All hosting options above have free tiers that work perfectly for this bot
