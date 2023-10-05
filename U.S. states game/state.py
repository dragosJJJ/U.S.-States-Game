from turtle import Turtle

FONT = (("Courier", 8))

class State(Turtle):
    def __init__(self, state_name, position):
        super().__init__()

        self.ht()
        self.penup()
        self.goto(position)
        self.write(f'{state_name}', font=FONT)

