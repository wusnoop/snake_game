from turtle import Turtle
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.all_square =[]
        self.create_snake()
        self.head = self.all_square[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        wus = Turtle(shape="square")
        wus.color("white")
        wus.penup()
        wus.goto(position)
        self.all_square.append(wus)

    def extend(self):
        self.add_segment(self.all_square[-1].position())

    def move(self):
        for seg_num in range(len(self.all_square) - 1, 0, -1):
            new_x = self.all_square[seg_num - 1].xcor()
            new_y = self.all_square[seg_num - 1].ycor()
            self.all_square[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)