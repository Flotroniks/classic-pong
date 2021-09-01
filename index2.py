import turtle
import winsound

#speed
speed= 0.3
paddle_speed = 25

#score
score_a=0
score_b=0

windows = turtle.Screen()
windows.title("Pong by flotroniks")
windows.bgcolor("black")
windows.setup(width=800, height=600)
windows.tracer(0)



paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


field = turtle.Turtle() 
field.speed(0)
field.shape("square")
field.color("white")
field.shapesize(stretch_wid=0.001, stretch_len=0.001)
field.penup()
field.goto(-400, 300)
field.pendown()
field.goto(400, 300)
field.goto(400, -300)
field.goto(-400, -300)
field.goto(-400, 300)
field.penup()
field.pendown()
field.goto(0, 300)
field.goto(0, -300)
field.penup()
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = speed
ball.dy = -speed

# Pen score

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0 ", align="center", font=("Courier", 24 ,"normal")  )

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += paddle_speed
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= paddle_speed
    paddle_a.sety(y)    

def paddle_b_up():
    y = paddle_b.ycor()
    y += paddle_speed
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= paddle_speed
    paddle_b.sety(y) 
         
#main game loop

windows.listen()
windows.onkeypress(paddle_a_up, "z")
windows.onkeypress(paddle_a_down, "s")
windows.onkeypress(paddle_b_up, "Up")
windows.onkeypress(paddle_b_down, "Down")



while True:
    windows.update()
    speed= 0.3

    #move the ball
    ball.setx(ball.xcor() + ball.dx) 
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("boop.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx*= -1
        score_a += 1
        pen.clear()   
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24 ,"normal")  )


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx*= -1 
        score_b += 1 
        pen.clear()
        pen.write("Player A: {} Player B: {} ".format(score_a, score_b), align="center", font=("Courier", 24 ,"normal")  )


    #padlle and balls colisition
    if (ball.xcor()> 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 ):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 ):
        ball.setx(-340)
        ball.dx *= -1        
        
           