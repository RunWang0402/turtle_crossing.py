import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


scoreboard=Scoreboard()
car_manager=CarManager()
#car_manager.cars() I also did creating a bunch of cars at once and make them run
player=Player()

screen.listen()
screen.onkey(player.move_forward,"Up")


game_is_on = True
while game_is_on:
    scoreboard.writee()
    car_manager.cars()
    car_manager.move()

    for car in car_manager.total:
        if player.distance(car)<30:
            game_is_on=False
            scoreboard.game_over()

    if player.ycor()>280:
        player.reach_the_end()
        car_manager.increase_speed()
        scoreboard.add_level()





    time.sleep(0.1)
    screen.update()



screen.exitonclick()