from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

sc = Screen()

#making the screen sizes ready so that go for the next move
sc.title("Welcome to the Ping Pong Game!!!")
sc.setup(800,600)
sc.bgcolor("grey")
sc.tracer(0)

ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
score = ScoreBoard()

sc.listen()
sc.onkey(r_paddle.go_up, "Up")
sc.onkey(r_paddle.go_down, "Down")

sc.onkey(l_paddle.go_up, "a")
sc.onkey(l_paddle.go_down, "z")

is_game_on = True

while is_game_on:
    sc.update()
    time.sleep(0.1)
    ball.move()
    
    if ball.ycor() >280 or ball.ycor() < -280:
        ball.bounce_y()
        
    #detect the colision
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50 or ball.xcor() > -340 and ball.distance(l_paddle) < 50 :
        ball.bounce_x()
    
    #reset the position
    if ball.xcor() >380:
        ball.reset_position()
        score.l_point()
        
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
    
sc.exitonclick()




