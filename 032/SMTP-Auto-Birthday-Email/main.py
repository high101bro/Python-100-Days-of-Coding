import smtplib
from email.mime.text import MIMEText
import pandas as pd
import datetime as dt

GMAIL_ACCOUNT = "UPDATE_ME@gmail.com"
GMAIL_APP_PASSWORD = "UPDATE_ME"

# Read CSV into DataFrame
df = pd.read_csv('birthdays.csv', delimiter=',')

# Convert 'date' column to datetime
df['DateColumn'] = pd.to_datetime(df['date'])

# Define the calculate_age function
def calculate_age(birthdate):
    today = dt.datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Add an 'Age' column to the DataFrame
df['Age'] = df['DateColumn'].apply(lambda x: calculate_age(x))

# Extract month and day for comparison
df['Month'] = df['DateColumn'].dt.month
df['Day'] = df['DateColumn'].dt.day

# Get today's month and day
today_month = dt.datetime.today().month
today_day = dt.datetime.today().day

# Filter rows where month and day match today's month and day
todays_birthdays = df[(df['Month'] == today_month) & (df['Day'] == today_day)]

# Send emails if there are any matches
for index, row in todays_birthdays.iterrows():
    # Prepare email
    message = f"Happy Birthday {row['name']}!\n\nSo what are you now, like {row['Age']}? You probably have a busy day, so call me when you can.\n\nDan"
    email = MIMEText(message)
    email['Subject'] = "Happy Birthday!"
    email['From'] = GMAIL_ACCOUNT
    email['To'] = row['email']

    # Send email
    print(f"Sending email to: {row['email']}")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(GMAIL_ACCOUNT, GMAIL_APP_PASSWORD)
        smtp_server.send_message(email)
