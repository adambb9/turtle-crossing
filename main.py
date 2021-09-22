import time
from turtle import Screen, Turtle
from player import Player
from cargenerator import CarGenerator
from score import Scoreboard

#1. Create Screen
#2. Create turtle and move with up key
#3. create method to put turtle at start line after reaching the end
#4. Create Scoreboard class
#5. Increase score by 1 every time turtle gets to the end
#6. Create empty game over method
#7. Create a car
#8. Start car on random point on y axis
#9. detect collision between turtle and car
#10. fill in game over function
#11. add more randomly generated cars
#12. change speed of cars as level increase


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
player.start_pos()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.player_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() > 290:
        scoreboard.increase_score()
        player.start_pos()






screen.exitonclick()