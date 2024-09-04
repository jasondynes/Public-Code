import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
current_card = {}
to_learn = {}

# open csv file
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text=LANGUAGE, fill="black")
    canvas.itemconfig(card_word, text=current_card[LANGUAGE], fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000, func=flip_card)


def remove_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_img)


def play_game():
    for words in data:
        print(words)
    print(data)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title(f"{LANGUAGE} language Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800, height=526)
front_img = tkinter.PhotoImage(file="./images/card_front.png")
back_img = tkinter.PhotoImage(file="./images/card_back.png")

canvas.create_image(400, 263, image=front_img)
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=front_img)
card_title = canvas.create_text(400, 150, text=LANGUAGE, font=("Arial", 50, "italic"))
card_word = canvas.create_text(400, 263, text="trouve", font=("Arial", 56, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Add Tick button
tick_image = tkinter.PhotoImage(file="./images/right.png")
tick_button = tkinter.Button(image=tick_image, highlightthickness=0, command=remove_card)
tick_button.grid(column=1, row=1)

# Add Cross button
cross_image = tkinter.PhotoImage(file="./images/wrong.png")
cross_button = tkinter.Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)
next_card()

window.mainloop()
