from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set shape to circle
        self.color("yellow")  # Set color to yellow
        self.penup()  # Lift pen to avoid drawing lines
        self.x_move = 10  # Initial horizontal movement speed
        self.y_move = 10  # Initial vertical movement speed
        self.move_speed = 0.1  # Initial movement speed

    def move(self):
        # Move the ball by updating its coordinates
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_ball_x(self):
        # Reverse horizontal direction and slightly increase speed
        self.x_move *= -1
        self.move_speed *= 0.95

    def bounce_ball_y(self):
        # Reverse vertical direction
        self.y_move *= -1

    def reset_ball(self):
        # Reset ball position to center, reset speed and horizontal direction
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_ball_x()  # Reset horizontal direction
