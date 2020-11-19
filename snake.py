import turtle
import time

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
serpiente.direction = 'left'
serpiente.color('white')

#Funciones
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


while True:
    ventana.update()
    movimiento()

    time.sleep(POSPONER)