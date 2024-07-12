import pygame, sys, random
from settings import *
from colores import *
from funciones_juego_plataforma import *

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_SIZE))
pygame.display.set_caption("test Juego")
pygame.mouse.set_visible(1)
background = pygame.image.load("background_bosque_juego.jpg").convert() #.convert() facilita a pygame trabajar con imagenes

en_ejecucion = True
reloj = pygame.time.Clock()
time_clock = 60
# ANCHO JUGADOR
ANCHO_JUGADOR = 15
ALTO_JUGADOR = 90

#       Movilidad Jugadores
#   JUGADOR UNO
# coordenadas
coordenada_x_uno = 50
coordenada_y_uno = 255
# velocidad de movimiento
velocidad_y_uno = 0
#   JUGADOR DOS
# coordenadas
coordenada_x_dos = 750
coordenada_y_dos = 255
# velocidad de movimiento
velocidad_y_dos = 0

#    PELOTA
# coordenadas
coordenada_x_pelota = 400 
coordenada_y_pelota = 300
velocidad_x_pelota = 3
velocidad_y_pelota = 3

while en_ejecucion:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_ejecucion = False
                #eventos teclado
        #jugador 1
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    velocidad_y_dos = -3
                if event.key == pygame.K_DOWN:
                    velocidad_y_dos = 3
        #jugador 2
                if event.key == pygame.K_w:
                    velocidad_y_uno = -3
                if event.key == pygame.K_s:
                    velocidad_y_uno = 3
        #jugador 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                velocidad_y_uno = 0
            if event.key == pygame.K_s:
                velocidad_y_uno = 0
        #jugador 2
            if event.key == pygame.K_UP:
                velocidad_y_dos = 0
            if event.key == pygame.K_DOWN:
                velocidad_y_dos = 0

    SCREEN.blit(background, [0, 0])
    
    if coordenada_y_pelota > 590 or coordenada_y_pelota < 10:
        velocidad_y_pelota *= -1

    if coordenada_x_pelota > 800 or coordenada_x_pelota < 0:
        velocidad_x_pelota *= -1
        velocidad_y_pelota *= -1
        coordenada_x_pelota = 400
        coordenada_y_pelota = 300

    #movimiento
    coordenada_y_uno += velocidad_y_uno

    coordenada_y_dos += velocidad_y_dos

    coordenada_x_pelota+= velocidad_x_pelota
    coordenada_y_pelota+= velocidad_y_pelota
    #jugadores
    jugador_uno = pygame.draw.rect(SCREEN, ROJO, ( coordenada_x_uno, coordenada_y_uno , ANCHO_JUGADOR, ALTO_JUGADOR))
    jugador_dos = pygame.draw.rect(SCREEN, AZUL, ( coordenada_x_dos, coordenada_y_dos , ANCHO_JUGADOR, ALTO_JUGADOR))
    #pelota
    pelota = pygame.draw.circle(SCREEN, BLANCO, (coordenada_x_pelota, coordenada_y_pelota), 10)

    #colisiones 
    if pelota.colliderect(jugador_uno) or pelota.colliderect(jugador_dos):
        velocidad_x_pelota *= -1
        time_clock += 2
    if time_clock == 80:
        velocidad_y_uno +=3
        velocidad_y_dos +=3

    reloj.tick(time_clock)
    pygame.display.flip()
pygame.quit()