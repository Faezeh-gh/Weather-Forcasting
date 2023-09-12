import tkinter as tk
from PIL import Image, ImageTk
import requests
import datetime as dt


def change_theme():
    current_image = background_label.cget("image")
    if current_image == str(initial_photo):
        image_path = "night.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        background_label.configure(image=photo)
        background_label.image = photo
        search_entry.delete(0, "end")
    else:
        image_path = "day.jpg"
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        background_label.configure(image=photo)
        background_label.image = photo


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
                description = weather_data['weather'][0]['description']
                humidity = weather_data['main']['humidity']
                wind_speed = weather_data['wind']['speed']
                sunrise = dt.datetime.utcfromtimestamp(weather_data['sys']['sunrise'] + weather_data['timezone'])
                sunset = dt.datetime.utcfromtimestamp(weather_data['sys']['sunset'] + weather_data['timezone'])
                weather_label.config(text=f"Weather in {city}: {description} \nTemperature in {city}: {temperature}°C\nHumidity: {humidity}%\n"
                                          f"Wind speed: {wind_speed} m/s\nThe sun rises at {sunrise} local time."
                                          f"\nThe sun sets at {sunset} local time.")
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

initial_image = Image.open("day.jpg")
initial_photo = ImageTk.PhotoImage(initial_image)

background_label = tk.Label(content_frame, image=initial_photo)
background_label.grid(row=0, column=0, columnspan=2)

change_button = tk.Button(content_frame, text="Change theme", command=change_theme, background="orange")
change_button.grid(row=1, column=0, pady=5)

search_frame = tk.Frame(content_frame)
search_frame.grid(row=2, column=0, padx=10)

search_entry = tk.Entry(search_frame, font=("Arial", 14))
search_entry.grid(row=0, column=0, padx=10)

search_btn = tk.Button(search_frame, text="Search", command=get_information)
search_btn.grid(row=0, column=1, padx=5)

weather_label = tk.Label(content_frame, text="", font=("Arial", 16))
weather_label.grid(row=3, column=0, pady=10)


window.mainloop()
