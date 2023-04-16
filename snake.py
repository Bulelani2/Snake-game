from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_PASSE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for pos in POSITION:
            self.add_body(pos)

    def add_body(self, pos):
        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color("white")
        tim.goto(pos)
        self.body.append(tim)

    def reset(self):
        for bod in self.body:
            bod.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def extend(self):
        # add a new body
        self.add_body(self.body[-1].position())

    def move(self):
        for a in range(len(self.body) - 1, 0, -1):
            new_x = self.body[a - 1].xcor()
            new_y = self.body[a - 1].ycor()
            self.body[a].goto(new_x, new_y)
        self.head.forward(MOVE_PASSE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
