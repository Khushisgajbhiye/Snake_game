import  turtle
import time
import random

delay = 0.2
score = 0
highestscore =0

bodies = []

a =turtle.Screen()
a.title("SNAKE-GAME")
a.bgcolor("black")
a.setup(width=600,height=600)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.fillcolor("purple")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("white")
food.penup()
food.ht()
food.goto(0,200)
food.st()

sb = turtle.Turtle()
sb.shape("square")
sb.color("white")
sb.fillcolor("white")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score:0   |  Heightest Score: 0")

def moveup() :
    if head.direction!="down" :
        head.direction = "up"
def movedown() :       
    if head.direction!="up" :
        head.direction = "down"
def moveleft() :       
    if head.direction!="right" :
        head.direction = "left"
def moveright() :       
    if head.direction!="left" :
        head.direction = "right"
        
def movestop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y= head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y= head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x= head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x= head.xcor()
        head.setx(x+20)
        
a.listen()
a.onkey(moveup, "Up")
a.onkey(movedown, "Down")
a.onkey(moveleft, "Left")
a.onkey(moveright, "Right")
a.onkey(movestop, "space")

while True:
    a.update()
    
    
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)

    if head.distance(food)<20:
        x = random.randint(-290,290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        
        body =turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("purple")
        body.fillcolor("white")
        bodies.append(body)
        
        score+=10
        
        delay-= 0.001
        
        if score> highestscore:
            highestscore= score
            
        sb.clear()
        sb.write("Score:{} Highest score: {}" .format(score,highestscore))
        
    for index in range(len(bodies)-1,0,-1):
        x = bodies[index-1].xcor()
        y = bodies[index-1].ycor()
        bodies[index].goto(x,y)
        
    if len(bodies)>0:
        x= head.xcor()
        y= head.ycor()
        bodies[0].goto(x,y)
        
    move()
    
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            
            for body in bodies:
                body.ht()
            bodies.clear()
            
            score = 0
            delay = 0.1
            
            sb.clear()
            sb.write("Score:{} Highest score: {}" .format(score,highestscore))
    time.sleep(0)
    
a.mainloop()
