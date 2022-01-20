from turtle import Turtle
import time

START_X_POS = [-40, -20, 0]
START_Y_POS = 0
DEFAULT_HEADING = 90
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_lenght = []
        self.create_snake()

    def snake_head(self):
        return self.snake_lenght[len(self.snake_lenght) - 1]

    def create_snake(self):
        for xpos in START_X_POS:
            self.add_segment(xpos, START_Y_POS, DEFAULT_HEADING)

    def move_forward(self):
        for cell_num in range(len(self.snake_lenght) - 1):
            new_x = self.snake_lenght[1 + cell_num].xcor()
            new_y = self.snake_lenght[1 + cell_num].ycor()
            self.snake_lenght[cell_num].goto(x=new_x, y=new_y)
        self.snake_head().forward(MOVE_DISTANCE)

    def turn_up(self):
        if self.snake_head().heading() == 0 or self.snake_head().heading() == 180:
            self.snake_head().setheading(90)
        else:
            pass

    def turn_down(self):
        if self.snake_head().heading() == 0 or self.snake_head().heading() == 180:
            self.snake_head().setheading(270)
        else:
            pass

    def turn_right(self):
        if self.snake_head().heading() == 90 or self.snake_head().heading() == 270:
            self.snake_head().setheading(0)
        else:
            pass

    def turn_left(self):
        if self.snake_head().heading() == 90 or self.snake_head().heading() == 270:
            self.snake_head().setheading(180)
        else:
            pass

    def extend(self):
        self.add_segment(self.snake_head().xcor(), self.snake_head().ycor(), self.snake_head().heading())

    def add_segment(self, xpos, ypos, heading):
        new_cell = Turtle(shape="square")
        new_cell.setheading(heading)
        new_cell.penup()
        new_cell.color("white")
        new_cell.goto(x=xpos, y=ypos)
        self.snake_lenght.append(new_cell)
