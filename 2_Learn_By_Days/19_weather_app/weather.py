import json
from pprint import pprint
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")


def get_current_weather():
    print("\n*********** Get Current Weather Conditions ***********\n")

    city = input("\nPlease enter a city name : ")

    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=imperial"

    response = requests.get(request_url)

    if response.status_code == 200:
        weather_data = response.json()  # object
        # print()
        # pprint(weather_data)
        # print()

        if __name__ == "__main__":
            print()
            print(json.dumps(weather_data, indent=4, sort_keys=True))
            print()
        else:
            print(f"\nCurrent weather for '{weather_data["name"]}'")
            print(f"\nThe temperature is {weather_data["main"]["temp"]}\u00B0C")
            print(
                f"\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"].capitalize()}\n"
            )
    else:
        print(f"Error - {response.status_code} - {response.text}")


if __name__ == "__main__":
    get_current_weather()
