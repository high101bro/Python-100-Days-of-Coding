
import smtplib
from email.mime.text import MIMEText
import random


GMAIL_ACCOUNT = "UPDATE_ME@gmail.com"
GMAIL_APP_PASSWORD = "UPDATE_ME"

with open('quotes.txt', 'r') as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)

print(quote)

recipients = ["daniel.komnick@gmail.com"]
email_text = f"""
Hi! This is an automated message from your python script...

{quote}
"""

msg = MIMEText(email_text)
msg["Subject"] = "Quote of the Day"
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
smtp_server.sendmail(
    msg["From"],
    recipients,
    msg.as_string()
)
smtp_server.quit()