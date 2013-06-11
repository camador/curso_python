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

    # Vida de la gema en segundos
    vida = 3

    def __init__(self, config, sprites_activos = {}):

        # Inicializa el ancestro
        pygame.sprite.Sprite.__init__(self)

        # Valores de configuración
        self.config = config

        # Carga la imagen (convert_alpha() convierte la imagen con transparencias (per pixel transparency)
        self.imagen = pygame.image.load(os.path.join(self.config.dir_img, 'gema1.png')).convert_alpha() 

        # Obtiene un rectángulo con las dimensiones y posición de la imagen
        self.rect = self.imagen.get_rect()

        # Fila la posición de inicio
        self.rect.centerx, self.rect.centery = self.__get_spawn()
        
        #
        # Evita que las gemas aparezcan unas sobre otras
        #

        # Si no hay otras gemas no hay que comprobar si hay colisión
        if sprites_activos['gema']:
            comprobar_colision = True
        else:
            comprobar_colision = False

        # Realiza comprobaciones de colisión hasta que la nueva gema no colisiona con
        # las ya existentes
        while comprobar_colision:
            
            comprobar_colision = False

            # Comprueba si ha habido colisión con alguna de las gemas activas
            for gema in sprites_activos['gema']:
                
                if pygame.sprite.collide_rect(self, gema):
                    
                    # Calcula una nueva posición de inicio y fuerza la comprobación
                    self.rect.centerx, self.rect.centery = self.__get_spawn()
                    comprobar_colision = True

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
            vida_perdida = (1.0 / self.config.framerate)
            self.vida -= vida_perdida

        else:
            vida_perdida = 0

        return vida_perdida

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
