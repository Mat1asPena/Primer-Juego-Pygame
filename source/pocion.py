import pygame
import random
from funciones import cargar_y_redimensionar_imagen
from sprite_groups import todas_pociones
from constantes import ANCHO_PANTALLA

class Pocion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = cargar_y_redimensionar_imagen("assets/pocion/pocion.png", 30, 30)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO_PANTALLA
        self.rect.y = random.randint(30,450)  # Ajuste para que aparezca arriba
        self.velocidad_x = -1  # Velocidad a la que se mueve la poción

    def update(self):
        self.rect.x += self.velocidad_x
        if self.rect.right < 0:
            self.kill()