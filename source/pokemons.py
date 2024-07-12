import pygame
import random
from funciones import cargar_y_redimensionar_imagen
from sprite_groups import *
from constantes import *

class Pokemones(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        rutas_imagenes = [
            f"assets/pokemones/ghost/gastly.png",
            f"assets/pokemones/ghost/hunter.png",
            f"assets/pokemones/ghost/gengar.png",
            f"assets/pokemones/charmander/charmander.png",
            f"assets/pokemones/charmander/charmeleon.png",
            f"assets/pokemones/charmander/charizard.png",
            f"assets/pokemones/bulbasaur/venasaur.png",
            f"assets/pokemones/bulbasaur/ivisaur.png",
            f"assets/pokemones/bulbasaur/bulbasaur.png",
            f"assets/pokemones/dragon/dragonite.png",
            f"assets/pokemones/dragon/dratini.png",
            f"assets/pokemones/dragon/dragonair.png",
            f"assets/pokemones/kadabra/abra.png",
            f"assets/pokemones/kadabra/kadabra.png",
            f"assets/pokemones/kadabra/alakazam.png",
            f"assets/pokemones/squartle/squartle.png",
            f"assets/pokemones/squartle/wartortle.png",
            f"assets/pokemones/squartle/blastoise.png"
        ]
        ruta_imagen = random.choice(rutas_imagenes)
        self.image = cargar_y_redimensionar_imagen(ruta_imagen, 50, 50)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad_x = random.choice([-2, -1, 1]) 
        self.velocidad_y = random.choice([-2, -1, 1])

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # Rebotar en los bordes de la pantalla
        if self.rect.left < 850 or self.rect.right > 1000:
            self.velocidad_x = -self.velocidad_x
        if self.rect.top < 0 or self.rect.bottom > 500:
            self.velocidad_y = -self.velocidad_y