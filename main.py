# Send-Liff-Message-Template-Python (SLMTP)
# Use CHRLINE-Patch (https://github.com/WEDeach/CHRLINE-Patch)
# Coder : nezumi0627
# Date : 2024/09/28
from typing import Any, Dict

from CHRLINE import CHRLINE

from flex import TemplateFlex

# Initialize CHRLINE instance
bot = CHRLINE(device="IOSIPAD", useThrift=True)


def send_flex_message(
    bot: CHRLINE, recipient_id: str, alt_text: str, flex_contents: Dict[str, Any]
) -> None:
    """
    Send a LINE Liff Flex message.

    Parameters:
        bot (CHRLINE): Instance of CHRLINE.
        recipient_id (str): ID of the recipient.
        alt_text (str): Alternative text for the Flex message.
        flex_contents (Dict[str, Any]): Content of the Flex message.

    Returns:
        None
    """
    # Construct Flex message data
    message_data = {"type": "flex", "altText": alt_text, "contents": flex_contents}

    bot.sendLiff(recipient_id, message_data)


# Create an instance of TemplateFlex and retrieve Flex data
template_flex = TemplateFlex(client=bot)
flex_data = template_flex.create_flex_template()

# Set the recipient ID and alternative text
recipient_id = "YOUR_CHAT_GID"
alt_text = "This is a Flex message"

# Send the Flex message
send_flex_message(bot, recipient_id, alt_text, flex_data)
