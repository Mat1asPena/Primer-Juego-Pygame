import pygame, sys, random
from source.juego_viejo.settings import *
from source.juego_viejo.colores import *
from source.juego_viejo.funciones_juego_plataforma import *

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_SIZE))
pygame.display.set_caption("test Juego")

en_ejecucion = True

ABAJO_DERECHA = 3 # +x +y
ABAJO_IZQUIERDA = 9 #-x +y
ARRIBA_DERECHA = 1 # -x +y
ARRIBA_IZQUIERDA = 7 # 

speed = 3

gravedad = True
gravedad_x = True

bloque = {"rectangulo": pygame.Rect(350, 250, 80, 80),"color": color_random(), "direccion": ABAJO_DERECHA}

#bloque = pygame.draw.rect(SCREEN, VERDE_LIMA, (350, 250, 80, 80))

while en_ejecucion:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_ejecucion = False
    SCREEN.fill(NEGRO)

    if bloque["rectangulo"].right >= ANCHO:
        if  bloque["direccion"] == ABAJO_DERECHA:
            bloque["direccion"] = ABAJO_IZQUIERDA
            bloque["color"] = color_random()
        else:
            bloque["direccion"] = ARRIBA_IZQUIERDA
            bloque["color"] = color_random()
    elif bloque["rectangulo"].left <= 0:
        if bloque["direccion"] == ABAJO_IZQUIERDA:
            bloque["direccion"] = ABAJO_DERECHA
            bloque["color"] = color_random()
        else:
            bloque["direccion"] = ARRIBA_DERECHA
            bloque["color"] = color_random()
    elif bloque["rectangulo"].top <= 0:
        if  bloque["direccion"] == ARRIBA_DERECHA:
            bloque["direccion"] = ABAJO_DERECHA
            bloque["color"] = color_random()
        else: 
            bloque["direccion"] = ABAJO_IZQUIERDA
            bloque["color"] = color_random()
    elif bloque["rectangulo"].bottom >= ALTO:
        if  bloque["direccion"] == ABAJO_DERECHA:
            bloque["direccion"] = ARRIBA_DERECHA
            bloque["color"] = color_random()
        else:
            bloque["direccion"] =  ARRIBA_IZQUIERDA
            bloque["color"] = color_random()

    if bloque["direccion"] == ABAJO_DERECHA:
        bloque["rectangulo"].x += speed
        bloque["rectangulo"].y += speed
    elif bloque["direccion"] == ABAJO_IZQUIERDA:
        bloque["rectangulo"].x -= speed
        bloque["rectangulo"].y += speed
    elif bloque["direccion"] == ARRIBA_DERECHA:
        bloque["rectangulo"].x += speed
        bloque["rectangulo"].y -= speed
    elif bloque["direccion"] == ARRIBA_IZQUIERDA:
        bloque["rectangulo"].x -= speed
        bloque["rectangulo"].y -= speed

    pygame.draw.rect(SCREEN, bloque["color"], bloque["rectangulo"])

    reloj.tick(60)
    pygame.display.flip()

pygame.quit()