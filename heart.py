n = int(input("Ënter the number of lines you want: "))  #greater than 50 for better results
import turtle as t
#t.forward(100)
t.left(90)
t.penup()
t.forward(50)
t.pendown()
t.speed(400*10)
t.hideturtle()
for i in range(n):
    t.color('violet')
    t.forward(i*3/7)
    t.color('indigo')
    t.forward(i*3/7)
    t.color('blue')
    t.forward(i*3/7)
    t.color('green')
    t.forward(i*3/7)
    t.color('yellow')
    t.forward(i*3/7)
    t.color('orange')
    t.forward(i*3/7)
    t.color('red')
    t.forward(i*3/7)
    t.penup()
    t.backward(i*3)
    t.pendown()
    t.right(180/n)

for i in range(n, 1, -1):
    t.color('violet')
    t.forward(i*3/7)
    t.color('indigo')
    t.forward(i*3/7)
    t.color('blue')
    t.forward(i*3/7)
    t.color('green')
    t.forward(i*3/7)
    t.color('yellow')
    t.forward(i*3/7)
    t.color('orange')
    t.forward(i*3/7)
    t.color('red')
    t.forward(i*3/7)
    t.penup()
    t.backward(i*3)
    t.pendown()
    t.right(180/n)


