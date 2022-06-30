import turtle
t = turtle.Turtle()
t.ht()
t.penup()
t.goto(300, 30)
t.pendown()
t.speed(0)
t.color('green')
b = 200
while b > 0:
  t.left(b)
  t.forward(b * 3)
  b -= 1