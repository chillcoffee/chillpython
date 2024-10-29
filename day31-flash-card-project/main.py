#Flash card app for Learning French Words
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

#------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

app_width = 600
app_height = 600

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

canvas = Canvas(width=800, height=526)








window.mainloop()