from bot.logger import setup_logger
from config import AUTHORIZED_USERS

logger = setup_logger(__name__)

def is_authorized(user_id: int) -> bool:
    return user_id in AUTHORIZED_USERS
