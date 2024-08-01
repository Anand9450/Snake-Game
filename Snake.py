from turtle import Turtle
START_LOC = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.boxs = []
        self.CreateSnake()
        self.head = self.boxs[0]

    def CreateSnake(self):
        for loc in START_LOC:
            self.add_box(loc)
    def add_box(self,loc):
        box = Turtle("square")
        box.color("white")
        box.penup()
        box.goto(loc)
        self.boxs.append(box)

    def extend(self):
        self.add_box(self.boxs[-1].position())


    def Move(self):
        for box_no in range(len(self.boxs)-1,0,-1):
            new_x = self.boxs[box_no-1].xcor()
            new_y = self.boxs[box_no - 1].ycor()
            self.boxs[box_no].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.setheading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.setheading != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.setheading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.setheading != LEFT:
            self.head.setheading(RIGHT)
