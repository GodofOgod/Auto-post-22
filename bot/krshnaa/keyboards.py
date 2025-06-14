from bot.logger import setup_logger
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Scripts import Labels  

logger = setup_logger(__name__)

def create_start_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(Labels.POST, callback_data="start_post"),
        InlineKeyboardButton(Labels.EDIT, callback_data="start_edit")
    )
    keyboard.add(
        InlineKeyboardButton(Labels.BROADCAST, callback_data="start_broadcast"),
        InlineKeyboardButton(Labels.HELP, callback_data="start_help")
    )
    keyboard.add(
        InlineKeyboardButton(Labels.DEFAULT_BUTTONS, callback_data="start_default_buttons"),
        InlineKeyboardButton(Labels.MY_CHANNELS, callback_data="start_my_channels")
    )
    keyboard.add(
        InlineKeyboardButton(Labels.CLOSE, callback_data="close_message")
    )
    logger.debug("Created start keyboard")
    return keyboard

def create_default_buttons_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("Set Default Buttons", callback_data="set_default_buttons"),
        InlineKeyboardButton("Clear Default Buttons", callback_data="clear_default_buttons")
    )
    keyboard.add(
        InlineKeyboardButton("Back", callback_data="back_to_start"),
        InlineKeyboardButton("Close", callback_data="close_message")
    )
    logger.debug("Created default buttons keyboard")
    return keyboard

def create_my_channels_keyboard(channels):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for index, channel in enumerate(channels, start=1):
        keyboard.add(
            InlineKeyboardButton(
                channel["title"],
                callback_data=f"view_channel:{channel['channel_id']}"
            ),
            InlineKeyboardButton(
                f"🗑️{index}",
                callback_data=f"delete_channel:{channel['channel_id']}"
            )
        )
    keyboard.row(
        InlineKeyboardButton("Clear All", callback_data="clear_all_channels"),
        InlineKeyboardButton("Back", callback_data="back_to_start"),
        InlineKeyboardButton("Close", callback_data="close_message")
    )
    logger.debug(f"Created my channels keyboard with {len(channels)} channels")
    return keyboard

def create_channel_selection_keyboard(channels, show_back=False, show_close=True):
    keyboard = InlineKeyboardMarkup(row_width=1)
    for channel in channels:
        keyboard.add(
            InlineKeyboardButton(
                channel["title"],
                callback_data=f"select_channel:{channel['channel_id']}"
            )
        )
    buttons = [InlineKeyboardButton("Cancel", callback_data="cancel_action")]
    if show_back:
        buttons.append(InlineKeyboardButton("Back", callback_data="back_action"))
    if show_close:
        buttons.append(InlineKeyboardButton("Close", callback_data="close_message"))
    keyboard.row(*buttons)
    logger.debug(f"Created channel selection keyboard with {len(channels)} channels")
    return keyboard

def create_button_keyboard(button_text: str, for_preview: bool = False) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    rows = button_text.strip().split("\n")
    for row in rows:
        buttons = []
        button_pairs = row.split("&&")
        for pair in button_pairs:
            try:
                text, action = pair.split("-", 1)
                text = text.strip()
                action = action.strip()
                if action.startswith(("http://", "https://", "t.me/")):
                    buttons.append(InlineKeyboardButton(text, url=action))
                elif action.startswith("popup:"):
                    buttons.append(InlineKeyboardButton(text, callback_data=action))
                elif action.startswith("alert:"):
                    buttons.append(InlineKeyboardButton(text, callback_data=action))
                elif action.startswith("share:"):
                    buttons.append(InlineKeyboardButton(text, switch_inline_query=action[6:].strip()))
                else:
                    logger.warning(f"Invalid button action: {action}")
            except ValueError:
                logger.error(f"Invalid button format: {pair}")
                continue
        if buttons:
            keyboard.row(*buttons)
    if not for_preview:
        keyboard.row(
            InlineKeyboardButton("Cancel", callback_data="cancel_action"),
            InlineKeyboardButton("Back", callback_data="back_action"),
            InlineKeyboardButton("Close", callback_data="close_message")
        )
    logger.debug(f"Created button keyboard from input: {button_text}, for_preview={for_preview}")
    return keyboard

def create_confirm_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("Confirm", callback_data="confirm_post"),
        InlineKeyboardButton("Cancel", callback_data="cancel_action")
    )
    keyboard.add(InlineKeyboardButton("Close", callback_data="close_message"))
    logger.debug("Created confirm keyboard")
    return keyboard

def create_help_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("Back to Start", callback_data="back_to_start")
    )
    logger.debug("Created help keyboard")
    return keyboard
