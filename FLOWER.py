import turtle


screen = turtle.Screen()
screen.bgcolor("white")


flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(10)  


def draw_petal():
    flower.color("red")
    flower.circle(100, 60)  
    flower.left(120)  
    flower.circle(100, 60)  
    flower.left(120)  


for _ in range(6):
    draw_petal()
    flower.right(60)  


flower.color("green")
flower.right(90)
flower.penup()
flower.goto(0, -100)
flower.pendown()
flower.forward(300)
flower.right(90)
flower.forward(10)


flower.hideturtle()


turtle.done()