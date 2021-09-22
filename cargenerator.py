from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_Y_POS = random.randint(-280,280)


#7. Create a car
#8. Start car on random point on y axis


class CarGenerator:

    def __init__(self):
        self.active_cars = []
        self.num_active_cars = 10
    
    def car_move(self):
        for car in self.active_cars:
            car.forward(MOVE_INCREMENT)

    def car_generator(self):
        if len(self.active_cars) < self.num_active_cars:
            new_car = Turtle()
            new_car.shape("square")
            new_car.turtlesize(1,2,1)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(COLORS[random.randint(0,5)])
            new_car.goto(300, random.randint(-250,280))
            self.active_cars.append(new_car)

    def increase_active_cars(self, num):
        self.num_active_cars += num

    def remove_car(self):
        for car in self.active_cars:
            index = self.active_cars.index(car)
            if car.xcor() < -310:
                self.active_cars.pop(index)






        
