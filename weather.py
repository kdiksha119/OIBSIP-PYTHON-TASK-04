import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_weather(data):
    if data:
        location = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        conditions = data['weather'][0]['description']

        print(f"Weather for {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {conditions.capitalize()}")
    else:
        print("Error: Unable to fetch weather data.")

def main():
    api_key = 'your_api_key_here'  # Replace with your OpenWeatherMap API key
    location = input("Enter the city name or ZIP code: ")

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
    