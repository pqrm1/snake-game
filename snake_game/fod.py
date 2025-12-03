from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        randomx = random.randint(-400, 400)
        randomy = random.randint(-450, 420)
        self.goto(randomx, randomy)