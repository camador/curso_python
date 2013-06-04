#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# DA RIENDA SUELTA A TU IMAGINACIÓN
#
# Requisitos mínimos:
# 
# - Debe haber una imagen de fondo.
# - 1 Jugador (Sprite) controlado por teclado.
# - 5 Objetos (Sprite estático o con movimiento aleatorio).
# 
# Requisitos OPCIONALES:
# 
# - Establecer un mecanismo de puntuación (mediante colisiones, por ejemplo).
# - Habrá Objetos (Sprite) que sumen puntos y otros que resten. Al tocar un objeto especifico, con la imagen que mas te guste, se acabará el juego. Se muestra el texto "game over" por ejemplo y después el ranking.
# - El juego tiene que tener un tiempo limite para conseguir puntos, acabado ese tiempo finaliza el juego. Se debe mostrar un texto con el tiempo que queda.
# - Mantener ranking de puntos: al acabar el juego se mostrará una tabla con las cinco puntuaciones mas altas.
# - Durante el juego se debe mostrar un texto con la puntuación actual.
# - Solicitar un nombre de usuario, para mostrarlo en ranking junto a su puntuación.
#

import pygame
from pygame.locals import *

import sys

# Constantes con el tamaño de la ventana
ANCHO = 800
ALTO = 600

def main():

    # Crea la ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))

    # Título de la ventana
    pygame.display.set_caption('Da rienda suelta a tu imaginación - César Amador')

    # El programa permanece funcionando hasta que se cierra la ventana
    while True:

        # Obtiene y recorre la lista de eventos que están teniendo lugar
        for evento in pygame.event.get():

            # Si encuentra el evento QUIT termina la ejecución
            if evento.type == QUIT:
                sys.exit(0)


    return 0

if __name__ == '__main__':

    # Inicializa Pygame
    pygame.init()

    # Empezando...
    main()
