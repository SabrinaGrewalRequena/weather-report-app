import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load the API key
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# App title
st.title("🌤️ Weather Report App")
st.write("Enter a city to see the current weather!")

# User input
city = st.text_input("Enter a city:")

if st.button("Get Weather"):
    if city:
        url = "https://api.openweathermap.org/data/2.5/weather"

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            st.subheader(f"Weather in {city.title()} 📍")
            st.write(f"🌡️ **Temperature:** {temperature}°C")
            st.write(f"💧 **Humidity:** {humidity}%")
            st.write(f"☁️ **Description:** {description.title()}")

        except requests.RequestException:
            st.error("Sorry, I could not get the weather. Please try another city.")
    else:
        st.warning("Please enter a city.")