import requests
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):
    """Gets current weather information for a city."""

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print("\n--- Weather Report ---")
    print(f"City: {city.title()}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description.title()}")
    print("----------------------")


def main():
    print("Welcome to the Weather Report App! 🌤️")

    city = input("Enter a city: ")

    try:
        get_weather(city)
    except requests.RequestException:
        print("Sorry, I could not get the weather. Please try again.")


if __name__ == "__main__":
    main()