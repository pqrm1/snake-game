from turtle import Screen,Turtle
import time
from snake import Snake
from fod import Food
from score import Score
import borders

screen=Screen()
screen.setup(500,500)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Score()

borders.bor()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    #collison with the food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #collison with the walls
    if snake.head.xcor()>450 or snake.head.xcor()<-450 or snake.head.ycor()>430 or snake.head.ycor()<-480:
        scoreboard.g_over()
        game_is_on=False

    #collision with itself
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.g_over()


screen.exitonclick()