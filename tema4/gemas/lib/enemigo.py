#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

from config import Config

from random import randint

import os

class Enemigo(pygame.sprite.Sprite):
    """
        Sprite para los enemigos
    """

    # Tipos de enemigos
    ENEMIGO = [
                {'fichero': 'enemigo.png', 'tamanio': (49, 38), 'factor_velocidad': 0.5},
                {'fichero': 'roca.png', 'tamanio': (48, 49), 'factor_velocidad': 0.25},
              ]

    def __init__(self, tipo = 0):

        # Inicializa el ancestro
        pygame.sprite.Sprite.__init__(self)

        # Carga la imagen (convert_alpha() convierte la imagen con transparencias (per pixel transparency)
        self.imagen = pygame.image.load(os.path.join(Config.IMG_DIR, self.ENEMIGO[tipo]['fichero'])).convert_alpha() 

        # Disminuye el tamaño del sprite para que no se vea demasiado grande
        self.imagen = pygame.transform.scale(self.imagen, self.ENEMIGO[tipo]['tamanio'])

        # Obtiene un rectángulo con las dimensiones y posición de la imagen
        self.rect = self.imagen.get_rect()

        # Fila la posición de inicio
        self.rect.centerx, self.rect.centery = self.__get_spawn()

        # Velocidad de movimiento en cada eje
        self.velocidad = {
                            Config.EJE_X: Config.VELOCIDAD_BASE * self.ENEMIGO[tipo]['factor_velocidad'],
                            Config.EJE_Y: Config.VELOCIDAD_BASE * self.ENEMIGO[tipo]['factor_velocidad']
                         }

    def mover(self, tiempo, sprites_activos):
        """
            Gestiona el movimiento del enemigo: movimiento automático en diagonal con rebote
            en los bordes de la ventana

            El cálculo de la posición del personaje se realiza en función de la velocidad y
            del tiempo (d = v * t, distancia = velocidad * tiempo), o sea, la nueva posición
            será igual a la posición actual más la distancia recorrida en el eje correspondiente

            El tiempo recibido como parámetro es el tiempo transcurrido por cada frame
        """

        # Cálculo de la distancia recorrida en un frame
        distancia_x = self.__get_distancia(Config.EJE_X, tiempo)
        distancia_y = self.__get_distancia(Config.EJE_Y, tiempo)

        # Modifica la posición en los dos ejes
        self.rect.centerx += distancia_x
        self.rect.centery += distancia_y

        # Al llegar a un borde de la ventana se invierte el sentido del movimiento en el eje
        # correspondiente y se recalcula la posición

        if self.rect.left <= 0 or self.rect.right >= Config.ANCHO:
            self.__rebote(Config.EJE_X, tiempo)

        if self.rect.top <= 0 or self.rect.bottom >= Config.ALTO:
            self.__rebote(Config.EJE_Y, tiempo)

        #
        # Detección de colisiones
        #

        # Jugador
        if pygame.sprite.collide_rect(self, sprites_activos['jugador']):
            raise Exception("Perdiste!")

        # Gemas
        # Comprueba si ha habido colisión con alguna de las gemas activas, si es que
        # hay alguna
        if sprites_activos['gema']:

            # Comprueba si ha habido colisión con alguna de las gemas activas
            for gema in sprites_activos['gema']:
       
                if pygame.sprite.collide_rect(self, gema):

                    # Las gemas hacen que el enemigo rebote
                    if self.rect.left <= gema.rect.right or self.rect.right >= gema.rect.left:
                        self.__rebote(Config.EJE_X, tiempo)

                    if self.rect.top <= gema.rect.bottom or self.rect.bottom >= gema.rect.top:
                        self.__rebote(Config.EJE_Y, tiempo)

    def __get_spawn(self):
        """
            Selecciona aleatoriamente un punto de spawn de entre los disponibles
        """
        
        return Config.SPAWN_POINTS[randint(0, len(Config.SPAWN_POINTS) - 1)]

    def __get_distancia(self, eje, tiempo):
        """
            Calcula la distancia recorrida en el eje indicado 
        """

        return self.velocidad[eje] * tiempo

    def __rebote(self, eje, tiempo):
        """
            Invierte el sentido del movimiento en el eje especificado y recalcula la
            posición
        """

        # Invierte el sentido del movimiento
        self.velocidad[eje] *= -1

        # Recalcula la distancia recorrida
        distancia = self.__get_distancia(eje, tiempo)

        # Fija la nueva posición
        if eje == Config.EJE_X:
            self.rect.centerx += distancia
        else:
            self.rect.centery += distancia


if __name__ == '__main__':
    print u'Módulo no ejecutable'
