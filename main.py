from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
GAME_SPEED = 0.1
SCREEN_BACKGROUND = "background.gif"


def new_game():
    """
    Represent brain of our game
    Initialize and start a new game
    """
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # For controlling our snake
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(GAME_SPEED)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.add_point()
            snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    # Wanna play a new game?
    choice = screen.textinput(title="New game", prompt="Do you want to play a new game? \nType yes/no: ")
    if choice:
        if choice.lower() == "yes":
            snake.clear_snake()
            food.clear_food()
            scoreboard.clear_scoreboard()
            new_game()
    else:
        return


screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgpic(SCREEN_BACKGROUND)
screen.title("Snake")
screen.tracer(0)

new_game()

screen.exitonclick()
