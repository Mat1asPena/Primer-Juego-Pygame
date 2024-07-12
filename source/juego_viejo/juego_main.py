import pygame
from settings_juego_main import *
from colores import *
from funciones_juego_plataforma import *
from personajes import *

pygame.init()

SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("test Juego")
pygame.mouse.set_visible(0)  # 0 no se ve el mouse | 1 se ve el mouse
imagen_fondo = pygame.image.load("background_bosque_juego.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, SCREEN_SIZE)

en_ejecucion = True
reloj = pygame.time.Clock()

# Coordenadas
coordenada_x = 30
coordenada_y = 220

# Lista acciones personaje principal
correr = [
    pygame.image.load(f"assets/sprites_personaje_principal/correr/correr (1).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/correr/correr (2).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/correr/correr (3).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/correr/correr (4).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/correr/correr (5).png").convert_alpha()
]

quieto = [
    pygame.image.load(f"assets/sprites_personaje_principal/quieto/quieto (1).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/quieto/quieto (2).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/quieto/quieto (3).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/quieto/quieto (4).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/quieto/quieto (5).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/quieto/quieto (6).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/quieto/quieto (7).png").convert_alpha()
]

salto = [
    pygame.image.load(f"assets/sprites_personaje_principal/salto/salto (1).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/salto/salto (2).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/salto/salto (3).png").convert_alpha(),
    pygame.image.load(f"assets/sprites_personaje_principal/salto/salto (4).png").convert_alpha()
]

# Diccionario de animaciones
animaciones = {
    "correr": correr,
    "quieto": quieto,
    "saltar": salto
}

jugador = Personaje(coordenada_x, coordenada_y, animaciones)
enemigo1 = EnemigoUno()

all_sprites = pygame.sprite.Group()
all_sprites.add(enemigo1)

mover_izquierda = False
mover_derecha = False
saltar = False

while en_ejecucion:
    velocidad_x = 0
    velocidad_y = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_ejecucion = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mover_izquierda = True
            if event.key == pygame.K_RIGHT:
                mover_derecha = True
            if event.key == pygame.K_UP:
                saltar = True
            if event.key == pygame.K_ESCAPE:
                pausa(pygame.K_ESCAPE)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mover_izquierda = False
            if event.key == pygame.K_RIGHT:
                mover_derecha = False
            if event.key == pygame.K_UP:
                saltar = False

    if mover_izquierda:
        velocidad_x = -3
    if mover_derecha:
        velocidad_x = 3
    if saltar and not jugador.is_jumping:
        jugador.is_jumping = True
        jugador.vel_y = jugador.jump_speed
    if jugador.is_jumping:
        jugador.vel_y += jugador.gravity
        velocidad_y = jugador.vel_y
        if jugador.hitbox.bottom >= SCREEN_SIZE[1] - 50:
            jugador.is_jumping = False
            jugador.vel_y = 0

    enemigo1.update()
    jugador.movimiento(velocidad_x, velocidad_y)
    jugador.update()

    SCREEN.blit(imagen_fondo, [0, 0])
    all_sprites.draw(SCREEN)
    jugador.dibujar(SCREEN)

    reloj.tick(60)
    pygame.display.flip()
pygame.quit()