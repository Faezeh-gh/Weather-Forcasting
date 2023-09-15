import tkinter as tk
from PIL import Image, ImageTk
import requests
import datetime


def change_background(city):
    time_info = get_city_time(city)
    current_hour = time_info.hour
    image_path = ""
    if current_hour >= 6 and current_hour < 18:
        image_path = "day.jpg"
    else:
        image_path = "night.jpg"

    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    background_label.configure(image=photo)
    background_label.image = photo


def get_city_time(city):
    api_key = "35566f885b8f003dda9abfbe515e6722"
    url = f"http://worldtimeapi.org/api/timezone/{city}"
    try:
        response = requests.get(url)
        time_data = response.json()
        if "datetime" in time_data:
            time_str = time_data["datetime"]
            time_info = datetime.datetime.strptime(time_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            return time_info
    except requests.exceptions.RequestException:
        pass

    return None


def get_temperature():
    city = search_entry.get()
    if city:
        api_key = "35566f885b8f003dda9abfbe515e6722"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(url)
            weather_data = response.json()

            if weather_data["cod"] == 200:
                temperature = weather_data["main"]["temp"]
                weather_label.config(text=f"Temperature in {city}: {temperature}°C")
                change_background(city)
            else:
                weather_label.config(text="City not found")
        except requests.exceptions.RequestException:
            weather_label.config(text="Error occurred")
    else:
        weather_label.config(text="Please enter a city")


window = tk.Tk()
window.title("Weather Forecasting")

initial_image = Image.open("day.jpg")
initial_photo = ImageTk.PhotoImage(initial_image)

background_label = tk.Label(window, image=initial_photo)
background_label.pack()

search_frame = tk.Frame(window)
search_frame.pack(padx=10)

search_entry = tk.Entry(search_frame, font=("Arial", 14))
search_entry.grid(row=0, column=0, padx=10)

search_btn = tk.Button(search_frame, text="Search", command=get_temperature)
search_btn.grid(row=0, column=1, padx=5)

weather_label = tk.Label(window, text="", font=("Arial", 16))
weather_label.pack(pady=10)

window.mainloop()
