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

# Pygame
import pygame
from pygame.locals import *

# Juego
from lib.config import Config
from lib.jugador import Jugador
from lib.enemigo import Enemigo
from lib.gema import Gema

# Otros
import sys
import os

##
## MAIN
##

def main():

    try:

        # Diccionario de sprites activos en cada momento
        sprites_activos = {}

        # Crea la ventana
        ventana = pygame.display.set_mode((Config.ANCHO, Config.ALTO))

        # Título de la ventana
        pygame.display.set_caption('Da rienda suelta a tu imaginación - César Amador')

        # Carga el fondo (convirtiéndolo al formato usado en SDL para mejorar la eficiencia)
        fondo = pygame.image.load(os.path.join(Config.IMG_DIR, 'fondo.jpg')).convert()

        # Instancia al jugador y lo añade a la lista de sprites activos
        jugador = Jugador()
        sprites_activos['jugador'] = jugador

        # Instancia un enemigo y lo añade a la lista de sprites activos
        enemigo = Enemigo()
        sprites_activos['enemigo'] = enemigo 

        # Instancia una gema y la añade a la lista de sprites activos
        gema = Gema()
        sprites_activos['gema'] = gema 

        # Instancia un reloj para controlar el tiempo
        reloj = pygame.time.Clock()

        # El programa permanece funcionando hasta que se cierra la ventana
        # Cada iteración del bucle es un frame
        while True:

            # Averigua el tiempo (en milisegundos) transcurrido por cada frame
            # Además, al usar FRAMERATE en la llamada, se fija el número de frames por segundo 
            # independientemente del hardware de la máquina
            tiempo = reloj.tick(Config.FRAMERATE)

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
            ############ Vida de la gema
            #
            gema.tick()
            if gema.vida <= 0:
                raise Exception('Gema vacía')

            #
            # ACTUALIZACIÓN DE POSICIONES EN PANTALLA
            # 

            # Situa el fondo en el primer pixel de la ventana
            ventana.blit(fondo, (0, 0))

            # Actualiza la posición de los sprites
            for nombre in sprites_activos.keys():
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
        print '\n\t' , e, '\n'
