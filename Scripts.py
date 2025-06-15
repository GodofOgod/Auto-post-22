# © 2025 FtKrishna. All rights reserved.
# Channel  : https://t.me/NxMirror
# Contact  : @FTKrshna

class FtKrshna:
    HELP_TEXT = (
        "👋 *Welcome to the Bot!*\n"
        "This bot helps you manage Telegram channels with ease. Below is a guide to all commands and features, with examples to get you started.\n\n"

        "📜 *Commands Overview*\n"
        "Use these commands to interact with the bot. All commands are case-insensitive.\n\n"

        "*/post*\n"
        "Create a new post (text, photo, video, or document) in a channel.\n"
        "• Steps: Select a channel, send your content, add buttons (optional), preview, and confirm.\n"
        "• Example:\n"
        "  - Type `/post`\n"
        "  - Choose a channel (e.g., My Channel)\n"
        "  - Send: `Check out our new product!`\n"
        "  - Add buttons: `Learn More - https://example.com`\n"
        "  - Confirm to post.\n\n"

        "*/edit*\n"
        "Edit an existing post in a channel.\n"
        "• Steps: Select a channel, enter the message ID, update content/buttons, preview, and confirm.\n"
        "• Example:\n"
        "  - Type `/edit`\n"
        "  - Choose a channel\n"
        "  - Enter message ID: `123`\n"
        "  - Send new content: `Updated product info!` or `keep` to retain old content\n"
        "  - Send new buttons: `Buy Now - https://shop.com` or `keep`\n"
        "  - Confirm to update.\n"
        "• Tip: Find the message ID in the channel or bot logs.\n\n"

        "*/broadcast*\n"
        "Send the same post to multiple channels at once.\n"
        "• Steps: Send content, add buttons (optional), preview, and confirm.\n"
        "• Example:\n"
        "  - Type `/broadcast`\n"
        "  - Send: `Join our event today!`\n"
        "  - Add buttons: `RSVP - https://event.com`\n"
        "  - Confirm to send to all channels.\n\n"

        "*/add*\n"
        "Add a channel to the bot’s database for posting.\n"
        "• Format: `/add -100xxxxxxxxxx` (channel ID starts with -100)\n"
        "• Example: `/add -100123456789` adds a channel named 'My Channel'.\n"
        "• You can Unlimited Channels\n\n"

        "*/setdefaultbtns*\n"
        "Set default buttons to automatically add to posts.\n"
        "• Steps: Send button format or `none` to clear.\n"
        "• Button Format:\n"
        "  - Single button: `Text - URL`\n"
        "  - Multiple buttons: `Text1 - URL1 && Text2 - URL2`\n"
        "  - New line for new row.\n"
        "  - Special buttons: `Text - popup:Message`, `Text - alert:Message`, `Text - share:Message`\n"
        "• Example:\n"
        "  - Type `/setdefaultbtns`\n"
        "  - Send:\n"
        "    ```\n"
        "    Website - https://example.com\n"
        "    Support - t.me/support && Share - share:Join us!\n"
        "    ```\n"
        "  - These buttons will be added to new posts.\n\n"

        "*/cancel*\n"
        "Stop any ongoing operation (e.g., posting, editing).\n"
        "• Example: Type `/cancel` during a `/post` to return to the main menu.\n\n"

        "*Features via Start Menu*\n"
        "Access these by typing `/start` and clicking buttons.\n\n"

        "• *My Channels*\n"
        "View and manage channels you’ve added with `/add`.\n"
        "• Features: See channel list, delete specific channels (🗑️), or clear all.\n"
        "• Example: Click 'My Channels' to see:\n"
        "  ```\n"
        "  [My Channel] [🗑️1]\n"
        "  [Clear All] [Back] [Close]\n"
        "  ```\n"
        "  Click 🗑️ to remove a channel.\n\n"

        "• *Default Buttons*\n"
        "Manage default buttons (same as `/setdefaultbtns`).\n"
        "• Example: Click 'Default Buttons', then 'Set Default Buttons', and send:\n"
        "  `Contact Us - t.me/contact`\n\n"

        "*Tips for Beginners*\n"
        "• Use `/start` to navigate easily.\n"
        "• Add channels with `/add` before posting.\n"
        "• Check previews before confirming posts.\n"
        "• Use `/cancel` if you’re stuck.\n"
        "• URLs must start with `http://`, `https://`, or `t.me/`.\n\n"

        "Ready to start? Type `/start` or click below!"
    )
    
    START_TEXT = (
        "👋 *Welcome!*\n\n"
        "Use the buttons below to:\n"
        "• Post content to your channels\n"
        "• Edit existing posts\n"
        "• Broadcast to multiple channels\n"
        "• Manage default buttons\n"
        "• View and manage your channels\n\n"
        "Get started by clicking an option below!"
    )
    
    DEFAULT_BUTTONS_TEXT = (
        "Send the default buttons in the format:\n\n"
        "• Single button:\n"
        "`Button text - t.me/LinkExample`\n\n"
        "• Multiple buttons in a single line:\n"
        "`Button text - t.me/Link1 && Button text - t.me/Link2`\n\n"
        "• Multiple rows of buttons:\n"
        "`Button text - t.me/Link1`\n"
        "`Button text - t.me/Link2`\n\n"
        "• Popup button:\n"
        "`Button text - popup: Text of the popup`\n\n"
        "• Alert button:\n"
        "`Button text - alert: Text of the popup`\n\n"
        "• Share button:\n"
        "`Button text - share: Text to share`\n\n"
        "Send `none` to clear default buttons."
    )
    
    NO_CHANNELS_TEXT = (
        "No channels available. Use /add to add a channel or define DEFAULT_CHANNELS in config."
    )
    
    SELECT_CHANNEL_TEXT = "Please select a channel to edit the post."


class Labels:
    POST = "Post"
    EDIT = "Edit"
    BROADCAST = "Broadcast"
    HELP = "Help"
    DEFAULT_BUTTONS = "Default Buttons"
    MY_CHANNELS = "My Channels"
    CLOSE = "Close"
