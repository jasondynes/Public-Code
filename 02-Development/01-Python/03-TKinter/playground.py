import tkinter

def button_clicked():
    # my_label.config(text="Button was clicked")
    message = input_box.get()
    my_label.config(text=message)
    my_label.grid(x=0, y=0)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=1000, height=800)
# padding around window elements
window.config(padx=20,pady=20)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# various ways to change text such as
my_label["text"] = "New Text Label"
my_label.config(text="New Text Label")
# my_label.pack()
# my_label.pack(side="left")
# when you want to specify exact x and y placement use PLACE method
my_label.place(x=50, y=50)
# also can use GRID method
my_label.grid(column=0, row=0)

# buttons
button = tkinter.Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# buttons
new_button = tkinter.Button(text="Click Me Again", command=button_clicked)
# button.pack()
new_button.grid(column=2, row=0)

# Entry class for TKinter to create an input field
input_box = tkinter.Entry(width=20)
input_box.insert(index=0, string="enter something here....")
# index param on insert method only works for a populated field
# input_box.insert(index=10, string="enter something here....")
# input_box.pack()
input_box.grid(column=3, row=2)

window.mainloop()
