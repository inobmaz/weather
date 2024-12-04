import requests

def get_weather(city, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']

        weather_info = {
            "City": city,
            "Temperature": temperature,
            "Feels Like": feels_like,
            "Weather": weather_description,
            "Humidity": humidity,
        }

        return weather_info
    else:
        return f"Error: Could not retrieve weather data for {city}."


if __name__ == "__main__":
    # Replace 'your_api_key' with your OpenWeatherMap API key
    api_key = "your_api_key"

    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)

    if isinstance(weather_data, dict):
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['Temperature']}°C")
        print(f"Feels Like: {weather_data['Feels Like']}°C")
        print(f"Weather: {weather_data['Weather']}")
        print(f"Humidity: {weather_data['Humidity']}%")
    else:
        print(weather_data)

