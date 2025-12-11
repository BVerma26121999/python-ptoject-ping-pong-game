from turtle import Turtle

#create the object of turtle and screen classes
class Paddle(Turtle):
    def __init__(self,dist):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(dist)
    
    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(),new_y)

