import turtle
turtle.title("This is for you Liz")
turtle.setworldcoordinates(-2000,-2000,2000,2000)

def liz(x,y,tilt,radius):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(tilt-45)
    turtle.circle(radius,90)
    turtle.left(90)
    turtle.circle(radius,90)

for tilt in range(0,360,30):
    liz(0,0,tilt,1000)