import asyncio
from . import bot, dp, register_handlers
from .logger import setup_logger

logger = setup_logger("FTKrshna")

async def main():
    logger.info("Initializing NxMirror Bot...")
    

    me = await bot.get_me()
    logger.info(f"Bot username: @{me.username} | ID: {me.id} | Name: {me.first_name}")

    try:
        logger.info("Registering handlers...")
        register_handlers(dp)

        logger.info("Bot Started Successfully...")
        await dp.start_polling()
    except Exception as e:
        logger.exception(f"Bot failed to start: {e}")
        raise
    finally:
        logger.info("Shutting down...")
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.close()
        logger.info("Bot stopped")

if __name__ == "__main__":
    asyncio.run(main())
  
