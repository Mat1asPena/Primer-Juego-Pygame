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
        raise Exception(f"No se pudo cargar la imagen: {ruta}")

    imagen_redimensionada = pygame.transform.scale(imagen, (ancho, alto))
    return imagen_redimensionada

def pausa(tecla:pygame.key, screen:pygame.Surface):
    """
    Pausa el bucle del juego y muestra un mensaje de pausa en la pantalla.

    Args:
    - tecla (int): La tecla que se utilizará para pausar y reanudar el juego.
    - screen (pygame.Surface): La pantalla del juego donde se mostrará el mensaje de pausa.
    """
    continuar = True
    while continuar:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == tecla:
                    continuar = False

        fuente = pygame.font.Font(None, 74)
        mensaje_pausa = fuente.render("PAUSA", True, (255, 0, 0))
        mensaje_pausa_rect = mensaje_pausa.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2))
        screen.blit(mensaje_pausa, mensaje_pausa_rect)
        
        pygame.display.flip()

def dibujar_boton(screen,text, rect, color, color_si_se_toca, alpha, action):
    """
    Dibuja un botón en la pantalla y ejecuta una acción si el botón es presionado.

    Args:
    - screen (pygame.Surface): La pantalla donde se dibujará el botón.
    - text (str): El texto que se mostrará en el botón.
    - rect (pygame.Rect): El rectángulo que define la posición y el tamaño del botón.
    - color (tuple): El color del botón.
    - color_si_se_toca (tuple): El color del botón cuando el mouse está sobre él.
    - alpha (int): El valor de transparencia del botón.
    - action (callable, optional): La acción a ejecutar cuando se presiona el botón. Defaults to None.

    Returns:
    - bool: True si el botón está siendo tocado, False en caso contrario.
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

def ordenar(lista: list):
    """
    Ordena una lista de tuplas en función del segundo elemento en orden descendente.
    Args:
    - lista (list): La lista de tuplas a ordenar.
    Raises:
    - TypeError: Si la entrada no es una lista o no contiene elementos.
    - ValueError: Si los elementos en las tuplas no pueden ser convertidos a enteros.
    """
    if not isinstance(lista, list):
        raise ValueError("La entrada debe ser una lista.")
    
    if len(lista) < 2:
        raise ValueError("La lista debe contener al menos dos elementos.")
    
    try:
        n = len(lista)
        for i in range(n-1):
            for j in range(n-1-i):
                if int(lista[j][1]) < int(lista[j+1][1]):
                    lista[j], lista[j+1] = lista[j+1], lista[j]
    except ValueError as e:
        raise ValueError("El elemento de la lista debe ser convertible entero.") from e


