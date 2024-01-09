

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Used to populate CSV file
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

csv = pandas.read_csv('50_states.csv')
states = csv.state.to_list()
# print(len(states))
# print(states)
# colorado = csv[csv['state'] == 'Colorado']
states_copy = states.copy()
while True:
    answer_state = screen.textinput(title='Guess the State', prompt="What's another state's name?")
    if answer_state.title() in states:
        print(answer_state.title())
        print(f"Correct! {answer_state.title()} is a U.S. State.")
        state = turtle.Turtle()
        state.penup()
        state.speed(0)
        state.hideturtle()
        coordinates = csv[csv['state'] == answer_state.title()]
        state.goto(float(coordinates.x), float(coordinates.y))
        state.write(answer_state.title(), align="center", font=("Arial", 8, "normal"))
        try:
            states_copy.remove(answer_state.title())
        except:
            pass
    elif answer_state.lower() == 'exit':

        states_save = pandas.DataFrame(states_copy)
        states_save.to_csv('states_to_learn.csv')
        break
    else:
        print(f"Try again... {answer_state.title()} is not a U.S. State.")


# turtle.mainloop()
# screen.exitonclick()  # using mainloop() instead


