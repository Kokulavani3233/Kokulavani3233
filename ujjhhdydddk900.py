import turtle as t
def rectangle(horizontal,vertical,color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1,3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
    
t.penup()
t.speed('normal')
t.bgcolor('Goldenrod')
    
#feet
t.goto(-100, -150)
rectangle(50,20,'blue')
t.goto(-30,-150)
rectangle(50,20,'blue')
    
#legs
t.goto(-25, -50)
rectangle(15,100,'yellow')
t.goto(-55,-50)
rectangle(-15,100,'yellow')

#body
t.goto(-90,100)
rectangle(100,150,'red')

#arms
t.goto(-150, 70)
rectangle(60,15,'yellow')
t.goto(-150,110)
rectangle(15,40,'blue')

#hands
t.goto(10, 70)
rectangle(60,15,'yellow')
t.goto(55,110)
rectangle(15,40,'blue')

#neck
t.goto(-50,120)
rectangle(15,20,'yellow')

#head
t.goto(-85,170)
rectangle(80,50,'red')

#eyes
t.goto(-63,160)
rectangle(40,15,'white')
t.goto(-60,160)
rectangle(8,8,'black')
t.goto(-35,160)
rectangle(8,8,'black')

#mouth
t.goto(-65,135)
t.right(0)
rectangle(40,10,'black')

t.hideturtle()
