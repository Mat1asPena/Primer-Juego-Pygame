import pygame
import random
from constantes import ALTO_PANTALLA
from funciones import cargar_y_redimensionar_imagen

class AtaqueCielo(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = self.cargar_imagen_aleatoria()
        self.rect = self.image.get_rect(center=(x, 0))
        self.velocidad_y = random.randint(4, 8)

    def cargar_imagen_aleatoria(self):
        imagenes = [
            "assets/ataques_cielo_random/alma.png",
            "assets/ataques_cielo_random/fuego_violeta.png",
            "assets/ataques_cielo_random/hielo_ataque.png"
        ]
        return pygame.image.load(random.choice(imagenes))

    def generar_ataques(x):
        ataques = []
        for _ in range(5):
            nuevo_ataque = AtaqueCielo(x)
            ataques.append(nuevo_ataque)
        return ataques

    # def update(self):
    #     self.rect.y += self.velocidad_y
    #     if self.rect.top > ALTO_PANTALLA:
    #         self.rect.y = -self.rect.height
    #         self.rect.x = random.randint(0, 620)
    #         self.image = self.cargar_imagen_aleatoria()
    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.y > ALTO_PANTALLA:
            self.kill()


