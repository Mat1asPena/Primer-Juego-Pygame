import pygame
import sys
from constantes import *
from funciones import *

def show_ranking(screen):
    clock = pygame.time.Clock()
    running = True

    background = cargar_y_redimensionar_imagen (f"assets/backgrounds/menu_principal/background_menu_ranking_v2.png",ANCHO_PANTALLA, ALTO_PANTALLA)

    pygame.mixer.init()
    pygame.mixer_music.load(f"assets/musica/figa_de_guine.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer_music.play(-1)

    # Leer los scores desde un archivo
    try:
        with open('scores.csv','r') as file:
            scores = [line.strip("\n").split(",") for line in file.readlines()]
    except FileNotFoundError:
        scores = []

    ordenar(scores)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.blit(background, [0, 0])

        font = pygame.font.Font(None, 36)
        y_offset = 100
        for score in scores:
            score_text = font.render(f'{score[0]}: {score[1]}', True, (0, 0, 0))
            screen.blit(score_text, (100, y_offset))
            y_offset += 40

        pygame.display.flip()
        clock.tick(60)