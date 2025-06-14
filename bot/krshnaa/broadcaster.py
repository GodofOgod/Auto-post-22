# © 2025 FtKrishna. All rights reserved.
# Channel  : https://t.me/NxMirror
# Contact  : @FTKrshna

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import TelegramAPIError
from bot.logger import setup_logger
from ..helpers import is_authorized, send_preview, send_to_channel
from ..modules import mongo_db
from config import DEFAULT_CHANNELS
from .keyboards import create_channel_selection_keyboard, create_button_keyboard, create_confirm_keyboard
from Scripts import FtKrshna

logger = setup_logger(__name__)

class BroadcastState(StatesGroup):
    WaitingForMessage = State()
    WaitingForButtons = State()
    WaitingForPreview = State()

async def broadcast_command(message: types.Message, state: FSMContext, from_button=False, user_id=None):
    logger.info(f"Received /broadcast from user {user_id or message.from_user.id} (from_button={from_button})")
    effective_user_id = user_id or message.from_user.id
    if not is_authorized(effective_user_id):
        await message.reply("You are not authorized to use this command.")
        logger.warning(f"Unauthorized user {effective_user_id} attempted /broadcast")
        return
    try:
        await message.reply(
            "Please send the message you want to broadcast (text, media, or media with captions).",
            reply_markup=create_channel_selection_keyboard([], show_back=False, show_close=True)
        )
        await BroadcastState.WaitingForMessage.set()
        await state.update_data(user_id=effective_user_id, flow="broadcast")
        logger.info(f"Prompted user {effective_user_id} for broadcast message")
    except Exception as e:
        await message.reply("Error starting broadcast.")
        logger.error(f"Error in /broadcast: {str(e)}")
        await state.finish()

async def get_all_channels(bot):
    db_channels = await mongo_db.get_channels()
    channels = db_channels if db_channels else []
    default_channels = []
    try:
        if DEFAULT_CHANNELS:
            for channel_id in DEFAULT_CHANNELS:
                try:
                    chat = await bot.get_chat(channel_id)
                    if chat.type == "channel":
                        default_channels.append({"channel_id": channel_id, "title": chat.title})
                    else:
                        logger.warning(f"Default channel ID {channel_id} is not a channel")
                except TelegramAPIError as e:
                    logger.error(f"Error fetching default channel {channel_id}: {str(e)}")
            channel_ids = {ch["channel_id"] for ch in channels}
            for def_ch in default_channels:
                if def_ch["channel_id"] not in channel_ids:
                    channels.append(def_ch)
            logger.info(f"Combined channels for broadcast: {len(channels)} (DB: {len(db_channels)}, Default: {len(default_channels)})")
    except NameError:
        logger.info("DEFAULT_CHANNELS not defined, using only database channels")
    return channels


async def receive_broadcast_message(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    if message.from_user.id != user_data.get("user_id"):
        logger.warning(f"User mismatch: {message.from_user.id} vs {user_data.get('user_id')}")
        return

    logger.info(f"Received broadcast message from user {message.from_user.id}: {message.text if message.text else message.content_type}")
    content = {}

    if message.text:
        content["type"] = "text"
        content["text"] = message.text
    elif message.photo:
        content["type"] = "photo"
        content["file_id"] = message.photo[-1].file_id
        content["caption"] = message.caption or ""
    elif message.video:
        content["type"] = "video"
        content["file_id"] = message.video.file_id
        content["caption"] = message.caption or ""
    elif message.document:
        content["type"] = "document"
        content["file_id"] = message.document.file_id
        content["caption"] = message.caption or ""
    else:
        await message.reply("Unsupported content type. Please send text, photo, video, or document.")
        logger.error(f"Unsupported content type from user {message.from_user.id}")
        await state.finish()
        return

    try:
        await state.update_data(content=content)
        await message.reply(
            FtKrshna.DEFAULT_BUTTONS_TEXT,
            parse_mode=types.ParseMode.MARKDOWN,
            reply_markup=create_channel_selection_keyboard([], show_back=True, show_close=True)
        )
        await BroadcastState.WaitingForButtons.set()
        logger.info(f"Prompted user {message.from_user.id} for broadcast buttons")
    except Exception as e:
        await message.reply("Error processing message.")
        logger.error(f"Error in receive_broadcast_message: {str(e)}")
        await state.finish()

async def receive_broadcast_buttons(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    if message.from_user.id != user_data.get("user_id"):
        logger.warning(f"User mismatch: {message.from_user.id} vs {user_data.get('user_id')}")
        return
    current_state = await state.get_state()
    logger.info(f"Received broadcast buttons from user {message.from_user.id} in state {current_state}: {message.text}")
    if current_state != BroadcastState.WaitingForButtons.state:
        logger.warning(f"Unexpected state {current_state} for user {message.from_user.id}")
        await message.reply("Bot is in an unexpected state. Please start over with /broadcast or use /cancel.")
        await state.finish()
        return
    content = user_data.get("content")
    if not content:
        await message.reply("Error: No message content found. Please start over with /broadcast.")
        logger.error(f"No content found for user {message.from_user.id}")
        await state.finish()
        return
    try:
        reply_markup = None
        if message.text.lower() == "none":
            logger.info(f"User {message.from_user.id} chose no buttons")
        else:
            reply_markup = create_button_keyboard(message.text, for_preview=True)
            logger.debug(f"Generated preview reply_markup for user {message.from_user.id}: {reply_markup}")
        preview_message = await send_preview(message.bot, content, reply_markup, message.chat.id)
        await state.update_data(preview_message_id=preview_message.message_id, reply_markup=reply_markup)
        await message.reply(
            "Preview sent. Please confirm to broadcast to all channels or cancel:",
            reply_markup=create_confirm_keyboard()
        )
        await BroadcastState.WaitingForPreview.set()
        logger.info(f"Sent broadcast preview to user {message.from_user.id}")
    except TelegramAPIError as e:
        await message.reply(f"Error sending preview: {str(e)}")
        logger.error(f"TelegramAPIError in receive_broadcast_buttons: {str(e)}")
        await state.finish()
    except ValueError as e:
        await message.reply("Invalid button format. Please use the specified format or send 'none'.")
        logger.error(f"ValueError in receive_broadcast_buttons: {str(e)}")
        await state.finish()
    except Exception as e:
        await message.reply("Error processing buttons. Please try again or use /cancel.")
        logger.error(f"Unexpected error in receive_broadcast_buttons: {str(e)}")
        await state.finish()

async def handle_broadcast_confirmation(callback_query: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    if callback_query.from_user.id != user_data.get("user_id"):
        await callback_query.answer()
        logger.warning(f"User mismatch in broadcast confirmation: {callback_query.from_user.id} vs {user_data.get('user_id')}")
        return
    logger.info(f"Received broadcast confirmation from user {callback_query.from_user.id}: {callback_query.data}")
    content = user_data.get("content")
    reply_markup = user_data.get("reply_markup")
    preview_message_id = user_data.get("preview_message_id")
    try:
        if callback_query.data == "confirm_post":
            channels = await get_all_channels(callback_query.bot)
            if not channels:
                await callback_query.message.reply("No channels available for broadcasting.")
                logger.info("No channels found for broadcast")
                await state.finish()
                return
            success_count = 0
            failed_channels = []
            for channel in channels:
                channel_id = channel["channel_id"]
                try:
                    await send_to_channel(callback_query.bot, content, reply_markup, channel_id)
                    success_count += 1
                    logger.info(f"Broadcasted message to channel {channel_id}")
                except TelegramAPIError as e:
                    failed_channels.append((channel_id, str(e)))
                    logger.error(f"Failed to broadcast to channel {channel_id}: {str(e)}")
            response = f"Broadcast completed: {success_count}/{len(channels)} channels successful."
            if failed_channels:
                response += "\nFailed channels:\n" + "\n".join(f"{ch[0]}: {ch[1]}" for ch in failed_channels)
            await callback_query.message.reply(response)
        else:
            await callback_query.message.reply("Broadcast canceled.")
            logger.info(f"Broadcast canceled by user {callback_query.from_user.id}")
        try:
            await callback_query.bot.delete_message(chat_id=callback_query.message.chat.id, message_id=preview_message_id)
        except Exception as e:
            logger.warning(f"Failed to delete preview message: {str(e)}")
        await callback_query.message.delete()
        await state.finish()
        await callback_query.answer()
    except Exception as e:
        await callback_query.message.reply("Error processing broadcast confirmation.")
        logger.error(f"Unexpected error in handle_broadcast_confirmation: {str(e)}")
        await state.finish()
