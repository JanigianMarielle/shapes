import turtle
import random

tiny = turtle.Turtle()
tiny.pendown()
tiny.speed(10)

sideLength = random.randint(0, 100)
print("my random number is ", sideLength)
for i in range(4):
  tiny.forward(sideLength)
  tiny.right(90)

tiny.penup()
tiny.left(90)
tiny.forward(50)
tiny.pendown()

sideLength2 = random.randint(0, 100)
print("my 2nd random number is ", sideLength2)
for i in range(4):
  tiny.forward(sideLength2)
  tiny.right(90)

tiny.penup()
tiny.left(90)
tiny.forward(50)
tiny.pendown()

sideLength3 = random.randint(0, 100)
print("my 3rd random number is ", sideLength3)
for i in range(3):
  tiny.forward(sideLength3)
  tiny.right(120)

tiny.penup()
tiny.left(90)
tiny.forward(50)
tiny.pendown()

sideLength4 = random.randint(0, 100)
print("my 4th random number is ", sideLength4)
for i in range(3):
  tiny.forward(sideLength4)
  tiny.right(120)