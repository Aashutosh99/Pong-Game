from turtle import Turtle

class Scoreboard(Turtle):
    """
    Scoreboard class for the Pong game.

    Displays and updates the scores for the left and right players.
    Inherits from Turtle to write text on the screen.
    """

    def __init__(self):
        """
        Initialize the scoreboard with both players' scores set to zero.
        Positions the scoreboard and updates it on the screen.
        """
        super().__init__()
        self.color("white")       # Text color
        self.hideturtle()         # Hide the turtle cursor
        self.penup()              # Do not draw when moving
        self.l_score = 0          # Left player's score
        self.r_score = 0          # Right player's score
        self.update_score()       # Display initial scores

    def update_score(self):
        """
        Clear previous score display and write the current left and right scores
        at designated positions on the screen.
        """
        self.clear()
        self.goto(-100, 280)  # Position for left score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 280)   # Position for right score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """
        Increase the left player's score by 1 and update the scoreboard.
        """
        self.l_score += 1
        self.update_score()

    def r_point(self):
        """
        Increase the right player's score by 1 and update the scoreboard.
        """
        self.r_score += 1
        self.update_score()
