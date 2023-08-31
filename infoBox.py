from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

LABEL_FONT = "Adobe Gothic Std"


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'
        , 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'
        , 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    Username = Username_entry.get()
    email_address = email_entry.get()
    new_password = password_entry.get()

    if len(Username) == 0 or len(new_password) == 0:
        messagebox.showwarning("Oops!", "Please don't leave any boxes empty.")
    else:
        is_ok = messagebox.askokcancel(title=Username, message=f"These are the details entered: \nEmail: "
                                                                   f"{email_address} "
                                                                   f"\nPassword: {new_password} \nIs it ok to save?")
        if is_ok:
            with open("my_passwords.txt", "a") as data_file:
                data_file.write(f"{Username} *|* {email_address} *|* {new_password}\n")
                Username_entry.delete(0, END)
                password_entry.delete(0, END)


root = Tk()
root.title("Information Box")
root.config(padx=50, pady=50)

canvas = Canvas(height=300, width=300)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

Username_label = Label(text="Username:", font=(LABEL_FONT, 15))
Username_label.grid(column=0, row=1, sticky=E)

email_label = Label(text="Email:", font=(LABEL_FONT, 15))
email_label.grid(column=0, row=2, sticky=E)

password_label = Label(text="Password:", font=(LABEL_FONT, 15))
password_label.grid(column=0, row=3, sticky=E)

Username_entry = Entry(width=37)
Username_entry.grid(column=1, row=1, columnspan=2, pady=5)
Username_entry.focus()

email_entry = Entry(width=37)
email_entry.grid(column=1, row=2, columnspan=2, pady=5)
email_entry.insert(0, "designguru14-shoppie@yahoo.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky=W, pady=5)

password_button = Button(text="Enter Password", padx=5, pady=5, command=generate_password)
password_button.grid(column=2, row=3)

add_info_button = Button(text="Add", width=38, pady=5, command=save)
add_info_button.grid(column=1, row=4, columnspan=2, sticky=W)

root.mainloop()