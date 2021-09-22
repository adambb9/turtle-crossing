import time
from turtle import Screen, Turtle
from player import Player
from cargenerator import CarGenerator
from score import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()






screen.exitonclick()