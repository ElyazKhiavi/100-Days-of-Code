import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    """Sends email notifications for cheap-flight deals via Gmail SMTP."""

    def __init__(self):
        self._account = os.getenv("GOOGLE_GMAIL_ACCOUNT")
        self._app_password = os.getenv("GOOGLE_APP_PASSWORD")
        self._smtp_server = os.getenv("GOOGLE_SMTP_SERVER")

        # Convert port to int only if it exists, otherwise leave as None
        port_value = os.getenv("GOOGLE_SMTP_SERVER_PORT")
        self._smtp_port = int(port_value) if port_value else 587   # never let None reach SMTP()

    def send_notification(self, subject, body):
        """
        Send an email to the configured Gmail account.
        Returns True on success, False otherwise.
        """
        if not all(
            [self._account, self._app_password, self._smtp_port, self._smtp_server]
        ):
            print(
                "One of Gmail Account, App Password, SMTP server or Port not included!"
            )
            return False

        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self._account
        msg["To"] = self._account
        msg.set_content(body)

        try:
            with smtplib.SMTP(self._smtp_server, self._smtp_port, timeout=10) as server:
                server.starttls()
                server.login(self._account, self._app_password)
                server.send_message(msg)
                print("✅ Email sent.")
                return True

        except smtplib.SMTPAuthenticationError as e:
            print(f"❌ Auth failed: {e.smtp_error.decode()}")
        except (smtplib.SMTPException, ConnectionError, OSError) as e:
            print(f"❌ SMTP/network error: {type(e).__name__} - {e}")

        return False

    def __str__(self):
        return "Send Notifications to Gmail via SMTP."
