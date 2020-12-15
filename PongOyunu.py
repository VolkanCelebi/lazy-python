import turtle
import winsound

#ekran
ekran = turtle.Screen()
ekran.setup(width=800, height=600)
ekran.bgcolor("blue")
ekran.title("Pong Oyunu")
ekran.tracer(0)

#panel A
panelA = turtle.Turtle()
panelA.speed(0)
panelA.shape("square")
panelA.color("white")
panelA.shapesize(stretch_wid=5, stretch_len=1)
panelA.penup()
panelA.goto(-350,0)
#panel B
panelB = turtle.Turtle()
panelB.speed(0)
panelB.shape("square")
panelB.color("white")
panelB.shapesize(stretch_wid=5, stretch_len=1)
panelB.penup()
panelB.goto(350,0)
#top
top = turtle.Turtle()
top.speed(0)
top.shape("square")
top.color("white")
top.penup()
top.goto(0,0)
top.dx = .2
top.dy = -.2

#tabela
tabela = turtle.Turtle()
tabela.speed(0)
tabela.color("white")
tabela.penup()
tabela.hideturtle()
tabela.goto(0,260)
tabela.write("Oyuncu A: 0 Oyuncu B: 0",align="center",
             font=("Courier",24,"normal"))
#skor
skorA = 0
skorB = 0
#olaylar
def panelAYukari():
    y = panelA.ycor()
    y += 20
    panelA.sety(y)
    if panelA.ycor() > 250:
        panelA.sety(250)
def panelAAsagi():
    y = panelA.ycor()
    y -= 20
    panelA.sety(y)
    if panelA.ycor() < -250:
        panelA.sety(-250)

def panelBYukari():
    y = panelB.ycor()
    y += 20
    panelB.sety(y)
    if panelB.ycor() > 250:
        panelB.sety(250)
def panelBAsagi():
    y = panelB.ycor()
    y -= 20
    panelB.sety(y)
    if panelB.ycor() < -250:
        panelB.sety(-250)


#klavye dinleme
ekran.listen()
ekran.onkeypress(panelAYukari,"w")
ekran.onkeypress(panelAAsagi,"s")
ekran.onkeypress(panelBYukari,"Up")
ekran.onkeypress(panelBAsagi,"Down")


#Ana döngü
while True:
    ekran.update()
    #top hareket
    top.setx(top.xcor() + top.dx)
    top.sety(top.ycor() + top.dy)
    #çerçeve kontrol
    if top.ycor() > 290:
        top.sety(290)
        top.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if top.ycor() < -290:
        top.sety(-290)
        top.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if top.xcor() > 390:
        top.goto(0,0)
        top.dx *= -1
        skorA +=1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        tabela.clear()
        tabela.write("Oyuncu A: {} Oyuncu B: {}".format(skorA,skorB),
                     align="center", font=("Courier",24,"normal"))

    if top.xcor() < -390:
        top.goto(0,0)
        top.dx *= -1
        skorB +=1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        tabela.clear()
        tabela.write("Oyuncu A: {} Oyuncu B: {}".format(skorA, skorB),
                     align="center", font=("Courier", 24, "normal"))

    #panel - top karşılaşma
    if(top.xcor() <-340 and top.xcor() >-350
            and (top.ycor() < panelA.ycor() + 40 )
                 and top.ycor() > panelA.ycor() -40 ):
        top.dx *= -1
        top.setx(-340)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (top.xcor() > 340 and top.xcor() < 350 and (
            top.ycor() < panelB.ycor() + 40
            and
            top.ycor() >
            panelB.ycor() - 40)):
        top.dx *= -1
        top.setx(340)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)