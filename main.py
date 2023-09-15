import tkinter as tk
from PIL import Image, ImageTk
import requests
import datetime as dt
import emoji


def change_theme(hour):
    current_image = background_label.cget("image")
    if current_image == str(initial_photo):
        if hour >= 6 and hour < 18:
            image_path = "day.jpg"
        else:
            image_path = "night.jpg"
    else:
        if hour >= 6 and hour < 18:
            image_path = "day.JPG"
        else:
            image_path = "night.png"

    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    background_label.configure(image=photo)
    background_label.image = photo
    search_entry.delete(0, "end")


def get_information():
    city = search_entry.get()
    if city:
        api_key = "35566f885b8f003dda9abfbe515e6722"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            weather_data = response.json()

            if weather_data["cod"] == 200:
                temperature = weather_data["main"]["temp"]
                description = weather_data['weather'][0]['main']
                humidity = weather_data['main']['humidity']
                wind_speed = weather_data['wind']['speed']

                city_time = dt.datetime.utcnow() + dt.timedelta(seconds=weather_data['timezone'])

                emoji = ""

                if description == "Clear":
                    emoji = "☀️"
                elif description == "Clouds":
                    emoji = "☁️"
                elif description == "Rain":
                    emoji = "🌧️"
                elif description == "Thunderstorm":
                    emoji = "⛈️"
                elif description == "Snow":
                    emoji = "❄️"
                elif description == "Mist" or description == "Haze" or description == "Fog":
                    emoji = "🌫️"
                elif description == "Drizzle":
                    emoji = "🌦️"
                else:
                    emoji = ""

                weather_label.config(text=f"Weather in {city}: {description} {emoji} \nTemperature in {city}:"
                                          f"{temperature}°C \nHumidity: {humidity}%\n"
                                          f"Wind speed: {wind_speed} m/s\n"
                                          f"City time: {city_time.strftime('%Y-%m-%d %H:%M:%S')}")

                change_theme(city_time.hour)
            else:
                weather_label.config(text="City not found")
        except requests.exceptions.RequestException:
            weather_label.config(text="Error occurred")
    else:
        weather_label.config(text="Please enter a city")


window = tk.Tk()
window.title("Weather Forecasts")
window.geometry("500x700")

content_frame = tk.Frame(window)
content_frame.pack(pady=10)

initial_image = Image.open("kaaryar.png")
initial_photo = ImageTk.PhotoImage(initial_image)

background_label = tk.Label(content_frame, image=initial_photo)
background_label.grid(row=0, column=0, columnspan=2)

search_frame = tk.Frame(content_frame, bg="cadetblue2")
search_frame.grid(row=2, column=0, padx=10)

search_entry = tk.Entry(search_frame, font=("Arial", 14))
search_entry.grid(row=0, column=0, padx=10)

search_btn = tk.Button(search_frame, text="Search", command=get_information, bg="azure2", fg="steelblue4")
search_btn.grid(row=0, column=1, padx=5)

weather_label = tk.Label(content_frame, text="", font=("Arial", 14), bg="azure2", fg="blueviolet")
weather_label.grid(row=3, column=0, pady=10)

window.mainloop()
