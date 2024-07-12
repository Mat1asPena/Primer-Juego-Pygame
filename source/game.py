import pygame
import sys
import random
from config import *
from constantes import *

from personaje_ash import PersonajeAsh
from pokeball import Pokeball
from pokemons import Pokemones
from ataques_aereos import AtaqueCielo
from pocion import Pocion

from funciones import *
from sprite_groups import *

def game_loop(screen):
    clock = pygame.time.Clock()
    running = True
    
    # Inicializar 
    score = 0
    pokeball_generations = 0
    pokemon_generations = 0

    tiempo_inicio = pygame.time.get_ticks()

    lista = []

    pygame.mixer.init()
    pygame.mixer.music.load("assets/musica/musica juego.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    flag_musica = True

    sonido_colision = pygame.mixer.Sound("assets/musica/pick_pokeball.mp3")
    sonido_colision.set_volume(0.5)  #                                                               VOLUMEN PICK_POKEBALL

    corazon = cargar_y_redimensionar_imagen("assets/vida/corazon.png", 30, 30)

    # Cargar y redimensionar animaciones
    quieto_masculino = [
        cargar_y_redimensionar_imagen("assets/personaje_masculino/quieto_masculino/quieto_masculino.png", 50, 45)
    ]
    movimiento_arriba_masculino = [
        cargar_y_redimensionar_imagen("assets/personaje_masculino/mirar_arriba_masculino/mirar_arriba_masculino (1).png", 50, 45),
        cargar_y_redimensionar_imagen("assets/personaje_masculino/mirar_arriba_masculino/mirar_arriba_masculino (2).png", 50, 45),
        cargar_y_redimensionar_imagen("assets/personaje_masculino/mirar_arriba_masculino/mirar_arriba_masculino (3).png", 50, 45)
    ]
    movimiento_abajo_masculino = [
        cargar_y_redimensionar_imagen("assets/personaje_masculino/mirar_abajo_masculino/mirar_abajo_masculino (1).png", 50, 45),
        cargar_y_redimensionar_imagen("assets/personaje_masculino/mirar_abajo_masculino/mirar_abajo_masculino (2).png", 50, 45),
        cargar_y_redimensionar_imagen("assets/personaje_masculino/mirar_abajo_masculino/mirar_abajo_masculino (3).png", 50, 45)
    ]
    movimiento_costados_masculino = [
        cargar_y_redimensionar_imagen("assets/personaje_masculino/caminar_costado_masculino/caminar_costado_masculino (1).png",50,45),
        cargar_y_redimensionar_imagen("assets/personaje_masculino/caminar_costado_masculino/caminar_costado_masculino (2).png",50,45),
        cargar_y_redimensionar_imagen("assets/personaje_masculino/caminar_costado_masculino/caminar_costado_masculino (3).png",50,45)
    ]
    animaciones_jugador_masculino = {
        "quieto": quieto_masculino,
        "movimiento_arriba": movimiento_arriba_masculino,
        "movimiento_abajo": movimiento_abajo_masculino,
        "movimiento_costados": movimiento_costados_masculino
    }

    personaje = PersonajeAsh(60, 300, animaciones_jugador_masculino)
    todos_los_sprites.add(personaje)

    background_juego = cargar_y_redimensionar_imagen("assets/backgrounds/juego/background_juego.png", 1000, 500)

#######################-EVENTOS-############################
    crear_pokeballs_event = pygame.USEREVENT + 1           #
    pygame.time.set_timer(crear_pokeballs_event, 5000)     #
#----------------------------------------------------------#
    crear_pokemones_event = pygame.USEREVENT + 2           #
    pygame.time.set_timer(crear_pokemones_event, 4000)     #
#----------------------------------------------------------#
    crear_ataques_cielo_event = pygame.USEREVENT + 3       #
    pygame.time.set_timer(crear_ataques_cielo_event, 3000) #
#----------------------------------------------------------#
    crear_pocion_event = pygame.USEREVENT + 4              #
    pygame.time.set_timer(crear_pocion_event, 10000)       #
############################################################

    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == crear_pokeballs_event and pokeball_generations < 5:
                for _ in range(5):
                    x = random.randint(20, 450) 
                    y = random.randint(20, 470) 
                    pokeball = Pokeball(x, y)
                    todas_pokeballs.add(pokeball)
                    todos_los_sprites.add(pokeball)
                pokeball_generations += 1
            if evento.type == crear_pokemones_event and pokemon_generations < 20:
                x = random.randint(860, 949)
                y = random.randint(51, 449)
                pokemon = Pokemones(x, y)
                pokemones.add(pokemon)
                todos_los_sprites.add(pokemon)
                pokemon_generations += 1
            if evento.type == crear_ataques_cielo_event:
                for _ in range(5):
                    x = random.randint(0, 620)
                    ataque_cielo = AtaqueCielo(x)
                    ataques_cielo.add(ataque_cielo)
                    todos_los_sprites.add(ataque_cielo)
            if evento.type == crear_pocion_event:
                pocion = Pocion()
                todas_pociones.add(pocion)
                todos_los_sprites.add(pocion)

        keys = pygame.key.get_pressed()
        velocidad_x, velocidad_y = 0, 0
        if keys[pygame.K_UP]:
            velocidad_y = -3
        elif keys[pygame.K_DOWN]:
            velocidad_y = 3
        if keys[pygame.K_LEFT]:
            velocidad_x = -3
        elif keys[pygame.K_RIGHT]:
            velocidad_x = 3
        elif keys[pygame.K_p]:
            pausa(pygame.K_p, screen)
        elif keys[pygame.K_m]:
            flag_musica = not flag_musica
            if flag_musica:
                pygame.mixer.music.set_volume(0.1)
            else:
                pygame.mixer.music.set_volume(0.0)
        if keys[pygame.K_SPACE]:
            pokeball_lanzada = personaje.disparar_funciona()
            if pokeball_lanzada:
                lista.append(pokeball_lanzada)
                todas_pokeballs_lanzadas.add(pokeball_lanzada)
                todos_los_sprites.add(pokeball_lanzada)

        personaje.movimiento(velocidad_x, velocidad_y)

        for pokeball in todas_pokeballs_lanzadas:
            pokeball.update()
            #pygame.draw.rect(screen, (0, 255, 0), pokeball.rect, 2)

        #               colisiones
        colisiones_pokeballs = pygame.sprite.spritecollide(personaje, todas_pokeballs, True)
        if colisiones_pokeballs:
            sonido_colision.play()
        for pokeball_lanzada in colisiones_pokeballs:
            personaje.pokeballs += 1

        colisiones = pygame.sprite.groupcollide(todas_pokeballs_lanzadas, pokemones, True, True)
        for pokeball, pokemon_list in colisiones.items():
            sonido_colision.play()
            score += 10
        
        # colisiones_ataques_cielo = pygame.sprite.spritecollide(personaje, ataques_cielo, True)
        # for ataque in colisiones_ataques_cielo:
        #     personaje.vidas -= 1
        #     #pygame.draw.circle(screen, (255, 0, 255), personaje.rect.center, 50, 3)
        #     personaje.inmune = True
        #     personaje.tiempo_inmunidad = pygame.time.get_ticks()
        # if personaje.inmune:
        #     tiempo_actual = pygame.time.get_ticks()
        #     if tiempo_actual - personaje.tiempo_inmunidad >= 500:
        #         personaje.inmune = False

        colisiones_pocion = pygame.sprite.spritecollide(personaje, todas_pociones, True)
        for curacion in colisiones_pocion:
            personaje.vidas +=1
            score += 5

        tiempo_actual = pygame.time.get_ticks()
        #loss
        if personaje.pokeballs <= 0 and len(pokemones) > 0 and tiempo_actual - tiempo_inicio > 20000:
            for sprite in todos_los_sprites:
                todos_los_sprites.remove(sprite)
            running = False

        if personaje.vidas == 0:
            for sprite in todos_los_sprites:
                todos_los_sprites.remove(sprite)
            running = False

        # Lógica del juego aquí
        screen.blit(background_juego, [0, 0])

        # Actualizar y dibujar todos los sprites
        todos_los_sprites.update()
        todos_los_sprites.draw(screen)

        for i in range(personaje.vidas):
            screen.blit(corazon, (10 + i * 40, 90))

        # # hitbox-----------------------------------------------------------#
        # # Dibujar las hitboxes
        # for pokemon in pokemones:
        #     pygame.draw.rect(screen, (255, 0, 0), pokemon.rect, 2)
        # for pokeball in todas_pokeballs:
        #     pygame.draw.rect(screen, (0, 255, 0), pokeball.rect, 2)
        # for poke in lista:
        #     pygame.draw.rect(screen, (0, 255, 0), poke.rect, 2)
        # #------------------------------------------------------------------#

        #cant de Pokeballs
        fuente = pygame.font.Font(None, 36)
        texto_pokeballs = fuente.render(f"Pokeballs: {personaje.pokeballs}", True, (255, 255, 255))
        screen.blit(texto_pokeballs, (10, 10))

        #score
        texto_score = fuente.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(texto_score, (10, 50))

        pygame.display.flip()
        clock.tick(60)

    from game_over import game_over_screen
    game_over_screen(screen, score)
