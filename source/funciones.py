import pygame
from constantes import *

def cargar_y_redimensionar_imagen(ruta: str, ancho: int, alto: int) -> pygame.Surface:
    """
    Carga una imagen desde una ruta dada y la redimensiona a las dimensiones especificadas.

    Args:
    - ruta (str): La ruta del archivo de imagen.
    - ancho (int): El ancho deseado para la imagen redimensionada.
    - alto (int): El alto deseado para la imagen redimensionada.

    Returns:
    - pygame.Surface: La imagen cargada y redimensionada como un objeto Surface de Pygame.
    """
    import pygame, os
    
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se pudo encontrar el archivo de imagen en la ruta: {ruta}")

    try:
        imagen = pygame.image.load(ruta)
    except pygame.error as e:
        raise Exception(f"No se pudo cargar la imagen: {ruta}") from e

    imagen_redimensionada = pygame.transform.scale(imagen, (ancho, alto))
    return imagen_redimensionada

def pausa(tecla):
    """pausa el bucle del jeugo

    Args:
        tecla (la tecla a la cual se le asigana la funcion): description
    """
    continuar = True
    while continuar :

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == tecla:
                    continuar = False

def dibujar_boton(screen,text, rect, color, color_si_se_toca, alpha, action=None):
    """summary

    Args:
        screen (type): pantalla 
        text (type): texto a escribir 
        rect (type): rectangulo a pasar 
        color (type): color_del cuadrado 
        color_si_se_toca (type): __ 
        alpha (type): description 
        action (type, optional): description. Defaults to None. 

    Returns:
        type: description
    """
    import pygame
    font = pygame.font.Font(None, 74)

    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    se_esta_tocando = rect.collidepoint(mouse_pos)


    superficie_boton = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    if se_esta_tocando:
        superficie_boton.fill((color_si_se_toca, alpha))
        if click[0] == 1 and action:
            pygame.time.delay(200)
            action()

    else:
        superficie_boton.fill((color, alpha))

    screen.blit(superficie_boton, (rect.x, rect.y))


    fuente = font.render(text, True, (0,0,0))
    screen.blit(fuente, (rect.x + (rect.width - fuente.get_width()) // 2, rect.y + (rect.height - fuente.get_height()) // 2))
    return se_esta_tocando

def pausa(tecla, screen):
    """pausa el bucle del jeugo

    Args:
        tecla (la tecla a la cual se le asigana la funcion): description
    """
    continuar = True
    while continuar :

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == tecla:
                    continuar = False
    
        fuente = pygame.font.Font(None, 74)
        mensaje_pausa = fuente.render("PAUSA", True, (255, 0, 0))
        mensaje_pausa_rect = mensaje_pausa.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2))
        screen.blit(mensaje_pausa, mensaje_pausa_rect)
        
        pygame.display.flip()

def ordenar(lista:list):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1-i):
            if int(lista[j][1]) < int(lista[j+1][1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]

