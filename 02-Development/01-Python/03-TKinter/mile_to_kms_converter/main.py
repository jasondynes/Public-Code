import tkinter


def convert_button_clicked():
    miles = float(input_box.get())
    kms = miles * 1.609
    result_label.config(text=kms)


window = tkinter.Tk()
window.title("Miles to KMs converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

left_label = tkinter.Label(text="is equal to", font=("Arial", 14, "normal"))
left_label.grid(column=0, row=1)

# buttons
calc_button = tkinter.Button(text="Calculate", command=convert_button_clicked, font=("Arial", 14, "normal"))
calc_button.grid(column=1, row=2)

tr_label = tkinter.Label(text="Miles", font=("Arial", 14, "normal"))
tr_label.grid(column=2, row=0)

middle_label = tkinter.Label(text="Km", font=("Arial", 14, "normal"))
middle_label.grid(column=2, row=1)

input_box = tkinter.Entry(width=10, font=("Arial", 14, "normal"))
input_box.insert(index=0, string="0")
input_box.grid(column=1, row=0)

result_label = tkinter.Label(text="0", font=("Arial", 14, "normal"))
result_label.grid(column=1, row=1)

window.mainloop()
