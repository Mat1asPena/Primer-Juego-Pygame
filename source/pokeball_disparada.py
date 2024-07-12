import pygame
from constantes import *
from funciones import cargar_y_redimensionar_imagen
from sprite_groups import *

class Pokeball_disparada(pygame.sprite.Sprite):
    def __init__(self, x, y, type:str, projectile_speed):
        super().__init__()
        if type == "pokeball":
            self.image = cargar_y_redimensionar_imagen(f"assets/pokeballs/pokeball.png", 20, 20)
        elif type == "superball":
            self.image = cargar_y_redimensionar_imagen(f"assets/pokeballs/superball.png", 20, 20)
        elif type == "ultraball":
            self.image = cargar_y_redimensionar_imagen(f"assets/pokeballs/ultraball.png", 20, 20)
        self.x = x
        self.y = y
        self.rect= self.image.get_rect()
        self.rect.centerx= x
        self.rect.centery= y
        self.type = type
        self.projectile_speed= projectile_speed

    def update(self):
        self.rect.x += self.projectile_speed
        todos_los_sprites.add(self)
        if self.rect.left > 1000:
            self.kill()