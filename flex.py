from typing import Any, Dict


class TemplateFlex:
    def __init__(self, client: Any) -> None:
        """
        Initializes the TemplateFlex instance with a client.

        Args:
            client: The client object to be used in the template.
        """
        self.client = client

    def create_flex_template(self) -> Dict[str, Any]:
        """
        Creates a flex template for messaging.

        Returns:
            A dictionary representing the flex template structure.
        """
        template_data: Dict[str, Any] = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {"type": "text", "text": "Send-Liff-Message-Template-Python"}
                ],
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "Follow",
                            "uri": "https://github.com/nezumi0627",
                        },
                        "style": "primary",
                        "color": "#123321",
                    }
                ],
            },
        }
        return template_data
