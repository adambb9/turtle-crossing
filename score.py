from turtle import Turtle

ALIGNMENT = "center"

FONT = ("Courier", 16, "normal")

#4. Create Scoreboard class
#5. Increase score by 1 every time turtle gets to the end
#6. Create game over method

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        x_pos, y_pos = -230, 250
        self.goto(x_pos, y_pos)
        self.score = 1
        self.update_score()


    def update_score(self):
        self.write(F"Level: {self.score}", align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

