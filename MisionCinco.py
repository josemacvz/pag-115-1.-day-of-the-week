#Autor: JOSE LUIS MACIAS VAZQUEZ. GRUPO 03
#Dibuja cuadros y circulos.

#Falta que el ciclo ponga las lineas x decrecientes hasta la mitad y después crecientes hasta el final y lo mismo para las líneas y.


import pygame

ANCHO = 800
ALTO = 800

NEGRO = (0,0,0)
BLANCO = (255,255,255)

def dibujarLineas(ventana):
    for y in range (0, ALTO, 10):
        pygame.draw.line(ventana, NEGRO,(0 ,y),(ANCHO, y))


    for x in range (0, ANCHO, 10):
        pygame.draw.line(ventana, NEGRO, (x, 0), (x, ALTO))


def dibujarCirculos(ventana):

    for radio in range (10, ALTO-390, 10):
        pygame.draw.circle(ventana, NEGRO, (ANCHO//2, ALTO//2), radio, 1)



def dibujarCuadrosCirculos():

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))

    reloj = pygame.time.Clock()

    termina = False

    while not termina:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                termina = True

        ventana.fill(BLANCO)

        dibujarLineas(ventana)
        dibujarCirculos(ventana)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def main():

    dibujarCuadrosCirculos()


main()

"""import random

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)# nada de rojo, ni verde, solo azul
NEGRO=(0,0,0)

# Estructura básica de un programa que usa pygame para dibujar
def generarColor():
    rojo=random.randint(0,255)
    verde=random.randint(0,255)
    azul=random.randint(0,255)

    return (rojo,verde,azul)


def dibujarLineasEstrellas(ventana):
    for y in range(0,ALTO, 10):
        xFinal=y+10
        colorAleatorio=generarColor()
        pygame.draw.line(ventana,colorAleatorio,(0,y),(xFinal,ALTO))




def dibujarEstrella():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        dibujarLineasEstrellas(ventana)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame




def dibujar(radio,x,y):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
       #dubujar circulo con toda la informacion
        pygame.draw.circle(ventana, ROJO, (x, y), radio)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    #radio=int(input("Radio: "))
    #while radio>0:
       # x= int(input("x: "))
        #y= int(input("y: "))
        #dibujar(radio,x,y)# Por ahora, solo dibuja
        #radio=int(input("Radio: "))
    dibujarEstrella()




# Llamas a la función principal
main()"""