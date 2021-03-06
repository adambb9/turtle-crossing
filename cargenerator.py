from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


#7. Create a car
#8. Start car on random point on y axis
#11. add more randomly generated cars
#12. change speed of cars as level increase


class CarGenerator:

    def __init__(self):
        self.active_cars = []
        self.num_active_cars = 10
        self.car_speed = 0.1
    
    def move_cars(self):
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
            new_car.goto(300, random.randint(-200,280))
            new_car.forward(STARTING_MOVE_DISTANCE)
            self.active_cars.append(new_car)

    def increase_active_cars(self, num):
        self.num_active_cars += num

    def remove_car(self):
        for car in self.active_cars:
            index = self.active_cars.index(car)
            if car.xcor() < -320:
                self.active_cars.pop(index)

    def increase_car_speed(self):
        self.car_speed *= 0.9

    






        
