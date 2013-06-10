#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base de datos
from lib.db import DB

# Juego
from lib.config import Config

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
