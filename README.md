# Weather Detector

The **Weather Detector** is a Python-based application that retrieves and displays the current weather information for a specified location. It uses the OpenWeatherMap API for fetching real-time weather data. This project includes both a CLI-based implementation and a GUI-based implementation using the `tkinter` library.

## Features
- Retrieves weather information such as:
  - Location
  - Temperature (in Celsius)
  - Weather condition (description)
  - Humidity
  - Wind speed
- Simple and interactive GUI for ease of use.

---

## CLI-Based Implementation

### Prerequisites
1. Python 3.x installed on your system.
2. `requests` library installed. You can install it via:
   ```bash
   pip install requests
   ```
3. An API key from [OpenWeatherMap](https://openweathermap.org/).

### How to Use
1. Clone or download the repository.
2. Open the `weather_detector.py` file.
3. Replace `your_api_key_here` with your actual API key from OpenWeatherMap.
4. Run the script in your terminal:
   ```bash
   python weather_detector.py
   ```
5. Enter the desired location when prompted, and the script will display the weather details.

---

## GUI-Based Implementation

### Prerequisites
1. Python 3.x installed on your system.
2. `requests` library installed. You can install it via:
   ```bash
   pip install requests
   ```
3. An API key from [OpenWeatherMap](https://openweathermap.org/).

### How to Use
1. Clone or download the repository.
2. Open the `weather_detector_gui.py` file.
3. Replace `your_api_key_here` with your actual API key from OpenWeatherMap.
4. Run the script in your terminal:
   ```bash
   python weather_detector_gui.py
   ```
5. Enter the desired location in the GUI and click on **Get Weather** to view the weather details.

---

## File Structure
- `main.py`: CLI-based implementation of the Weather Detector.
- `main_2.py`: GUI-based implementation of the Weather Detector.

---

## Example Output
### CLI-Based
```
Enter the location (e.g., city name): Surabaya

Weather Information:
Location: Surabaya
Temperature: 26.01°C
Condition: overcast clouds
Humidity: 80%
Wind Speed: 0.72 m/s
```

### GUI-Based
![Screenshot_1](https://github.com/user-attachments/assets/69c55ddf-2725-4ca0-bfee-efd9b4450eb5)

The GUI displays the weather details in a neatly organized layout after entering a location and clicking the **Get Weather** button.

---

## Notes
- Ensure you have a stable internet connection for fetching weather data.
- If you encounter a `401 Unauthorized` error, verify your API key and ensure it is active.
- The application currently supports fetching weather data by city name. Future enhancements may include location detection by coordinates.

---

## Inspire
source: https://www.youtube.com/watch?v=aQZzMJgPMqQ

---

## License
This project is licensed under the MIT License. Feel free to modify and distribute as needed.

