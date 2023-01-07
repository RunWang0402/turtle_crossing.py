from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.total=[]
        self.move_distance = 5


    def cars(self):
        randomm=random.randint(0,6)
        if randomm==1:
            car=Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.turtlesize(stretch_len=2,stretch_wid=1)
            car.setheading(180)
            car.penup()
            random_y=random.randint(-250,250)
            car.setposition(300,random_y)
            self.total.append(car)


    def move(self):
        for car in self.total:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += 10





