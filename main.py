import tkinter as tk
from PIL import Image, ImageTk
import requests


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
            else:
                weather_label.config(text="City not found")
        except requests.exceptions.RequestException:
            weather_label.config(text="Error occurred")
    else:
        weather_label.config(text="Please enter a city")


window = tk.Tk()
window.title("Weather Forecasts")

content_frame = tk.Frame(window)
content_frame.pack(pady=10)

initial_image = Image.open("day.jpg")
initial_photo = ImageTk.PhotoImage(initial_image)

background_label = tk.Label(content_frame, image=initial_photo)
background_label.grid(row=0, column=0, columnspan=2)

change_button = tk.Button(content_frame, text="Change theme", command=change_theme, background="blue")
change_button.grid(row=1, column=0, pady=5)

search_frame = tk.Frame(content_frame)
search_frame.grid(row=2, column=0, padx=10)

search_entry = tk.Entry(search_frame, font=("Arial", 14))
search_entry.grid(row=0, column=0, padx=10)

search_btn = tk.Button(search_frame, text="Search", command=get_temperature)
search_btn.grid(row=0, column=1, padx=5)

weather_label = tk.Label(content_frame, text="", font=("Arial", 16))
weather_label.grid(row=3, column=0, pady=10)


window.mainloop()
