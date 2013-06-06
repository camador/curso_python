#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Config():
    """
        Constantes de configuración para el juego
    """

    # Tamaño de la ventana
    ANCHO = 1024
    ALTO = 768

    # Nombre de los ejes
    EJE_X = 'x'
    EJE_Y = 'y'

    # Ubicación de los ficheros
    IMG_DIR = 'imagenes'

    # Velocidad base para todos los sprites
    VELOCIDAD_BASE = 1

    # Número de frames por segundo
    FRAMERATE = 60

    # Puntos de spawn (las 4 esquinas)
    SPAWN_MARGEN_X = ANCHO / 10 
    SPAWN_MARGEN_Y = ALTO / 8
    SPAWN_POINTS = [
                    (SPAWN_MARGEN_X, SPAWN_MARGEN_Y), 
                    (SPAWN_MARGEN_X, ALTO - SPAWN_MARGEN_Y), 
                    (ANCHO - SPAWN_MARGEN_X, SPAWN_MARGEN_Y), 
                    (ANCHO - SPAWN_MARGEN_X, ALTO - SPAWN_MARGEN_Y)]


if __name__ == '__main__':
    print u'Módulo no ejecutable'
