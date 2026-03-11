from turtle import Scree
from score_board import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake Game")
screen.setup(600, 600)
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

            scoreboard.reset()
            snake.reset()
        for segment in snake.segments[1: ]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()


screen.exitonclick()
