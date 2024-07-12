import pygame
from colores import *
from random import randint, choice
from settings_juego_main import *

class Personaje():
    def __init__(self, x: int, y: int, animaciones: dict):
        if not isinstance(animaciones, dict):
            raise TypeError("esto no es un diccionario")
        self.flip = False

        self.animaciones = animaciones
        self.estado = "quieto"
        self.frame_i = 0
        self.update_time = pygame.time.get_ticks()

        self.imagen = self.animaciones[self.estado][self.frame_i]
        self.hitbox = pygame.Rect(0, 0, ANCHO_PERSONAJE, ALTO_PERSONAJE)
        self.hitbox.center = (x, y)

        self.vel_y = 0
        self.jump_speed = -13
        self.gravity = 1
        self.is_jumping = False

    def movimiento(self, velocidad_y):
        if velocidad_y < 0:
            self.estado = "correr_arriba"
        elif velocidad_y > 0:
            self.estado = "correr_abajo"
        else:
            self.estado = "quieto"
        self.hitbox.y += velocidad_y

        if self.hitbox.bottom > SCREEN_SIZE[1] - 50:
            self.hitbox.bottom = SCREEN_SIZE[1] - 50

    def update(self):
        tiempo_entre_animaciones = 100
        if pygame.time.get_ticks() - self.update_time >= tiempo_entre_animaciones:
            self.frame_i += 1
            self.update_time = pygame.time.get_ticks()
            if self.frame_i >= len(self.animaciones[self.estado]):
                self.frame_i = 0  # Reinicia a 0 
        if self.frame_i < len(self.animaciones[self.estado]):
            self.imagen = self.animaciones[self.estado][self.frame_i]

    def dibujar(self, ventana):
        if self.frame_i < len(self.animaciones[self.estado]):
            imagen_flip = pygame.transform.flip(self.animaciones[self.estado][self.frame_i], self.flip, False)
            ventana.blit(imagen_flip, self.hitbox)

class EnemigoUno(pygame.sprite.Sprite):
    def __init__(self):
        # Cargar las imágenes
        self.imagen_movimiento = pygame.image.load("assets/fantasma/enemigo_fantasma_movimiento (1).png").convert_alpha()
        self.imagen_quieto = pygame.image.load("assets/fantasma/enemigo_fantasma_quieto (0).png").convert_alpha()

        # Inicializar la imagen y el rectángulo del sprite
        self.image = self.imagen_quieto
        self.rect = self.image.get_rect()
        self.rect.center = (randint(550, 750), 240)

        # Parámetros de movimiento
        self.speed = 2
        self.direccion = self.direccion_random()

        # maneja la pausa
        self.quieto = False
        self.tiempo_quieto = 0

    def direccion_random(self):
        return choice(["izquierda", "derecha"])

    def update(self):
        if self.quieto:
            # Comprobar si han pasado 2 segundos
            if pygame.time.get_ticks() - self.tiempo_quieto >= 2000:
                self.quieto = False
                self.direccion = self.direccion_random()
            else:
                self.image = self.imagen_quieto
        else:
            self.image = self.imagen_movimiento

            # Mover el enemigo
            if self.direccion == "izquierda":
                self.rect.x -= self.speed
                self.image = pygame.transform.flip(self.imagen_movimiento, True, False)
            elif self.direccion == "derecha":
                self.rect.x += self.speed
                self.image = self.imagen_movimiento

            if self.rect.left <= 0:
                self.quieto = True
                self.tiempo_quieto = pygame.time.get_ticks()
                self.rect.left = 0
            elif self.rect.right >= ANCHO:
                self.direccion = self.direccion_random()
                self.rect.right = ANCHO - self.rect.width

# class EnemigoDos(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         # Cargar las imágenes
#         self.imagen_movimiento = pygame.image.load("assets/fantasma/enemigo_fantasma_movimiento (1).png").convert_alpha()
#         self.imagen_quieto = pygame.image.load("assets/fantasma/enemigo_fantasma_quieto (0).png").convert_alpha()
        
#         # Inicializar la imagen y el rectángulo del sprite
#         self.image = self.imagen_quieto
#         self.rect = self.image.get_rect()
#         self.rect.center = (randint(550, 750), 240)
        
#         # Parámetros de movimiento
#         self.speed = 5
#         self.direccion = self.direccion_random()
    
#     def direccion_random(self):
#         return choice(["izquierda", "derecha"])

#     def update(self):
#         # Asignar la imagen de movimiento
#         self.image = self.imagen_movimiento
        
#         # Mover el enemigo
#         if self.direccion == "izquierda":
#             self.rect.x -= self.speed
#             self.image = pygame.transform.flip(self.imagen_movimiento, True, False)
#         elif self.direccion == "derecha":
#             self.rect.x += self.speed
#             self.image = self.imagen_movimiento

#         # Cambio de dirección si se sale de los límites
#         if self.rect.left < 0:
#             self.direccion = self.direccion_random()
#             self.rect.left = 0
#         elif self.rect.right > ANCHO:
#             self.direccion = self.direccion_random()
#             self.rect.right = ANCHO - ANCHO_PERSONAJE

# class EnemigoTres(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         # Cargar las imágenes
#         self.imagen_movimiento = pygame.image.load("assets/fantasma/enemigo_fantasma_movimiento (1).png").convert_alpha()
#         self.imagen_quieto = pygame.image.load("assets/fantasma/enemigo_fantasma_quieto (0).png").convert_alpha()
        
#         # Inicializar la imagen y el rectángulo del sprite
#         self.image = self.imagen_quieto
#         self.rect = self.image.get_rect()
#         self.rect.center = (randint(550, 750), 240)
        
#         # Parámetros de movimiento
#         self.speed = 5
#         self.direccion = self.direccion_random()
    
#     def direccion_random(self):
#         return choice(["izquierda", "derecha"])

#     def update(self):
#         # Asignar la imagen de movimiento
#         self.image = self.imagen_movimiento
        
#         # Mover el enemigo
#         if self.direccion == "izquierda":
#             self.rect.x -= self.speed
#             self.image = pygame.transform.flip(self.imagen_movimiento, True, False)
#         elif self.direccion == "derecha":
#             self.rect.x += self.speed
#             self.image = self.imagen_movimiento

#         # Cambio de dirección si se sale de los límites
#         if self.rect.left < 0:
#             self.direccion = self.direccion_random()
#             self.rect.left = 0
#         elif self.rect.right > ANCHO:
#             self.direccion = self.direccion_random()
#             self.rect.right = ANCHO - ANCHO_PERSONAJE

# class EnemigoCuatro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Cargar las imágenes
        self.imagen_movimiento = pygame.image.load("assets/fantasma/enemigo_fantasma_movimiento (1).png").convert_alpha()
        self.imagen_quieto = pygame.image.load("assets/fantasma/enemigo_fantasma_quieto (0).png").convert_alpha()
        
        # Inicializar la imagen y el rectángulo del sprite
        self.image = self.imagen_quieto
        self.rect = self.image.get_rect()
        self.rect.center = (randint(550, 750), 240)
        
        # Parámetros de movimiento
        self.speed = 5
        self.direccion = self.direccion_random()
    
    def direccion_random(self):
        return choice(["izquierda", "derecha"])

    def update(self):
        # Asignar la imagen de movimiento
        self.image = self.imagen_movimiento
        
        # Mover el enemigo
        if self.direccion == "izquierda":
            self.rect.x -= self.speed
            self.image = pygame.transform.flip(self.imagen_movimiento, True, False)
        elif self.direccion == "derecha":
            self.rect.x += self.speed
            self.image = self.imagen_movimiento

        # Cambio de dirección si se sale de los límites
        if self.rect.left < 0:
            self.direccion = self.direccion_random()
            self.rect.left = 0
        elif self.rect.right > ANCHO:
            self.direccion = self.direccion_random()
            self.rect.right = ANCHO - ANCHO_PERSONAJE