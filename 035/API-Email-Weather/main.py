#! /usr/bin/env python3

import requests
import datetime
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
GMAIL_ACCOUNT = os.getenv("GMAIL_ACCOUNT")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

#######################################
# Pulling weather information via API #
#######################################

MY_LAT = 40.438130
MY_LON = -80.088210
CITY_NAME = 'Pittsburgh,US'
owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"  # Responds with a 5 day forcast in 3 hours increments
weather_params = {
    'lat': MY_LAT,
    'lon': MY_LON,
    'appid': API_KEY,
    'units': 'imperial',
    # 'cnt': 4,  # Limits the count of 3 hour forecasts, so 12 hours worth
}
response = requests.get(url=owm_endpoint, params=weather_params)
# response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?lat={MY_LAT}&lon={MY_LON}&appid={API_KEY}")

response.raise_for_status()
weather_data = response.json()
print(weather_data)


def get_cardinal_direction(degree):
    directions = ["North", "Northeast", "East", "Southeast", "South", "Southwest", "West", "Northwest", "North"]
    idx = int((degree + 22.5) // 45)
    return directions[idx]


city = weather_data['city']['name']
country = weather_data['city']['country']
message = f"Here is the 12 hour forecast for {city},{country}.\n\n"

for forecast in weather_data['list']:
    epoch_time = forecast['dt']
    dt_object = datetime.datetime.utcfromtimestamp(epoch_time)
    # formatted_time = dt_object.strftime('%A, %Y-%m-%d %H%M')
    formatted_time = dt_object.strftime('%A, %d %b at %I:%M %p')
    message += f"{formatted_time}\n"

    temp_low = forecast['main']['temp_min']
    temp_high = forecast['main']['temp_max']
    feels_like = forecast['main']['feels_like']
    message += f"Temperature: feels like {feels_like}°F [ {temp_low} - {temp_high} ]\n"

    for weather in forecast['weather']:
        message += f"{str(weather['description']).capitalize()} with "
    try:
        message += f"{forecast['rain']['3h']}\" of precipitation\n"
    except KeyError as err:
        message += f"0\" of precipitation\n"

    cloud_coverage = forecast['clouds']['all']
    humidity = forecast['main']['humidity']
    message += f"{cloud_coverage}% cloud coverage and {humidity}% humidity\n"

    wind_speed = forecast['wind']['speed']
    wind_gust = forecast['wind']['gust']
    cardinal_direction = (get_cardinal_direction(forecast['wind']['deg']).lower())
    message += f"Wind speeds {wind_speed} mph with gusts of {wind_gust} from the {cardinal_direction}\n"

    message += f"\n"

print(message)


########################
# Graphing the weather #
########################
class CustomDateFormatter(mdates.DateFormatter):
    def __init__(self, fmt_date, fmt_time):
        self.fmt_date = fmt_date
        self.fmt_time = fmt_time
        self.last_date = None

    def __call__(self, x, pos=0):
        dt = mdates.num2date(x)
        if self.last_date == dt.date():
            fmt = self.fmt_time
        else:
            fmt = self.fmt_date
            self.last_date = dt.date()
        return dt.strftime(fmt)

# Formatters
date_formatter = CustomDateFormatter('%Y-%m-%d', '%H:%M')
hour_locator = mdates.HourLocator(interval=3)

data = weather_data
forecasts = data['list']

# Create DataFrame
forecasts = data['list']
df = pd.DataFrame([{
    'timestamp': pd.to_datetime(forecast['dt_txt']),
    'temp_feels_like': forecast['main']['feels_like'],
    'temp_low': forecast['main']['temp_min'],
    'temp_high': forecast['main']['temp_max'],
    'humidity': forecast['main']['humidity'],
    'precipitation': forecast.get('rain', {}).get('3h', 0) + forecast.get('snow', {}).get('3h', 0),
    'cloud_coverage': forecast['clouds']['all'],
    'wind_speed': forecast['wind']['speed'],
    'wind_gust': forecast['wind'].get('gust', 0)
} for forecast in forecasts])

# Define formatter and locator for x-axis
date_formatter = CustomDateFormatter('%Y-%m-%d', '%H:%M')
hour_locator = mdates.HourLocator(interval=3)


# Temperature Graph
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['timestamp'], df['temp_feels_like'], label='Feels Like Temp (°F)', color='tab:orange')
ax.plot(df['timestamp'], df['temp_low'], label='Low Temp (°F)', color='tab:blue', linestyle='--')
ax.plot(df['timestamp'], df['temp_high'], label='High Temp (°F)', color='tab:red', linestyle='--')
ax.set_xlabel('Time')
ax.set_ylabel('Temperature (°F)')
ax.set_title('Temperature Forecast')
ax.xaxis.set_major_locator(hour_locator)
ax.xaxis.set_major_formatter(date_formatter)
ax.legend()
plt.xticks(rotation=90)
plt.tight_layout(pad=1.0)
fig.savefig('temperature_graph.png')
# plt.show()


# Wind Graph
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df['timestamp'], df['wind_speed'], label='Wind Speed (mph)', color='tab:purple')
ax.plot(df['timestamp'], df['wind_gust'], label='Wind Gust (mph)', color='tab:pink', linestyle='-.')
ax.set_xlabel('Time')
ax.set_ylabel('Wind Speed and Gust (mph)')
ax.set_title('Wind Forecast')
ax.xaxis.set_major_locator(hour_locator)
ax.xaxis.set_major_formatter(date_formatter)
ax.legend()
plt.xticks(rotation=90)
plt.tight_layout(pad=1.0)
fig.savefig('wind_graph.png')
# plt.show()


# Precipitation and Humidity Graph
fig, ax1 = plt.subplots(figsize=(12, 6))
color = 'tab:blue'
ax1.plot(df['timestamp'], df['precipitation'], label='Precipitation (inches)', color=color)
ax1.set_xlabel('Time')
ax1.set_ylabel('Precipitation (inches)', color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax2 = ax1.twinx()
color = 'tab:green'
ax2.plot(df['timestamp'], df['humidity'], label='Humidity (%)', color=color, linestyle=':')
ax2.set_ylabel('Humidity (%)', color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax1.set_title('Precipitation and Humidity Forecast')
ax1.xaxis.set_major_locator(hour_locator)
ax1.xaxis.set_major_formatter(date_formatter)
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=90)
plt.tight_layout(pad=1.0)
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left')
fig.savefig('precipitation_humidity_graph.png')
# plt.show()

################################
# Generate HTML map of of area #
################################

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather Map Layers</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Leaflet CSS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />

    <!-- Leaflet JavaScript -->
    <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
</head>
<body>
    <div id="map" style="width: 600px; height: 400px;"></div>

    <script>
    // Initialize the map
    var map = L.map('map').setView([40.438130, -80.088210], 6);

    // Add a base map layer
    var osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Your OpenWeatherMap API key
    var apiKey = 'UPDATE_ME';  // Replace with your actual API key

    // Weather layers
    var temperatureLayer = L.tileLayer(`http://tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png?appid=${apiKey}`, {opacity: 1.0});
    var precipitationLayer = L.tileLayer(`http://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{y}.png?appid=${apiKey}`, {opacity: 1.0}).addTo(map);
    var cloudsLayer = L.tileLayer(`http://tile.openweathermap.org/map/clouds_new/{z}/{x}/{y}.png?appid=${apiKey}`, {opacity: 10.}).addTo(map);
    var windLayer = L.tileLayer(`http://tile.openweathermap.org/map/wind_new/{z}/{x}/{y}.png?appid=${apiKey}`, {opacity: 1.0});

    // Layer control
    var baseMaps = { "OpenStreetMap": osmLayer };
    var overlayMaps = {
        "Temperature": temperatureLayer,
        "Precipitation": precipitationLayer,
        "Clouds": cloudsLayer,
        "Wind": windLayer
    };
    L.control.layers(baseMaps, overlayMaps).addTo(map);
    </script>
</body>
</html>
"""

# Write the HTML content to a file
with open("weather_map.html", "w") as file:
    file.write(html_content)

###########################################
# Emailing out notification to recipients #
###########################################


recipients = [GMAIL_ACCOUNT]

# Create a MIMEMultipart object for the email
msg = MIMEMultipart()
msg['Subject'] = "5 Day Weather Forecast"
msg['From'] = GMAIL_ACCOUNT
msg['To'] = ", ".join(recipients)

# Attach the text message
text_part = MIMEText(message, 'plain')
msg.attach(text_part)

# Attach the images
for file_name in ['temperature_graph.png', 'wind_graph.png', 'precipitation_humidity_graph.png']:
    with open(file_name, 'rb') as file:
        img = MIMEImage(file.read(), name=file_name)
        img.add_header('Content-Disposition', 'attachment', filename=file_name)
        msg.attach(img)

##### DOES NOT WANT TO ATTACH FOR SOME REASON ##### 
# # Attach the HTML file content
# with open("weather_map.html", "r") as file:
#     html_content = file.read()
# html_attachment = MIMEText(html_content, "html", "utf-8")
# msg.attach(html_attachment)
##### DOES NOT WANT TO ATTACH FOR SOME REASON ##### 

# Send the email
smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp_server.login(GMAIL_ACCOUNT, GMAIL_APP_PASSWORD)
print(f"Sending email to: {recipients}")
smtp_server.send_message(msg)
smtp_server.quit()

