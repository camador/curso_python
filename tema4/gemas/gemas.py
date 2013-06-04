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
import os

# Tamaño de la ventana
ANCHO = 800
ALTO = 600

# Ubicación de los ficheros
IMG_DIR = 'imagenes'

# Velocidad base para todos los sprites
VELOCIDAD_BASE = 1

# Número de frames por segundo
FRAMERATE = 60

##
## JUGADOR
##

class Jugador(pygame.sprite.Sprite):
    """
        Sprite para el jugador
    """

    def __init__(self):

        # Inicializa el ancestro
        pygame.sprite.Sprite.__init__(self)

        # Carga la imagen (convert_alpha() convierte la imagen con transparencias (per pixel transparency)
        self.imagen = pygame.image.load(os.path.join(IMG_DIR, 'jugador.png')).convert_alpha() 

        # Obtiene un rectángulo con las dimensiones y posición de la imagen
        self.rect = self.imagen.get_rect()

        # Estable el centro de la ventana como posición inicial
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2

        # Velocidad de movimiento
        self.velocidad = VELOCIDAD_BASE

    def mover(self, tiempo):
        """
            Gestiona el movimiento del personaje

            El cálculo de la posición del personaje se realiza en función de la velocidad y
            del tiempo (d = v * t, distancia = velocidad * tiempo), o sea, la nueva posición
            será igual a la posición actual más la distancia recorrida en el eje correspondiente
        """

        # Los límites del movimiento son los bordes de la ventana
        if self.rect.top >= 0 and self.rect.bottom <= ALTO and self.rect.left >= 0 and self.rect.right <= ANCHO:

            # Obtiene las pulsaciones de teclas
            teclas = pygame.key.get_pressed()

            # Cursor Arriba
            if teclas[K_UP]:

                # Desplazamiento hacia arriba
                self.rect.centery -=  self.velocidad * tiempo

##
## MAIN
##

def main():

    try:

        # Crea la ventana
        ventana = pygame.display.set_mode((ANCHO, ALTO))

        # Título de la ventana
        pygame.display.set_caption('Da rienda suelta a tu imaginación - César Amador')

        # Carga el fondo (convirtiéndolo al formato usado en SDL para mejorar la eficiencia)
        fondo = pygame.image.load(os.path.join(IMG_DIR, 'fondo.jpg')).convert()

        # Instancia al jugador
        jugador = Jugador()

        # Instancia un reloj para controlar el tiempo
        reloj = pygame.time.Clock()

        # El programa permanece funcionando hasta que se cierra la ventana
        while True:

            # Averigua el tiempo (en milisegundos) transcurrido por cada frame (cada iteración del bucle)
            # Además, al usar FRAMERATE en la llamada, se fija el número de frames por segundo 
            # independientemente del hardware de la máquina
            tiempo = reloj.tick(FRAMERATE)

            # Obtiene y recorre la lista de eventos que están teniendo lugar
            for evento in pygame.event.get():

                # Si encuentra el evento QUIT termina la ejecución
                if evento.type == QUIT:
                    sys.exit(0)

            #
            # CALCULO DEL MOVIMIENTO
            # 
            jugador.mover(tiempo)

            #
            # ACTUALIZACIÓN DE POSICIONES EN PANTALLA
            # 

            # Situa el fondo en el primer pixel de la ventana
            ventana.blit(fondo, (0, 0))

            # Situa al jugador en la ventana
            ventana.blit(jugador.imagen, jugador.rect)

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
        print '\n\t' , e, '\n'
