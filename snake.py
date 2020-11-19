import turtle
import time
import random

POSPONER = 0.1

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

    if serpiente.distance(comida) < 20:
        x = random.randint(-680,680)
        y = random.randint(-680,680)
        comida.goto(x,y)
    
    movimiento()

    time.sleep(POSPONER)