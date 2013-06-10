#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
import pygame

# Otros
import os

class Jugador(pygame.sprite.Sprite):
    """
        Sprite para el jugador
    """
    def __init__(self, config):

        # Inicializa el ancestro
        pygame.sprite.Sprite.__init__(self)

        # Carga la imagen (convert_alpha() convierte la imagen con transparencias (per pixel transparency))
        self.imagen = pygame.image.load(os.path.join(config.dir_img, 'jugador.png')).convert_alpha() 

        # Disminuye el tamaño del sprite para que no se vea demasiado grande
        self.imagen = pygame.transform.scale(self.imagen, (57, 67))

        # Obtiene un rectángulo con las dimensiones y posición de la imagen
        self.rect = self.imagen.get_rect()

        # Estable el centro de la ventana como posición inicial
        self.rect.centerx = config.ventana_ancho / 2
        self.rect.centery = config.ventana_alto / 2

        # Velocidad de movimiento
        self.velocidad = config.velocidad_base

if __name__ == '__main__':
    print u'Módulo no ejecutable.'
