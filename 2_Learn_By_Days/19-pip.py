# What is PIP?
# PIP is a package manager for Python packages, or modules if you like.

# What is a Package?
# A package contains all the files you need for a module.
# Modules are Python code libraries you can include in your project.


# Install PIP
# If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

# pip install pip


# Download a Package
# Downloading a package is very easy.
# Open the command line interface and tell PIP to download the package you want.
# Navigate your command line to the location of Python's script directory, and type the following:


# pip install camelcase


#  Create a Virtual Environment
# python -m venv my_venv
# my_venv\Scripts\activate

# for GitBash 
# source my_venv/Scripts/activate
# . my_venv/Scripts/activate

# pip install <package-name>
# pip freeze > requirements.txt
# pip install -r requirements.txt
# deactivate


# -----------------------------------------------------------------------------------------


# py -m pip install requests==2.30.0
# py -m pip install -U requests
# py -m pip uninstall requests

# creating a virtual environment
# py -m venv .venv
# source .venv/SCripts/activate
# deactivate

# pip list ( global ) => lots of package
# pip list ( local venv ) => only few package

# pip show requests

# py -m pip install python-dotenv

# py -m pip freeze > requirements.txt


# * Error fix => .venv clash
# * deactivate
# * => rm -rf .venv
# * python -m venv .venv
# * source .venv/Scripts/activate
# * py -m pip install python-dotenv requests


# try:
#     from dotenv import load_dotenv
#     print("dotenv imported successfully!")
# except ModuleNotFoundError as e:
#     print(f"Error: {e}")


# # request_url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}&units=imperial"
# # request_url = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}&units=imperial"


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

        # if __name__ == "__main__":
        #     print()
        #     print(json.dumps(weather_data, indent=4, sort_keys=True))
        #     print()
        # else:
        print(f"\nCurrent weather for '{weather_data["name"]}'")
        print(f"\nThe temperature is {weather_data["main"]["temp"]}\u00B0C")
        print(f"\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"].capitalize()}\n")
    else:
        print(f"Error - {response.status_code} - {response.text}")


if __name__ == "__main__":
    get_current_weather()
