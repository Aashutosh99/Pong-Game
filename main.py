import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from background import Background

"""
Pong Game 🎾

A classic 2-player Pong game using Python's turtle module.
Players control paddles to bounce the ball and score points against each other.
The game features ball-wall and ball-paddle collision detection, a scoreboard,
and smooth gameplay.
"""

# Set up the screen
screen = Screen()
screen.setup(width=1000, height=800)
screen.title("Pong")
screen.bgcolor("#98FF98")  # Set background color
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create paddles, ball, scoreboard, and background
paddle = Paddle(350)      # Right paddle
paddle_2 = Paddle(-350)   # Left paddle
ball = Ball()              # The game ball
background = Background()  # Additional visuals/background
scoreboard = Scoreboard()  # Display scores

# Listen for key presses to control paddles
screen.listen()
screen.onkey(paddle.paddle_up, "Up")       # Move right paddle up
screen.onkey(paddle.paddle_down, "Down")   # Move right paddle down
screen.onkey(paddle_2.paddle_up, "w")      # Move left paddle up
screen.onkey(paddle_2.paddle_down, "s")    # Move left paddle down

game_is_on = True
while game_is_on:
    """
    Main game loop:
    - Update the screen
    - Move the ball
    - Check for collisions with paddles or walls
    - Reset ball and update scores when it goes out of bounds
    """
    screen.update()

    time.sleep(ball.move_speed)  # Control the ball speed
    ball.move()                  # Move the ball

    # Detect collision with paddles and bounce
    if paddle.distance(ball) < 50 and ball.xcor() > 330 or \
       paddle_2.distance(ball) < 50 and ball.xcor() < -330:
        ball.bounce_ball_x()

    # Detect collision with top and bottom walls and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    # Ball goes out of bounds on the right
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()  # Increment left player's score

    # Ball goes out of bounds on the left
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()  # Increment right player's score

# Close the game window when clicked
screen.exitonclick()
