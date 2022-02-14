from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(.12)
    snake.move()
    scoreboard.show()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.refresh()

    if snake.head.xcor()>290 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-290:
        scoreboard.reset()
        snake.reset()


    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()