
# Weather Info Script

This Python script fetches and displays real-time weather information for any city using the OpenWeatherMap API. It is simple to use and provides current weather conditions and temperature in Fahrenheit.

## Features
- Retrieve current weather conditions (e.g., Clear, Rain, Clouds).
- Display the current temperature in Fahrenheit.
- Handle errors for invalid city names gracefully.

## Prerequisites
- Python 3.x installed on your machine.
- The `requests` library installed.

## Setup
1. Install Python if it's not already installed. Download it from [Python.org](https://www.python.org/).
2. Install the `requests` library:
   ```bash
   pip install requests
   ```
3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/appid) and replace the `api_key` variable in the script with your key.

## Usage
1. Run the script:
   ```bash
   python weather_info.py
   ```
2. When prompted, enter the name of the city for which you want to check the weather.
   Example:
   ```text
   Enter city: New York
   ```
3. The script will display:
   - The current weather condition (e.g., Clear, Clouds, Rain).
   - The current temperature in Fahrenheit.

### Example Output
```text
Enter city: Los Angeles
The weather in Los Angeles is: Clear
The temperature in Los Angeles is: 75F
```

### Error Handling
If the city is not found (e.g., due to a typo or an invalid city name), the script will display:
```text
City not found
```

## Notes
- The script fetches weather data in imperial units (Fahrenheit). To use metric units (Celsius), change the `units=imperial` parameter to `units=metric` in the API call.
- Ensure that your API key is valid and you stay within the API's usage limits.

## Contributing
Contributions are welcome! Feel free to fork this repository and create pull requests. For major changes, please open an issue to discuss your ideas first.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
