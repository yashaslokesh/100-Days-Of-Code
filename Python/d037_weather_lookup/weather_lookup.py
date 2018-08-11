import requests
import json
import os

# From https://openweathermap.org/
API_KEY = os.environ.get("OPEN_WEATHER_MAP_KEY")

def get_temp(city):
    url = f"http://api.openweathermap.org/data/2.5/find?q={city}&APPID={API_KEY}"
    response = requests.get(url)
    json_data = json.loads(response.text)

    k_temp = json_data["list"][0]["main"]["temp"]
    c_temp = k_temp - 273.15

    return c_temp

def main():
    city = input("\nEnter a city name to get weather data for it: ")
    temp = get_temp(city)
    print(f"\nThe temperature for {city.upper()} in degrees Celsius is: {round(temp, 2)}\n")

if __name__ == '__main__':
    main()