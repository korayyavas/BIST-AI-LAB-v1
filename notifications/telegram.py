"""
Telegram Notifier
BIST AI LAB v3
"""

from __future__ import annotations

import requests


class TelegramNotifier:

    def __init__(
        self,
        token: str,
        chat_id: str,
    ):

        self.token = token

        self.chat_id = chat_id

    # ==================================================

    def send(
        self,
        message: str,
    ) -> bool:

        url = (
            f"https://api.telegram.org/bot"
            f"{self.token}/sendMessage"
        )

        payload = {

            "chat_id": self.chat_id,

            "text": message,

            "parse_mode": "Markdown",

        }

        try:

            response = requests.post(

                url,

                json=payload,

                timeout=10,

            )

            return response.status_code == 200

        except Exception:

            return False