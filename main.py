import datetime as dt
import requests


Base_url = "https://api.openweathermap.org/data/2.5/weather?q="
API_key = "35566f885b8f003dda9abfbe515e6722"

city = "Tehran"

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius

url = (f"https://api.openweathermap.org/data/2.5/weather?q="
                            f"{city}&units=imperial&APPID={API_key}")

response = requests.get(url).json()

temp_celsius = fahrenheit_to_celsius(response['main']['temp'])

feel_like_celsius = fahrenheit_to_celsius(response['main']['feels_like'])

windspeed = response['wind']['speed']

humidity = response['main']['humidity']

description = response['weather'][0]['description']

sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"tempreture in {city}: {temp_celsius:.2f}C")
print(f"tempreture in {city}: feels like: {feel_like_celsius:.2f}C")
print(f"tempreture in {city}: {temp_celsius:.2f}C")
print(f"humidity in {city}: {humidity}%")
print(f"wind speed in {city}: {windspeed}m/s")
print(f"general weather in {city}: {description}")
print(f"sun rises in {city} at {sunrise} local time.")
print(f"sun sets in {city} at {sunset} local time.")
