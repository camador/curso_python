#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
import pygame

# Otros
from random import randint
import os

class Gema(pygame.sprite.Sprite):
    """
        Sprite para las gemas
    """

    # Vida de la gema
    # La vida viene dada por un número de segundos
    vida = 3

    def __init__(self, config):

        # Inicializa el ancestro
        pygame.sprite.Sprite.__init__(self)

        # Valores de configuración
        self.config = config

        # Carga la imagen (convert_alpha() convierte la imagen con transparencias (per pixel transparency)
        self.imagen = pygame.image.load(os.path.join(self.config.img_dir, 'gema1.png')).convert_alpha() 

        # Obtiene un rectángulo con las dimensiones y posición de la imagen
        self.rect = self.imagen.get_rect()

        # Fila la posición de inicio
        self.rect.centerx, self.rect.centery = self.__get_spawn()

    def __get_spawn(self):
        """
            Genera un punto de spawn en cualquier punto de la pantalla excluyendo
            los márgenes
        """
        x = randint(self.config.spawn_margen_x, self.config.ventana_ancho - self.config.spawn_margen_x)  
        y = randint(self.config.spawn_margen_y, self.config.ventana_alto - self.config.spawn_margen_y)  

        return (x, y)

if __name__ == '__main__':
    print u'Módulo no ejecutable'
