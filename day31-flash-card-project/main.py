#Flash card app for Learning French Words
from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#------------------------- NEXT CARD ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

#----------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

#------------------------- REMOVE CARD ------------------------------- #
def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


#------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy - Learn French Words")

flip_timer = window.after(3000, flip_card)

app_width = 900
app_height = 530 + 100 + 100

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
window.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 526/2, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)

#Buttons
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
right_button = Button(image=right_img, highlightthickness=0, command=is_known)

#Labels
card_title = canvas.create_text(400,150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 253, text="", font=("Arial", 40, "bold"))


#PlaceButtons on Grid
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

next_card()







window.mainloop()