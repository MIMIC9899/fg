import turtle
import winsound

wn = turtle.Screen()
wn.title("POONG")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(2) #speed?

#Score
sA=0
sB=0

#Paddle A
pA = turtle.Turtle()
pA.speed(0)
pA.shape("square")
pA.color('white')
pA.shapesize(stretch_wid=5, stretch_len=1)
pA.penup()
pA.goto(-350, 0)

#Paddle B
pB = turtle.Turtle()
pB.speed(0)
pB.shape("square")
pB.color('white')
pB.shapesize(stretch_wid=5, stretch_len=1)
pB.penup()
pB.goto(350, 0)

#Ball
B = turtle.Turtle()
B.speed(0)
B.shape("square")
B.color('white') 
B.penup()
B.goto(0, 0)
B.dx = 2
B.dy = 2

#Pen
P= turtle.Turtle()
P.speed(0)
P.color('white')
P.penup()
P.hideturtle()
P.goto(0,260)
P.write("Player A: 0  Player B: 0", align='center', font=('Courier', 24, 'normal'))

#Func
def pAUp():
    y = pA.ycor()
    y+= 40
    pA.sety(y)

def pADown():
    y = pA.ycor()
    y-= 40
    pA.sety(y)

def pBUp():
    y = pB.ycor()
    y+= 40
    pB.sety(y)

def pBDown():
    y = pB.ycor()
    y-= 40
    pB.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(pAUp, 'w')
wn.onkeypress(pADown, 's')
wn.onkeypress(pBUp, 'Up')
wn.onkeypress(pBDown, 'Down')

#Main game
while True:
    wn.update()
    
    #Move the Ball
    B.setx(B.xcor() + B.dx)
    B.sety(B.ycor() + B.dy)
    
    #Border checking
    if B.ycor() >290:
        B.sety(290)
        B.dy *=-1
        winsound.PlaySound('C:\\vscode\\5g\\1g\\tolk.wav', winsound.SND_ASYNC)
    
    if B.ycor() < -290:
        B.sety(-290)
        B.dy *=-1
        winsound.PlaySound('C:\\vscode\\5g\\1g\\tolk.wav', winsound.SND_ASYNC)
        
    if B.xcor() >390:
        B.goto(0, 0)
        B.dx *=-1
        sA+=1
        P.clear()
        P.write(f"Player A: {sA}  Player B: {sB}", align='center', font=('Courier', 24, 'normal'))
    
    if B.xcor() < -390:
        B.goto(0,0)
        B.dx *=-1
        sB+=1
        P.clear()
        P.write(f"Player A: {sA}  Player B: {sB}", align='center', font=('Courier', 24, 'normal'))
    
    
    #Paddle and ball collisions
    if B.xcor() > 340 and B.xcor() < 350 and B.ycor() < pB.ycor() + 40 and B.ycor() > pB.ycor() -40:
        B.setx(340)
        B.dx*=-1
        winsound.PlaySound('C:\\vscode\\5g\\1g\\tolk.wav', winsound.SND_ASYNC)
        
    if B.xcor() < -340 and B.xcor() > -350 and B.ycor() < pA.ycor() + 40 and B.ycor() > pA.ycor() -40:
        B.setx(-340)
        B.dx*=-1
        winsound.PlaySound('C:\\vscode\\5g\\1g\\tolk.wav', winsound.SND_ASYNC)