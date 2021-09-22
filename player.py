from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 200


#2. Create turtle and move with up key
#3. create method to put turtle at start line after reaching the end

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.setheading(90)

    def start_pos(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()

    def player_move(self):
        self.forward(10)
