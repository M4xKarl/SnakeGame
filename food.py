from turtle import Turtle
import random

MAX_WIDTH = 280
MIN_WIDTH = -280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(MIN_WIDTH, MAX_WIDTH)
        random_y = random.randint(MIN_WIDTH, MAX_WIDTH)
        self.goto(random_x, random_y)