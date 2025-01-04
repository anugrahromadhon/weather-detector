import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(api_key, location):
    """
    Get the current weather for a specific location using a weather API.

    Parameters:
        api_key (str): Your API key for the weather service.
        location (str): Location for which you want the weather data (e.g., city name or coordinates).

    Returns:
        dict: Weather data including temperature, description, and more.
    """
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'

    try:
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()

        weather = {
            "location": data.get("name"),
            "temperature": data["main"].get("temp"),
            "description": data["weather"][0].get("description"),
            "humidity": data["main"].get("humidity"),
            "wind_speed": data["wind"].get("speed")
        }

        return weather
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")
        return None

def fetch_weather():
    location = location_entry.get()
    if not location:
        messagebox.showwarning("Input Error", "Please enter a location.")
        return

    weather_data = get_weather(API_KEY, location)

    if weather_data:
        result_label.config(text=(
            f"Location: {weather_data['location']}\n"
            f"Temperature: {weather_data['temperature']}°C\n"
            f"Condition: {weather_data['description']}\n"
            f"Humidity: {weather_data['humidity']}%\n"
            f"Wind Speed: {weather_data['wind_speed']} m/s"
        ))
    else:
        result_label.config(text="Failed to retrieve weather data.")

# GUI Setup
root = tk.Tk()
root.title("Weather Detector")
root.geometry("400x300")
root.config(bg="#f0f8ff")

API_KEY = "your API here"  # Replace with your actual API key from OpenWeatherMap

# Widgets
header_label = tk.Label(root, text="Weather Detector", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#4682b4")
header_label.pack(pady=10)

location_label = tk.Label(root, text="Enter Location:", font=("Arial", 12), bg="#f0f8ff", fg="#333333")
location_label.pack()

location_entry = tk.Entry(root, font=("Arial", 12))
location_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Get Weather", font=("Arial", 12), bg="#4682b4", fg="white", command=fetch_weather)
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff", fg="#333333", justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()
