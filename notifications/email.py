"""
Email Notifier
BIST AI LAB v3
"""

from __future__ import annotations

import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailNotifier:

    def __init__(
        self,
        smtp_server: str,
        smtp_port: int,
        username: str,
        password: str,
    ):

        self.smtp_server = smtp_server

        self.smtp_port = smtp_port

        self.username = username

        self.password = password

    # ==================================================

    def send(
        self,
        receiver: str,
        subject: str,
        message: str,
    ) -> bool:

        mail = MIMEMultipart()

        mail["From"] = self.username

        mail["To"] = receiver

        mail["Subject"] = subject

        mail.attach(
            MIMEText(
                message,
                "plain",
            )
        )

        try:

            with smtplib.SMTP(
                self.smtp_server,
                self.smtp_port,
            ) as server:

                server.starttls()

                server.login(
                    self.username,
                    self.password,
                )

                server.sendmail(

                    self.username,

                    receiver,

                    mail.as_string(),

                )

            return True

        except Exception:

            return False