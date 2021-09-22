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
        self.active_cars = []
        self.shape("square")
        self.turtlesize(1,2,1)
        self.penup()
        self.setheading(180)
        random_color = random.randint(0, 5)
        starting_y_pos = random.randint(-280, 280)
        self.color(COLORS[random_color])
        self.goto(300, starting_y_pos)
        self.car_move()
    
    def car_move(self):
        self.forward(MOVE_INCREMENT)

    def car_generator(self):
        new_car = CarGenerator()
        self.active_cars.append(new_car)



        
