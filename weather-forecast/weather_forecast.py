import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

API_KEY = os.getenv("OPEN_WEATHER_KEY")
city = "jakarta"

API_URL = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

# Make Request to the API
try:
    response = requests.get(API_URL)
    forecast_data = response.json()  # Stores and parse the JSON response
except requests.exceptions.RequestException as error:
    print("Error fetching forecast data:", error)
    exit()

# Get today date
current_date = datetime.now().date()

# Create empty list for forecast output
forecast = []

# Loop through the forecast_data list and append the data for each day to the forecast list
for data in forecast_data["list"]:
    forecast_date = datetime.fromtimestamp(data["dt"]).date()
    if forecast_date > current_date:
        current_date = forecast_date
        formatted_date = current_date.strftime("%a, %d %b %Y")
        temperature = data["main"]["temp"]

        forecast.append({"date": formatted_date, "temperature": temperature})

# Print the forecast data
print(f"Weather Forecast:")
for data in forecast:
    print(f"{data['date']}: {data['temperature']}°C")
