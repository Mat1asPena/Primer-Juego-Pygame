import pygame
import sys
from funciones import cargar_y_redimensionar_imagen
from constantes import ANCHO_PANTALLA, ALTO_PANTALLA

def game_over_screen(screen, score):
    clock = pygame.time.Clock()
    running = True

    pygame.mixer.init()
    pygame.mixer_music.load(f"assets/musica/game_over_music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer_music.play(-1)

    background_game_over = cargar_y_redimensionar_imagen(f"assets/backgrounds/menu_principal/game_over_background.jpg", ANCHO_PANTALLA, ALTO_PANTALLA)

    # Guardar el puntaje en el archivo
    nombre = input("Ingrese su nombre: ")
    with open('scores.csv', 'a') as file:
        file.write(f'{nombre},{score}\n')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                running = False
                from main import main_menu
                main_menu()

        screen.blit(background_game_over, [0,0])
        font = pygame.font.Font(None, 74)
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        prompt_text = font.render('Precione Enter', True, (0, 0, 0))
        screen.blit(score_text, (screen.get_width() // 2 - score_text.get_width() // 2, 300))
        screen.blit(prompt_text, (screen.get_width() // 2 - prompt_text.get_width() // 2, 350))

        pygame.display.flip()
        clock.tick(60)