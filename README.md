# tarea
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
