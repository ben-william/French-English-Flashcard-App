from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE = '#FFFFFF'
BLACK = '#000000'

# ------------- Data Handling --------

df = pd.read_csv('./data/french_words.csv')

# Run this line to refresh all words to 'to learn' file
# df.to_csv('./words_to_learn.csv', index=False)
try:
    to_learn = pd.read_csv('./words_to_learn.csv').to_dict(orient='records')
except FileNotFoundError:
    to_learn = pd.read_csv('./data/french_words.csv').to_dict(orient='records')

print(to_learn)
# ------------- Functionality --------
next_word = {}

wrong_button_clicked = False

def check():
    to_learn.remove(next_word)
    pd.DataFrame(to_learn).to_csv('./data/words_to_learn.csv', index=False)
    print(len(to_learn))
    next_card()


def next_card():
    global next_word, flip_timer
    next_word = random.choice(to_learn)
    card.itemconfig(card_bg, image=card_front_img)
    card.itemconfig(language, text='French', fill=BLACK)
    card.itemconfig(word, text=f'{next_word["French"]}', fill=BLACK)
    # keep card from flipping until 3 sec are up, regardless of clicks
    window.after_cancel(flip_timer)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global check_btn
    card.itemconfig(card_bg, image=card_back_img)
    card.itemconfig(language, text='English', fill=WHITE)
    card.itemconfig(word, text=f'{next_word["English"]}', fill=WHITE)
    print(len(to_learn))


# ------------- UI -------------------


window = Tk()
window.title("Flashcard Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flip Timer
flip_timer = window.after(3000, flip_card)

# Flashcard
card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')
card = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg = card.create_image(400, 263, image=card_front_img)
card.config(width=800, height=526)
card.grid(row=0, column=0, columnspan=2)

# Text
language = card.create_text(400, 150, text='', font=("Arial", 40, 'italic'), fill=BLACK)
word = card.create_text(400, 250, text='', font=("Arial", 60, 'bold'), fill=BLACK)

# Buttons
wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightbackground=BACKGROUND_COLOR, command=check)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()