from turtle import Turtle, Screen
import random
import time

my_screen = Screen()
my_screen.setup(500, 500)

positions = [(-230, 0 ),(-230, 40),(-230, -40)]
colors = ["red", "green", "blue"]
turtles = []


for i in range(len(positions)):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(positions[i])
    turtles.append(new_turtle)


my_turtle = Turtle()

steps = [10, 20, 25, 15, 30, 35]
game_on = True

winner = []  

user_choice = my_screen.textinput("turtle race","Please choose one option: (blue, red, green): ").lower()
while game_on:
    
    colors = ("red", "blue", "green")
    if user_choice in colors:
        for turtle in turtles:
            time.sleep(0.1)
            turtle.forward(random.choice(steps))
            if turtle.xcor() > 230:
                winner.append(turtle.color())
                game_on = False
                if user_choice == "".join(winner):
                    my_screen.bgcolor("black")
                else:
                    my_screen.bgcolor("red")
                    my_turtle.color("white")
                    my_turtle.write("loser", align="center", font=("arial", 35, "normal"))



my_screen.exitonclick()