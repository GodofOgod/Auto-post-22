# © 2025 FtKrishna. All rights reserved.
# Channel  : https://t.me/NxMirror
# Contact  : @FTKrshna

import os

# Telegram Bot Token from @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8208550925:AAHas2c6vHZBFdW97gWFsq1OwlCv2_sbMLw")

# List of authorized user IDs (Admins)
AUTHORIZED_USERS = list(map(int, os.environ.get("AUTHORIZED_USERS", "1489652480,1397269319").split(",")))

# MongoDB URL and DB name
DB_URL = os.environ.get("DB_URL", "mongodb+srv://wemedia360:DfQbsNu54pMHTkUy@deamxbotz1.lfquley.mongodb.net/?retryWrites=true&w=majority&appName=deamxbotz1")
DB_NAME = os.environ.get("DB_NAME", "nitin")

# Optional: List of default Telegram channels)
# You can add unlimited channel directy from bot)
DEFAULT_CHANNELS = list(map(int, os.environ.get("DEFAULT_CHANNELS", "-1002592795866").split(",")))
