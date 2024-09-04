import csv
import turtle
import pandas
IMAGE_FILE = "blank_states_img.gif"
OUTPUT_CSV_FILE = "states_to_learn.csv"
TOTAL_ANSWERS = 50
correct_answers = []
screen = turtle.Screen()
screen.title("Name the U.S. States Game")
screen.addshape(IMAGE_FILE)
turtle.shape(IMAGE_FILE)

# code to work out X and Y co-ordinates on the image to create CSV file data
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

total_correct = 0
not_all_answered = True
# create pandas dataframe
states_data = pandas.read_csv("50_states.csv")
all_states_to_guess = states_data.state.to_list()
# guessed_states = []

while not_all_answered:
    answer = screen.textinput(title=f"{total_correct}/50 States Correct", prompt="What's another state's name?").title()
    if answer.lower() == "exit":
        break
    if answer in all_states_to_guess:
        # tracks answers already given in a list
        all_states_to_guess.remove(answer.title())
        total_correct += 1
        # write state name guessed onto map
        state_data = states_data[states_data.state == answer]
        # x_cor = float(states_data.x[states_data.state == answer].to_string(index=False))
        # y_cor = float(states_data.y[states_data.state == answer].to_string(index=False))
        t = turtle.Turtle()
        # hide turtle movements when creating turtle and using it to write text
        t.hideturtle()
        t.penup()
        # move to location of state and then add text
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.to_string(index=False), font=("Verdana", 6, "bold"))
        t.write(state_data.state.item(), font=("Verdana", 6, "bold"))
        if total_correct == 50:
            not_all_answered = False

# states to learn CSV
with open(OUTPUT_CSV_FILE, "w") as learning_file:
    file = csv.writer(learning_file)
    print(all_states_to_guess)
    file.writerow(all_states_to_guess)

screen.exitonclick()






