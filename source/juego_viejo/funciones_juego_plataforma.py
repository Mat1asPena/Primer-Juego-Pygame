import pygame
from random import randrange, randint

def get_random_elemento(lista: list) -> any:
    """
    Devuelve un elemento aleatorio de una lista.

    Args:
        lista (list): La lista de la cual se tomará un elemento aleatorio.

    Returns:
        any: Un elemento aleatorio de la lista.

    Raises:
        ValueError: Si el argumento no es una lista.
    """
    if not isinstance(lista, list):
        raise ValueError("Esto no es una lista")
    
    if len(lista) == 0:
        raise ValueError("La lista está vacía")

    tam = len(lista)
    return lista[randrange(tam)]

def get_random_color(colors_list: list) -> tuple[int, int, int]:
    """
    Devuelve un color aleatorio de una lista de colores.

    Args:
        colors_list (list): La lista de colores de la cual se tomará un color aleatorio.

    Returns:
        tuple[int, int, int]: Un color aleatorio en formato RGB.

    Raises:
        ValueError: Si el argumento no es una lista o si la lista está vacía.
    """
    if not isinstance(colors_list, list):
        raise ValueError("Esto no es una lista")
    
    if len(colors_list) == 0:
        raise ValueError("La lista de colores está vacía")
    
    return get_random_elemento(colors_list)

def color_random() -> tuple[int, int, int]:
    """
    Genera un color aleatorio.

    Returns:
        tuple[int, int, int]: Un color aleatorio en formato RGB.
    """
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

def escalar_imagen(imagen: pygame.Surface, escala: float) -> pygame.Surface:
    """
    Escala una imagen por un factor dado.

    Args:
        imagen (pygame.Surface): La imagen a escalar.
        escala (float): El factor de escala.

    Returns:
        pygame.Surface: La imagen escalada.

    Raises:
        TypeError: Si el argumento `imagen` no es una instancia de pygame.Surface.
        ValueError: Si el argumento `escala` no es un número positivo.
    """
    if not isinstance(imagen, pygame.Surface):
        raise TypeError("El argumento 'imagen' debe ser una instancia de pygame.Surface")
    
    if not isinstance(escala, (int, float)) or escala <= 0:
        raise ValueError("El argumento 'escala' debe ser un número positivo")

    width = imagen.get_width()
    height = imagen.get_height()
    nueva_imagen = pygame.transform.scale(imagen, (int(width * escala), int(height * escala)))
    return nueva_imagen

def pausa(tecla: int):
    """
    Pone en pausa el juego hasta que se presione una tecla específica.

    Args:
        tecla (int): La tecla que se debe presionar para salir de la pausa.

    Raises:
        TypeError: Si el argumento `tecla` no es un número entero.
    """
    if not isinstance(tecla, int):
        raise TypeError("El argumento 'tecla' debe ser un número entero")

    pausado = True
    while pausado:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == tecla:
                    pausado = False
