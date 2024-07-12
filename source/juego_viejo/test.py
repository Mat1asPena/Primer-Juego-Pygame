import pygame
from source.juego_viejo.settings_juego_main import *
from source.juego_viejo.colores import *
from source.juego_viejo.funciones_juego_plataforma import *
from pj_test import *

pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_SIZE))
pygame.display.set_caption("test Juego")
pygame.mouse.set_visible(0)  # 0 no se ve el mouse | 1 se ve el mouse #
imagen_fondo = pygame.image.load("background_bosque_juego.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, SCREEN_SIZE)

en_ejecucion = True
reloj = pygame.time.Clock()

# Coordenadas
coordenada_x = 30
coordenada_y = 210

velocidad_x = 0
velocidad_y = 0

# Diccionario de animaciones del personaje principal
animaciones = {
    'agachado': [
        pygame.image.load(f"sprites_personaje_principal/agachado/agachado.png").convert_alpha()
    ],
    'correr': [
        pygame.image.load(f"sprites_personaje_principal/correr/correr (1).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/correr/correr (2).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/correr/correr (3).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/correr/correr (4).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/correr/correr (5).png").convert_alpha()
    ],
    'golpe_kunai': [
        pygame.image.load(f"sprites_personaje_principal/golpe kunai/golpe kunai (1).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/golpe kunai/golpe kunai (2).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/golpe kunai/golpe kunai (3).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/golpe kunai/golpe kunai (4).png").convert_alpha()
    ],
    'muerte': [
        pygame.image.load(f"sprites_personaje_principal/muerte/muerte (1).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/muerte/muerte (2).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/muerte/muerte (3).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/muerte/muerte (4).png").convert_alpha()
    ],
    'primer_golpe': [
        pygame.image.load(f"sprites_personaje_principal/primer_golpe/primer_golpe (1).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/primer_golpe/primer_golpe (2).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/primer_golpe/primer_golpe (3).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/primer_golpe/primer_golpe (4).png").convert_alpha()
    ],
    'quieto': [
        pygame.image.load(f"sprites_personaje_principal/quieto/quieto (1).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/quieto/quieto (2).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/quieto/quieto (3).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/quieto/quieto (4).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/quieto/quieto (5).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/quieto/quieto (6).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/quieto/quieto (7).png").convert_alpha()
    ],
    'recibir_danio': [
        pygame.image.load(f"sprites_personaje_principal/recibir_danio/recibir_danio (1).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/recibir_danio/recibir_danio (2).png").convert_alpha()
    ],
    'salto': [
        pygame.image.load(f"sprites_personaje_principal/salto/salto (1).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/salto/salto (2).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/salto/salto (3).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/salto/salto (4).png").convert_alpha()
    ],
    'segundo_golpe': [
        pygame.image.load(f"sprites_personaje_principal/segundo_golpe/segundo_golpe (1).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/segundo_golpe/segundo_golpe (2).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/segundo_golpe/segundo_golpe (3).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/segundo_golpe/segundo_golpe (4).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/segundo_golpe/segundo_golpe (5).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/segundo_golpe/segundo_golpe (6).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/segundo_golpe/segundo_golpe (7).png").convert_alpha()
    ],
    'tercer_golpe': [
        pygame.image.load(f"sprites_personaje_principal/tercer_golpe/tercer_golpe (1).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/tercer_golpe/tercer_golpe (2).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/tercer_golpe/tercer_golpe (3).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/tercer_golpe/tercer_golpe (4).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/tercer_golpe/tercer_golpe (5).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/tercer_golpe/tercer_golpe (6).png").convert_alpha(),
        pygame.image.load(f"sprites_personaje_principal/tercer_golpe/tercer_golpe (7).png").convert_alpha()
    ]
}

jugador = Personaje(coordenada_x, coordenada_y, animaciones['correr'])

mover_izquierda = False
mover_derecha = False
agacharse = False
saltar = False

while en_ejecucion:
    if mover_izquierda:
        velocidad_x = -3
    if mover_derecha:
        velocidad_x = 3
    if saltar:
        jugador.jump()
        jugador.animacion = animaciones['salto']  # Cambiar la animación a salto
    elif agacharse:
        jugador.crouch()
        jugador.animacion = animaciones['agachado']  # Cambiar la animación a agachado
    else:
        jugador.uncrouch()
        jugador.animacion = animaciones['correr']  # Por ejemplo, cambiar la animación a correr si no se agacha ni salta

    jugador.movimiento(velocidad_x, velocidad_y)
    jugador.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_ejecucion = False
        # Eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mover_izquierda = True
            if event.key == pygame.K_RIGHT:
                mover_derecha = True
            if event.key == pygame.K_UP:
                saltar = True
            if event.key == pygame.K_DOWN:
                agacharse = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                mover_izquierda = False
                velocidad_x = 0
            if event.key == pygame.K_RIGHT:
                mover_derecha = False
                velocidad_x = 0
            if event.key == pygame.K_UP:
                saltar = False
                velocidad_y = 0
            if event.key == pygame.K_DOWN:
                agacharse = False
                velocidad_y = 0

    SCREEN.blit(imagen_fondo, [0, 0])
    jugador.dibujar(SCREEN)

    reloj.tick(60)
    pygame.display.update()

pygame.quit()
