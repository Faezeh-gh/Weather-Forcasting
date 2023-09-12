import tkinter as tk
from PIL import ImageTk, Image


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


def perform_search():
    search_query = search_entry.get()
    weather_label.config(text=f"Weather for '{search_query}': Sunny ☀️")
    """if search_query:
        results = []
        if results:
            print("displaying search results:", results)
        else:
            print("no research results found for query:", search_query)
    else:
        print("search query is empty")"""


window = tk.Tk()
window.title("Weather Forcasting")

initial_image = Image.open("day.jpg")
initial_photo = ImageTk.PhotoImage(initial_image)

background_label = tk.Label(window, image=initial_photo)
background_label.pack()

change_button = tk.Button(window, text="Change theme", command=change_theme, background="yellow")
change_button.pack()

search_frame = tk.Frame(window, bg="white")
search_frame.pack(fill="x", padx=10, pady=(0, 10))

search_entry = tk.Entry(search_frame)
search_entry.pack(side="left", expand=True, padx=(0, 5))

search_btn = tk.Button(search_frame, text="Search", command=perform_search)
search_btn.pack(side="right")

weather_label = tk.Label(window, text="", font=("Arial", 14))
weather_label.pack(pady=10)


window.mainloop()
