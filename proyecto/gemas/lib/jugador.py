#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pygame
import pygame
from pygame.locals import *

# Otros
import os

class Jugador(pygame.sprite.Sprite):
    """
        Sprite para el jugador
    """
    def __init__(self, config):

        # Inicializa el ancestro
        pygame.sprite.Sprite.__init__(self)

        # Valores de configuración
        self.config = config

        # Carga la imagen (convert_alpha() convierte la imagen con transparencias (per pixel transparency))
        self.imagen = pygame.image.load(os.path.join(self.config.dir_img, 'jugador.png')).convert_alpha() 

        # Disminuye el tamaño del sprite para que no se vea demasiado grande
        self.imagen = pygame.transform.scale(self.imagen, (57, 67))

        # Obtiene un rectángulo con las dimensiones y posición de la imagen
        self.rect = self.imagen.get_rect()

        # Establece el centro de la ventana como posición inicial
        self.rect.centerx = self.config.ventana_ancho / 2
        self.rect.centery = self.config.ventana_alto / 2

        # Velocidad de movimiento
        self.velocidad = self.config.velocidad_base
        

    def mover(self, tiempo):
        """
            Gestiona el movimiento del personaje: movimiento con los cursores

            El cálculo de la posición del personaje se realiza en función de la velocidad y
            del tiempo (d = v * t, distancia = velocidad * tiempo), o sea, la nueva posición
            será igual a la posición actual más la distancia recorrida en el eje correspondiente

            El parámetro recibido es el tiempo transcurrido por cada frame
        """

        # Obtiene las pulsaciones de teclas
        teclas = pygame.key.get_pressed()

        # Cálculo de la distancia recorrida en un frame
        distancia = self.velocidad * tiempo

        # Los límites del movimiento son los bordes de la ventana
        if self.rect.top >= 0:

            # Cursor Arriba
            if teclas[K_UP]:

                # Desplazamiento hacia arriba
                self.rect.centery -= distancia

        if self.rect.bottom <= self.config.ventana_alto:

            # Cursor Abajo
            if teclas[K_DOWN]:

                # Desplazamiento hacia abajo
                self.rect.centery += distancia

        if self.rect.left >= 0:

            # Cursor Izquierda
            if teclas[K_LEFT]:

                # Desplazamiento hacia la izquierda
                self.rect.centerx -= distancia

        if self.rect.right <= self.config.ventana_ancho:

            # Cursor Derecha
            if teclas[K_RIGHT]:

                # Desplazamiento hacia la derecha
                self.rect.centerx += distancia

if __name__ == '__main__':
    print u'Módulo no ejecutable.'
