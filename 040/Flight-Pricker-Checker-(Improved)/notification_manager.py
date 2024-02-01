from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

load_dotenv()

GMAIL_ACCOUNT = os.getenv("GMAIL_ACCOUNT")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = "8888615710"
TWILIO_VERIFIED_NUMBER = "7206351314"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_emails(self, emails, subject, message):
        # recipients = [GMAIL_ACCOUNT]
        recipients = emails
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["To"] = ", ".join(recipients)
        msg["From"] = GMAIL_ACCOUNT

        smtp_server = smtplib.SMTP_SSL(
            host='smtp.gmail.com',
            # smtp.gmail.com
            # smtp.live.com
            # smtp.mail.yahoo.com
            port=465
        )

        smtp_server.login(
            user=GMAIL_ACCOUNT,
            password=GMAIL_APP_PASSWORD
        )

        print(f"""
Sending email to: {", ".join(recipients)}
Subject: {subject}
Message: {message}
""")

        smtp_server.sendmail(
            msg["From"],
            recipients,
            msg.as_string()
        )

        smtp_server.quit()


    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)