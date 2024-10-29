#Password Generator
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

FONT = "Arial"
fs = 12

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    input_pass.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    email = input_username.get()
    password = input_pass.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            input_website.delete(0, END)
            input_pass.delete(0, END)
            input_website.focus()
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if len(website) == 0:
            messagebox.showinfo(title="Empty Search", message="No search key to find.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
                pyperclip.copy(password)
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")
# app_width = 600
# app_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# x = (screen_width / 2) - (app_width / 2)
# y = (screen_height / 2) - (app_height / 2)
# window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(row=0, column=1)

#Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_username = Label(text="Email/Username:")
label_username.grid(row=2, column=0)
label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0)

#Entries
input_website = Entry(width=33)
input_website.grid(row=1, column=1)
input_website.focus()
input_username = Entry(width=51)
input_username.grid(row=2, column=1, columnspan=2)
input_username.insert(0, "ruffaresentes@gmail.com")
input_pass = Entry(width=33)
input_pass.grid(row=3, column=1)

#Buttons
button_search = Button(text="Search", highlightthickness=0, command=find_password, width=15)
button_search.grid(row=1, column=2)
button_generate = Button(text="Generate Password", highlightthickness=0, command=generate)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=43, command=save)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
