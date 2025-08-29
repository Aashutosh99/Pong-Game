from turtle import Turtle

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BORDER_PEN_SIZE = 5
BORDER_COLOR = "DarkGreen"
CENTER_LINE_COLOR = "DarkGreen"
CENTER_LINE_SEGMENT_LENGTH = 10
CIRCLE_COLOR = "LightBlue"
CIRCLE_RADIUS = 50
INSIDE_COLOR = "aqua"

class Background(Turtle):
    """
    Background class for the Pong game.

    Draws the game arena, including:
    - The outer border
    - The filled inside area
    - The dashed center line
    - A filled circle at the center
    Inherits from Turtle to draw graphics.
    """

    def __init__(self):
        """
        Initialize the background by drawing all visual elements:
        border, filled inside, center line, and the center circle.
        """
        super().__init__()
        self.hideturtle()
        self.pensize(BORDER_PEN_SIZE)
        self.draw_border()
        self.fill_inside()
        self.draw_center_line()
        self.draw_filled_circle()

    def draw_border(self):
        """
        Draw a rectangular border around the game area using BORDER_COLOR.
        """
        self.color(BORDER_COLOR)
        self.penup()
        self.goto(-SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.pendown()
        self.setheading(0)
        for _ in range(2):
            self.forward(SCREEN_WIDTH)
            self.right(90)
            self.forward(SCREEN_HEIGHT)
            self.right(90)

    def fill_inside(self):
        """
        Fill the inner area of the game arena with INSIDE_COLOR.
        """
        self.penup()
        self.goto(-SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.pendown()
        self.color(INSIDE_COLOR)
        self.begin_fill()
        self.setheading(0)
        for _ in range(2):
            self.forward(SCREEN_WIDTH)
            self.right(90)
            self.forward(SCREEN_HEIGHT)
            self.right(90)
        self.end_fill()

    def draw_center_line(self):
        """
        Draw a dashed vertical line at the center of the screen
        using CENTER_LINE_COLOR.
        """
        self.color(CENTER_LINE_COLOR)
        self.penup()
        self.goto(0, SCREEN_HEIGHT // 2)
        self.setheading(270)
        self.pendown()
        for _ in range(SCREEN_HEIGHT // (2 * CENTER_LINE_SEGMENT_LENGTH)):
            self.forward(CENTER_LINE_SEGMENT_LENGTH)
            self.penup()
            self.forward(CENTER_LINE_SEGMENT_LENGTH)
            self.pendown()

    def draw_filled_circle(self):
        """
        Draw a filled circle at the center of the screen using CIRCLE_COLOR.
        """
        self.penup()
        self.goto(-50, 0)
        self.pendown()
        self.color(CIRCLE_COLOR)
        self.begin_fill()
        self.circle(CIRCLE_RADIUS)
        self.end_fill()
