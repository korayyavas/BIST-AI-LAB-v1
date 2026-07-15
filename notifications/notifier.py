"""
Notification Manager
BIST AI LAB v3
"""

from __future__ import annotations

from notifications.telegram import TelegramNotifier
from notifications.email import EmailNotifier


class Notifier:

    def __init__(
        self,
        telegram: TelegramNotifier | None = None,
        email: EmailNotifier | None = None,
    ):

        self.telegram = telegram

        self.email = email

    # ==================================================

    def send_telegram(
        self,
        message: str,
    ) -> bool:

        if self.telegram is None:

            return False

        return self.telegram.send(
            message
        )

    # ==================================================

    def send_email(
        self,
        receiver: str,
        subject: str,
        message: str,
    ) -> bool:

        if self.email is None:

            return False

        return self.email.send(

            receiver,

            subject,

            message,

        )

    # ==================================================

    def broadcast(
        self,
        message: str,
        receiver: str | None = None,
        subject: str = "BIST AI LAB Alert",
    ) -> dict:

        result = {

            "telegram": False,

            "email": False,

        }

        if self.telegram:

            result["telegram"] = self.send_telegram(
                message
            )

        if self.email and receiver:

            result["email"] = self.send_email(

                receiver,

                subject,

                message,

            )

        return result