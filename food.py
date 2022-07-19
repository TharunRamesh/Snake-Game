from turtle import Turtle
import random
# SHAPES = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
# FSHAPE = input(f"select the shape of food among the list {SHAPES}: ")
# COLORS = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan",
#           "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
# FCOLOR = input(f"select the shape of food among the list {COLORS}: ")

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        #you can choose any shape of food
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-265, 265), y=random.randint(-260, 260))
