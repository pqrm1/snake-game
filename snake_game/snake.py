from turtle import Turtle

MOV_DIS = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0)]

class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segs(i)

    def add_segs(self,position):
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segment.append(tim)

    def extend(self):
        self.add_segs(self.segment[-1].position())

    def move(self):
        for segs in range(len(self.segment) - 1, 0, -1):
            x_cord = self.segment[segs - 1].xcor()
            y_cord = self.segment[segs - 1].ycor()
            self.segment[segs].goto(x_cord, y_cord)

        self.head.forward(MOV_DIS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)