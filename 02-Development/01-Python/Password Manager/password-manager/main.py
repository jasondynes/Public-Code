import tkinter
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Arial"
FILE_NAME = "data.txt"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password = password_letters + password_symbols + password_numbers

    # random shuffle method
    random.shuffle(password)
    scrambled_password = "".join(password)
    # copies password into clipboard for user to paste direct into login screen after clicking generate
    pyperclip.copy(scrambled_password)
    pwd_field.delete(0, 'end')
    pwd_field.insert(0, scrambled_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():á
    # capture field contents from GUI
    website = website_field.get()
    email = email_field.get()
    password = pwd_field.get()
    # if any field is blank then give use a message informing them and do not save
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        is_ok = False
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        # check user is happy with contents via message dialog box
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email} \n"
                                                              f"Password: {password} \nIs it OK to save?")
    if is_ok:
        # save details to .txt file
        with open(FILE_NAME, "a") as pwd_file:
            pwd_file.write(f"{website}|{email}|{password}\n")
            # delete contents of 2 of 3 fields (leave email)
            website_field.delete(0, 'end')
            pwd_field.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# # add Website label
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

# add website field
website_field = tkinter.Entry(width=50)
website_field.grid(column=1, row=1, columnspan=2)
website_field.focus()
#
# # add Email / Username label
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

# # add Email / Username field
email_field = tkinter.Entry(width=50)
email_field.grid(column=1, row=2, columnspan=2)
email_field.insert(0, "jason.dynes@gmail.com")
#
# # add Password label
pwd_label = tkinter.Label(text="Password:")
pwd_label.grid(column=0, row=3)

# # add Password field
pwd_field = tkinter.Entry(width=40)
pwd_field.grid(column=1, row=3)

# # Add Generate Password button
gen_pwd_button = tkinter.Button(text="Generate", padx=0, command=gen_password)
gen_pwd_button.grid(column=2, row=3)

# # Add 'add' button
save_pwd_button = tkinter.Button(text="Add", width=36, command=save)
save_pwd_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
