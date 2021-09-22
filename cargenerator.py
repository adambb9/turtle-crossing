from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_Y_POS = random.randint(-280,280)


#7. Create a car
#8. Start car on random point on y axis


class CarGenerator(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.turtlesize(1,2,1)
        self.penup()
        self.setheading(180)
        randnum = random.randint(0, 6)
        self.color(COLORS[randnum])
        self.start_pos()

    def start_pos(self):
        self.goto(300, STARTING_Y_POS)
    
    def car_move(self):
        self.forward(MOVE_INCREMENT)


        
