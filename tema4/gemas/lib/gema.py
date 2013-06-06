#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from config import Config

from random import randint

import os

class Gema(pygame.sprite.Sprite):
    """
        Sprite para las gemas
    """

    # Vida de la gema
    # La vida viene dada por un número de segundos
    vida = 3

    def __init__(self):

        # Inicializa el ancestro
        pygame.sprite.Sprite.__init__(self)

        # Carga la imagen (convert_alpha() convierte la imagen con transparencias (per pixel transparency)
        self.imagen = pygame.image.load(os.path.join(Config.IMG_DIR, 'gema1.png')).convert_alpha() 

        # Obtiene un rectángulo con las dimensiones y posición de la imagen
        self.rect = self.imagen.get_rect()

        # Fila la posición de inicio
        self.rect.centerx, self.rect.centery = self.__get_spawn()

    def tick(self):
        """
            Resta puntos de vida a la gema por cada frame que el jugador pase colisionando con
            ella
        """
        
        # La gema ha de seguir viva
        if self.vida > 0:

            # La cantidad de vida restada por cada frame viene dada por la fórmula:
            #
            # vida_restada_por_frame = 1 / FRAMERATE
            #
            # Como el framerate es el número de frames por segundo (fps) y la vida de la gema
            # viene expresada en segundos, dividiendo un segundo entre el número de frames 
            # que tienen lugar en él se obtiene la cantidad de vida que pierde la gema en cada frame.
            self.vida -= (1.0 / Config.FRAMERATE)
        

    def __get_spawn(self):
        """
            Genera un punto de spawn en cualquier punto de la pantalla excluyendo
            los márgenes
        """
        x = randint(Config.SPAWN_MARGEN_X, Config.ANCHO - Config.SPAWN_MARGEN_X)  
        y = randint(Config.SPAWN_MARGEN_Y, Config.ALTO - Config.SPAWN_MARGEN_Y)  

        return (x, y)


if __name__ == '__main__':
    print u'Módulo no ejecutable'
