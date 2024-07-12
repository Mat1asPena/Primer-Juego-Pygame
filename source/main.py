import pygame
import sys
from game import game_loop
from config import config_menu
from ranking import show_ranking
from game_over import game_over_screen
from funciones import *
from constantes import *

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Configurar la pantalla
screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Juego segundo parcial")
background = cargar_y_redimensionar_imagen(f"assets/backgrounds/menu_principal/background_menu_main.png", ANCHO_PANTALLA, ALTO_PANTALLA)

# Fuente
font = pygame.font.Font(None, 74)

def main_menu():
    pygame.mixer.init()
    pygame.mixer_music.load(f"assets/musica/figa_de_guine.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer_music.play(-1)

    while True:
        screen.blit(background, [0, 0])

        TITULO = font.render("Parcial 2", True, NEGRO)
        jugar_boton = font.render("Jugar", True, NEGRO)
        salir_boton = font.render("Salir", True, NEGRO)
        ranking_boton = font.render("Ranking", True, NEGRO)

        jugar_boton_rect = jugar_boton.get_rect(center=(ANCHO_PANTALLA // 2, 250))
        screen.blit(jugar_boton, jugar_boton_rect)

        ranking_boton_rect = ranking_boton.get_rect(center=(ANCHO_PANTALLA // 2, 350))
        screen.blit(ranking_boton, ranking_boton_rect)
        
        salir = salir_boton.get_rect(center=(ANCHO_PANTALLA // 2, 450))
        screen.blit(salir_boton, salir)

        TITULO_RECT = TITULO.get_rect(center=(ANCHO_PANTALLA // 2, 100))
        screen.blit(TITULO, TITULO_RECT)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if jugar_boton_rect.collidepoint(event.pos):
                    game_loop(screen)
                elif ranking_boton_rect.collidepoint(event.pos):
                    show_ranking(screen)
                elif salir.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    main_menu()
