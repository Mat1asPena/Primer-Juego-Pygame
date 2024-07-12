import pygame
import sys
from funciones import *
from constantes import *

background = cargar_y_redimensionar_imagen (f"assets/backgrounds/menu_principal/background_menu.jpg",ANCHO_PANTALLA, ALTO_PANTALLA)

def config_menu(screen):
    
    pygame.mixer.init()
    pygame.mixer_music.load(f"assets/musica/figa_de_guine.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer_music.play(-1)
    
    reloj = pygame.time.Clock()
    running = True
    screen.blit(background, [0, 0])
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Dibujar elementos de configuración aquí
        screen.fill((255, 255, 255))

        pygame.display.flip()
        reloj.tick(60)