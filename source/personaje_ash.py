import pygame
from funciones import cargar_y_redimensionar_imagen
from sprite_groups import *
from pokeball_disparada import Pokeball_disparada
from constantes import *

class PersonajeAsh(pygame.sprite.Sprite):
    def __init__(self, x, y, animaciones):
        super().__init__()
        self.animaciones = animaciones
        self.estado = "quieto"
        self.frame_i = 0
        self.update_time = pygame.time.get_ticks()

        self.cooldown_time = 1000  # Tiempo de cooldown en milisegundos (1 segundo)
        self.ultimo_lanzamiento = pygame.time.get_ticks() - self.cooldown_time  # Iniciar con el cooldown cumplido

        self.direccion = "derecha"  # Dirección inicial del personaje
        self.pokeballs = 0  # Inicialmente no tiene Pokeballs

        self.vidas = 3
        self.tiempo_inmunidad = 0
        self.inmune = False

        self.image = self.animaciones[self.estado][self.frame_i]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def movimiento(self, velocidad_x, velocidad_y):
        if velocidad_y < 0:
            self.estado = "movimiento_arriba"
        elif velocidad_y > 0:
            self.estado = "movimiento_abajo"
        elif velocidad_x != 0:
            self.estado = "movimiento_costados"
            self.direccion = "derecha" if velocidad_x > 0 else "izquierda"
        else:
            self.estado = "quieto"

        # Verificar límites de la pantalla en y
        if self.rect.top < 0:  # Si el personaje se sale por arriba
            self.rect.top = 0
        elif self.rect.bottom > 500:  # Si el personaje se sale por abajo
            self.rect.bottom = 500

        # Verificar límite en x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 600:  # Límite en coordenada_x 450
            self.rect.right = 600

        self.rect.x += velocidad_x
        self.rect.y += velocidad_y

    def disparar_funciona(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_lanzamiento >= self.cooldown_time and self.pokeballs > 0:
        #Solo disparar si ha pasado el cooldown y tiene Pokeballs disponibles
            pokeball = Pokeball_disparada(self.rect.centerx, self.rect.centery, "pokeball", 3)
            pokeball.update()
            self.ultimo_lanzamiento = tiempo_actual
            self.pokeballs -= 1

            return pokeball
        else:
            return None

    def update(self):
        tiempo_entre_animaciones = 100
        if pygame.time.get_ticks() - self.update_time >= tiempo_entre_animaciones:
            self.frame_i += 1
            self.update_time = pygame.time.get_ticks()
            if self.frame_i >= len(self.animaciones[self.estado]):
                self.frame_i = 0  # Reinicio
        # validar índice
        if self.frame_i < len(self.animaciones[self.estado]):
            self.image = self.animaciones[self.estado][self.frame_i]

        if self.estado == "movimiento_costados" and self.direccion == "izquierda":
            self.image = pygame.transform.flip(self.image, True, False)