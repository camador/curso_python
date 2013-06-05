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
from random import randint

# Tamaño de la ventana
ANCHO = 1024
ALTO = 768

# Nombre de los ejes
EJE_X = 'x'
EJE_Y = 'y'

# Ubicación de los ficheros
IMG_DIR = 'imagenes'

# Velocidad base para todos los sprites
VELOCIDAD_BASE = 1

# Número de frames por segundo
FRAMERATE = 60

# Puntos de spawn (las 4 esquinas)
SPAWN_MARGEN_X = ANCHO / 10 
SPAWN_MARGEN_Y = ALTO / 8
SPAWN_POINTS = [
                (SPAWN_MARGEN_X, SPAWN_MARGEN_Y), 
                (SPAWN_MARGEN_X, ALTO - SPAWN_MARGEN_Y), 
                (ANCHO - SPAWN_MARGEN_X, SPAWN_MARGEN_Y), 
                (ANCHO - SPAWN_MARGEN_X, ALTO - SPAWN_MARGEN_Y)]

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
            Gestiona el movimiento del personaje: movimiento con los cursores

            El cálculo de la posición del personaje se realiza en función de la velocidad y
            del tiempo (d = v * t, distancia = velocidad * tiempo), o sea, la nueva posición
            será igual a la posición actual más la distancia recorrida en el eje correspondiente

            El tiempo recibido como parámetro es el tiempo transcurrido por cada frame
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

        if self.rect.bottom <= ALTO:

            # Cursor Abajo
            if teclas[K_DOWN]:

                # Desplazamiento hacia abajo
                self.rect.centery += distancia

        if self.rect.left >= 0:

            # Cursor Izquierda
            if teclas[K_LEFT]:

                # Desplazamiento hacia la izquierda 
                self.rect.centerx -= distancia

        if self.rect.right <= ANCHO:

            # Cursor Derecha
            if teclas[K_RIGHT]:

                # Desplazamiento hacia la derecha
                self.rect.centerx += distancia

##
## ENEMIGOS
##

class Enemigo(pygame.sprite.Sprite):
    """
        Sprite para los enemigos
    """

    def __init__(self):

        # Inicializa el ancestro
        pygame.sprite.Sprite.__init__(self)

        # Carga la imagen (convert_alpha() convierte la imagen con transparencias (per pixel transparency)
        self.imagen = pygame.image.load(os.path.join(IMG_DIR, 'enemigo.png')).convert_alpha() 

        # Obtiene un rectángulo con las dimensiones y posición de la imagen
        self.rect = self.imagen.get_rect()

        # Fila la posición de inicio
        self.rect.centerx, self.rect.centery = self.__get_spawn()

        # Velocidad de movimiento en cada eje
        self.velocidad = {
                            EJE_X: VELOCIDAD_BASE * 0.5,
                            EJE_Y: VELOCIDAD_BASE * 0.5
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
        distancia_x = self.__get_distancia(EJE_X, tiempo)
        distancia_y = self.__get_distancia(EJE_Y, tiempo)

        # Modifica la posición en los dos ejes
        self.rect.centerx += distancia_x
        self.rect.centery += distancia_y

        # Al llegar a un borde de la ventana se invierte el sentido del movimiento en el eje
        # correspondiente y se recalcula la posición

        if self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.velocidad[EJE_X] *= -1
            distancia = self.__get_distancia(EJE_X, tiempo)
            self.rect.centerx += distancia

        if self.rect.top <= 0 or self.rect.bottom >= ALTO:
            self.velocidad[EJE_Y] *= -1
            distancia = self.__get_distancia(EJE_Y, tiempo)
            self.rect.centery += distancia

        # Detección de colisiones
        if pygame.sprite.collide_rect(self, sprites_activos['jugador']):
            raise Exception("Perdiste!")

    def __get_spawn(self):
        """
            Selecciona aleatoriamente un punto de spawn de entre los disponibles
        """
        
        return SPAWN_POINTS[randint(0, len(SPAWN_POINTS) - 1)]

    def __get_distancia(self, eje, tiempo):
        """
            Calcula la distancia recorrida en el eje indicado 
        """

        return self.velocidad[eje] * tiempo


##
## MAIN
##

def main():

    try:

        # Diccionario de sprites activos en cada momento
        sprites_activos = {}

        # Crea la ventana
        ventana = pygame.display.set_mode((ANCHO, ALTO))

        # Título de la ventana
        pygame.display.set_caption('Da rienda suelta a tu imaginación - César Amador')

        # Carga el fondo (convirtiéndolo al formato usado en SDL para mejorar la eficiencia)
        fondo = pygame.image.load(os.path.join(IMG_DIR, 'fondo.jpg')).convert()

        # Instancia al jugador y lo añade a la lista de sprites activos
        jugador = Jugador()
        sprites_activos['jugador'] = jugador

        # Instancia a un enemigo y lo añade a la lista de sprites activos
        enemigo = Enemigo()
        sprites_activos['enemigo'] = enemigo 

        # Instancia un reloj para controlar el tiempo
        reloj = pygame.time.Clock()

        # El programa permanece funcionando hasta que se cierra la ventana
        # Cada iteración del bucle es un frame
        while True:

            # Averigua el tiempo (en milisegundos) transcurrido por cada frame
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
            enemigo.mover(tiempo, sprites_activos)

            #
            # ACTUALIZACIÓN DE POSICIONES EN PANTALLA
            # 

            # Situa el fondo en el primer pixel de la ventana
            ventana.blit(fondo, (0, 0))

            # Enemigo y jugador
            ventana.blit(enemigo.imagen, enemigo.rect)
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
