from turtle import Turtle

class Paddle(Turtle):
    """
    Paddle class for the Pong game.

    Represents a vertical paddle controlled by a player. Can move up and down
    within the screen boundaries. Inherits from Turtle.
    """

    def __init__(self, x_coordinate):
        """
        Initialize a paddle at the given x-coordinate.

        Args:
            x_coordinate (int): The x-coordinate where the paddle is placed.
        """
        super().__init__()
        self.y_coordinate = x_coordinate  # Store starting x-coordinate
        self.shape("square")              # Paddle shape
        self.color("DarkGreen")           # Paddle color
        self.setheading(90)               # Point upwards
        self.penup()                      # Do not draw when moving
        self.shapesize(1, 5)              # Scale paddle (1 height x 5 width)
        self.goto(x_coordinate, 0)        # Position paddle at x-coordinate

    def paddle_up(self):
        """
        Move the paddle upward by 50 units, unless it reaches the top boundary.
        """
        if self.ycor() != 250:
            self.forward(50)

    def paddle_down(self):
        """
        Move the paddle downward by 50 units, unless it reaches the bottom boundary.
        """
        if self.ycor() != -250:
            self.backward(50)
