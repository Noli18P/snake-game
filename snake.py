import turtle
import time
import random

POSPONER = 0.1
score = 0
high_score = 0

#Configuracion ventana
ventana = turtle.Screen()
ventana.title('Snake...')
ventana.bgcolor('black')
ventana.setup(700,700,0,0)
ventana.tracer(0)

#Serpiente
serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.shape('square')
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color('white')

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.penup()
comida.goto(0,100)
comida.color('blue')

#Cuerpo de la serpiente
cuerpo = []

#marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color('white')
marcador.penup()
marcador.hideturtle()
marcador.goto(0,300)
marcador.write('Score: 0     High Score: 0', align='center', font=('Courier', 24, 'normal'))

#Funciones
def up_mov():
    serpiente.direction = 'up'


def down_mov():
    serpiente.direction = 'down'


def left_mov():
    serpiente.direction = 'left'


def right_mov():
    serpiente.direction = 'right'


def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor()
        serpiente.sety(y + 20)

    if serpiente.direction == 'down':
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    
    if serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    
    if serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x - 20)

#Teclado
ventana.listen()
ventana.onkeypress(up_mov, 'Up')
ventana.onkeypress(down_mov, 'Down')
ventana.onkeypress(left_mov, 'Left')
ventana.onkeypress(right_mov, 'Right')

while True:
    ventana.update()

    #colisiones borde
    if serpiente.xcor() > 280 or serpiente.xcor() < -280 or serpiente.ycor() > 280 or serpiente.ycor() < -280:
        time.sleep(1)
        serpiente.goto(0,0)
        serpiente.direction = 'stop'

        for cuerpos in cuerpo:
            cuerpos.goto(1000,1000)

        cuerpo.clear()
        score = 0
        marcador.clear()
        marcador.write('Score: {}     High Score: {}'.format(score,high_score), align='center', font=('Courier', 24, 'normal'))

    #colisiones comida
    if serpiente.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        cuerpo_serpiente = turtle.Turtle()
        cuerpo_serpiente.speed(0)
        cuerpo_serpiente.shape('square')
        cuerpo_serpiente.penup()
        cuerpo_serpiente.color('green')
        cuerpo.append(cuerpo_serpiente)

        #Aumentar puntaje
        score += 10
        
        if score > high_score:
            high_score = score

        marcador.clear()
        marcador.write('Score: {}     High Score: {}'.format(score,high_score), align='center', font=('Courier', 24, 'normal'))

    total_cuerpo = len(cuerpo)
    for i in range(total_cuerpo -1, 0, -1):
        x = cuerpo[i - 1].xcor()
        y = cuerpo[i - 1].ycor()
        cuerpo[i].goto(x,y)
    
    if total_cuerpo > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)

    movimiento()

    time.sleep(POSPONER)