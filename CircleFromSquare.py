import turtle
screen = turtle.getscreen()
screen.bgcolor("red")
slomo = turtle.Turtle()
def draw_square():
    #draw
    slomo.shape("turtle")
    slomo.color("yellow")
    cnt = 0
    while cnt < 124 :
        slomo.forward(100)
        slomo.right(90)
        cnt +=1
        if(cnt%4 == 0) :
            slomo.right(10)
    screen.exitonclick()

draw_square()
