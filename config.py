# © 2025 FtKrishna. All rights reserved.
# Channel  : https://t.me/NxMirror
# Contact  : @FTKrshna

import os

# Telegram Bot Token from @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7726282640:ABCD")

# List of authorized user IDs (Admins)
AUTHORIZED_USERS = list(map(int, os.environ.get("AUTHORIZED_USERS", "12345678,87654321").split(",")))

# MongoDB URL and DB name
DB_URL = os.environ.get("DB_URL", "mongodb+srv://username:password@cluster.mongodb.net")
DB_NAME = os.environ.get("DB_NAME", "NxMirror")

# Optional: List of default Telegram channels)
# You can add unlimited channel directy from bot)
DEFAULT_CHANNELS = list(map(int, os.environ.get("DEFAULT_CHANNELS", "-1001234567890,-1009876543210").split(",")))
