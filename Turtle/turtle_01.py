from turtle import Turtle, Screen

tim = Turtle()
tim.speed(1)
lenth = 50
angle = 90
for i in range(10):
    tim.forward(lenth)
    tim.right(angle)
    tim.forward(lenth+50)
    # lenth -= 10
    # angle += 5

# tim.left(90)


screen = Screen()
screen.exitonclick()