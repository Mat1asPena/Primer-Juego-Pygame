import pygame
from funciones import cargar_y_redimensionar_imagen
from sprite_groups import *
from constantes import *

class Pokeball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = cargar_y_redimensionar_imagen("assets/pokeballs/pokeball.png", 20, 20)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y