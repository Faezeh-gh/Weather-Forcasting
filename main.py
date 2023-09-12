import tkinter as tk
import requests


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
                temperature_label.config(text=f"Temperature in {city}: {temperature}°C")
            else:
                temperature_label.config(text="City not found")
        except requests.exceptions.RequestException:
            temperature_label.config(text="Error occurred")
    else:
        temperature_label.config(text="Please enter a city")


root = tk.Tk()
root.title("City Temperature")

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, font=("Arial", 14))
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Search", command=get_temperature)
search_button.pack(side=tk.LEFT)

temperature_label = tk.Label(root, font=("Arial", 16))
temperature_label.pack(pady=10)


root.mainloop()
