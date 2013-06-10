#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base de datos
from lib.db import DB

# Juego
from lib.config import Config
from lib.jugador import Jugador

# Pygame
import pygame
from pygame.locals import *

# Otros
import os
import sys

def main():

    try :

        #
        # CONFIGURACIÓN
        #

        # Gestor de base de datos
        db = DB()

        # Carga los valores de configuración
        config = Config(db)

        # Diccionario de sprites activos en cada momento
        sprites_activos = {}

        #
        # VENTANA
        #

        # Crea la ventana
        ventana = pygame.display.set_mode((config.ventana_ancho, config.ventana_alto))

        # Título de la ventana
        pygame.display.set_caption('Gemas')

        # Carga el fondo (convirtiéndolo al formato usado en SDL para mejorar la eficiencia)
        fondo = pygame.image.load(os.path.join(config.dir_img, 'fondo.jpg')).convert()

        #
        # SPRITES
        #

        # Instancia al jugador y lo añade a la lista de sprites activos
        jugador = Jugador(config)
        sprites_activos['jugador'] = jugador

        #
        # BUCLE DE EVENTOS
        #

        # El programa permanece funcionando hasta que se cierra la ventana
        # Cada iteración del bucle es un frame
        while True:

            # Obtiene y recorre la lista de eventos que están teniendo lugar
            for evento in pygame.event.get():

                # Si encuentra el evento QUIT termina la ejecución
                if evento.type == QUIT:
                    sys.exit(0)

            #
            # ACTUALIZACIÓN DE POSICIONES EN PANTALLA
            #

            # Situa el fondo en el primer pixel de la ventana
            ventana.blit(fondo, (0, 0))

            # Actualiza la posición de los sprites
            for nombre in sprites_activos.keys():
                # Si se trata de una lista de sprites la recorre y
                # procesa cada elemento
                if isinstance(sprites_activos[nombre], list):
                    for elemento in sprites_activos[nombre]:
                        ventana.blit(elemento.imagen, elemento.rect)
                else:
                    ventana.blit(sprites_activos[nombre].imagen, sprites_activos[nombre].rect)

            #
            # ACTUALIZACIÓN DE LA PANTALLA
            #

            # Dibuja la escena
            pygame.display.flip()


        return 0

    except pygame.error, e:
        print '\n'
        print u'Error en Pygame: '
        print '\n\t' , e, '\n'

if __name__ == '__main__':

    try:
        
        # Inicializa Pygame
        pygame.init()

        # Empezando...
        main()
        
    except Exception, e:
        print '\n'
        print u'Error inesperado: '
        print '\n\t', e, '\n'
