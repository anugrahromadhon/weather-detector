import requests

def get_weather(api_key, location):
    """
    Get the current weather for a specific location using a weather API.

    Parameters:
        api_key (str): Your API key for the weather service.
        location (str): Location for which you want the weather data (e.g., city name or coordinates).

    Returns:
        dict: Weather data including temperature, description, and more.
    """
    base_url =f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
    
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
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == "__main__":
    API_KEY = "e8eb13aa18fcec11b71f4f1932602d08"  # Replace with your actual API key from OpenWeatherMap
    location = input("Enter the location (e.g., city name): ")

    weather_data = get_weather(API_KEY, location)

    if weather_data:
        print("\nWeather Information:")
        print(f"Location: {weather_data['location']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Condition: {weather_data['description']}")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    else:
        print("Failed to retrieve weather data.")
