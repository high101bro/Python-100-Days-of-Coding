
import datetime as dt
import requests
import smtplib
from email.mime.text import MIMEText

# HTTPS Code Summary
# 1xx = Hold on...
# 2xx = Here you go...
# 3xx = Go away...
# 4xx = Client screwed up...
# 5xx = Server screwed up...

GMAIL_ACCOUNT = "UPDATE_ME@gmail.com"
GMAIL_APP_PASSWORD = "UPDATE_ME"

ISS_LOCATION_API = "http://api.open-notify.org/iss-now.json"

MY_LAT = 40.438130
MY_LON = -80.088210
VIEWABLE_DEGREE = 10

response = requests.get(
    url=ISS_LOCATION_API
)
# print(response)

# Provides error if not 200
response.raise_for_status()

data = response.json()
# print(data)

iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])
iss_timestamp = data['timestamp']
# print(iss_latitude, iss_longitude, iss_timestamp)

def iss_within_range(iss_latitude, iss_longitude):
    return MY_LAT - VIEWABLE_DEGREE <= iss_latitude <= MY_LAT + VIEWABLE_DEGREE and MY_LON - VIEWABLE_DEGREE <= iss_longitude <= MY_LON + VIEWABLE_DEGREE

def parse_utc_time(time_str):
    time = dt.datetime.fromisoformat(time_str)
    return time.replace(tzinfo=None)

def get_twilight_times():
    SUNRISE_AND_SUNSET_API = "https://api.sunrise-sunset.org/json"
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LON,
        'formatted': 0,
    }
    response = requests.get(url=SUNRISE_AND_SUNSET_API, params=parameters)
    response.raise_for_status()
    data = response.json()

    return {
        'sunrise': parse_utc_time(data['results']['sunrise']),
        'sunset': parse_utc_time(data['results']['sunset']),
        'civil_twilight_begin': parse_utc_time(data['results']['civil_twilight_begin']),
        'civil_twilight_end': parse_utc_time(data['results']['civil_twilight_end']),
        'astronomical_twilight_begin': parse_utc_time(data['results']['astronomical_twilight_begin']),
        'astronomical_twilight_end': parse_utc_time(data['results']['astronomical_twilight_end']),
    }

def astronomical_nighttime(twilight_times):
    time_now_utc = dt.datetime.utcnow()
    if time_now_utc >= twilight_times['astronomical_twilight_end'] or time_now_utc <= twilight_times['astronomical_twilight_begin']:
        return True
    else:
        return False

def civil_nighttime(twilight_times):
    time_now_utc = dt.datetime.utcnow()
    if time_now_utc >= twilight_times['civil_twilight_end'] or time_now_utc <= twilight_times['civil_twilight_begin']:
        return True
    else:
        return False

def normal_nighttime(twilight_times):
    time_now_utc = dt.datetime.utcnow()
    if time_now_utc >= twilight_times['sunset'] or time_now_utc <= twilight_times['sunrise']:
        return True
    else:
        return False

# Fetching twilight times once
twilight_times = get_twilight_times()

print(iss_within_range(iss_latitude, iss_longitude))

# Example usage in if statements
if iss_within_range(iss_latitude, iss_longitude):
    if astronomical_nighttime(twilight_times):
        message = f"Look up! ☝️\n\nIt's currently astronomical twilight - so it should be plenty dark enough to see the ISS 🛰️ overhead:\n  Your Latitude:   {MY_LAT}\n  Your Longitude:  {MY_LON}\n  ISS Latitude:   {iss_latitude}\n  ISS Longitude:  {iss_longitude}"
    elif civil_nighttime(twilight_times):
        message = f"Look up! ☝️\n\nIt's currently civil twilight, so it may be dark enough and see the ISS 🛰️ overhead:\n  Your Latitude:   {MY_LAT}\n  Your Longitude:  {MY_LON}\n  ISS Latitude:   {iss_latitude}\n  ISS Longitude:  {iss_longitude}"
    elif normal_nighttime(twilight_times):
        message = f"Look up! ☝️\n\nThe sun is set, but it may not be dark enough yet. Give it a few minutes and you may be able to see the ISS 🛰️ overhead:\n  Your Latitude:   {MY_LAT}\n  Your Longitude:  {MY_LON}\n  ISS Latitude:   {iss_latitude}\n  ISS Longitude:  {iss_longitude}"
    else:
        message = f"It's bright outside, so odds are you won't see the ISS overhead:\n  Your Latitude:   {MY_LAT}\n  Your Longitude:  {MY_LON}\n  ISS Latitude:   {iss_latitude}\n  ISS Longitude:  {iss_longitude}"

    print(message)

    recipients = [GMAIL_ACCOUNT]

    msg = MIMEText(message)
    msg["Subject"] = "ISS Overhead"
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

    print(f"Sending email to: {recipients}")
    smtp_server.sendmail(
        msg["From"],
        recipients,
        msg.as_string()
    )

    smtp_server.quit()

else:
    message = f"The ISS is not within range:\n  Your Latitude:   {MY_LAT}\n  Your Longitude:  {MY_LON}\n  ISS Latitude:   {iss_latitude}\n  ISS Longitude:  {iss_longitude}"
    print(message,)
