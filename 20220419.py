# 作者:王嘉良
# 乒乓球遊戲

import turtle
import winsound 

win = turtle.Screen()
win.title("Pong by JiaLiang")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#初始化分數
score_a=0
score_b=0


# 左球板
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5,stretch_len=1)

# 右球板
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)

#球
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx=0.08
Ball.dy=0.08

#功能
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
#輸入功能
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down,"Down")

#計分系統
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player A: 0 Player B: 0", align="center", font =("Courier",24,"normal"))


#畫面更新
while True:
    win.update()

    #移動球
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #邊界
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy*=-1
        winsound.PlaySound("PONG 1.wav",winsound.SND_ASYNC)
    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy*=-1
        winsound.PlaySound("PONG 1.wav",winsound.SND_ASYNC) 

    if Ball.xcor() > 390:
        Ball.goto(0,0)
        Ball.dx*=-1
        score_a +=1
        score.clear()
        score.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font =("Courier",24,"normal"))

    if Ball.xcor() < - 390:
        Ball.goto(0,0)
        Ball.dx*=-1
        score_b +=1
        score.clear()
        score.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font =("Courier",24,"normal"))

    #球反彈
    if (Ball.xcor() > 340 and Ball.xcor() < 350 ) and (Ball.ycor() < paddle_b.ycor() + 40 and Ball.ycor() > paddle_b.ycor() -40 ):
        Ball.setx(340)
        Ball.dx*= -1
        winsound.PlaySound("PONG 1.wav",winsound.SND_ASYNC)
    if (Ball.xcor() < -340 and Ball.xcor() > -350 ) and (Ball.ycor() < paddle_a.ycor() + 40 and Ball.ycor() > paddle_a.ycor() -40 ):
        Ball.setx(-340)
        Ball.dx*= -1
        winsound.PlaySound("PONG 1.wav",winsound.SND_ASYNC)
    

    
    
   