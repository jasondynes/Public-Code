import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    tick_label.config(text="")
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    # If 1st, 3rd, 5h, 7th rep:
    if reps % 2 == 1:
        title_label.config(text="Work", fg=GREEN)
        countdown(work_secs)
    elif reps % 8 == 0:
        # if it's 8th rep then
        title_label.config(text="Break", fg=RED)
        countdown(long_break_secs)
    elif reps % 2 == 0:
        # if it's 2nd, 4th, 6th rep
        title_label.config(text="Break", fg=PINK)
        countdown(short_break_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = "0" + str(count_secs)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
            tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# add TIMER text
title_label = tkinter.Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# Add START button
start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Add RESET button
reset_button = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Add tick image
tick_label = tkinter.Label(fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

window.mainloop()
