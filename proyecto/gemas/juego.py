#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base de datos
from lib.db import DB

# Juego
from lib.config import Config
from lib.jugador import Jugador
from lib.enemigo import Enemigo
from lib.gema import Gema
from lib.marcador import Marcador
from lib.record import Record

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

        # Diccionario de sprites activos en cada momento
        sprites_activos = {}

        # Instancia un reloj para controlar el tiempo
        reloj = pygame.time.Clock()

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
        # SPRITES
        #

        # Instancia al jugador y lo añade a la lista de sprites activos
        jugador = Jugador(config)
        sprites_activos['jugador'] = jugador

        # Instancia dos enemigos y los añade a la lista de sprites activos
        sprites_activos['enemigo'] = [Enemigo(config, 0), Enemigo(config, 1)]

        # Instancia las gemas y las añade a la lista de sprites activos
        sprites_activos['gema'] = []
        for i in range(1, config.gema_max_activas + 1):
            gema = Gema(config, 0, sprites_activos)
            sprites_activos['gema'].append(gema)

        # Indica el momento en que ha de generarse una nueva gema (0 = no se genera ninguna)
        proximo_respawn_gema = 0

        # Marcador
        marcador = Marcador(config)
        sprites_activos['marcador'] = marcador

        # Puntuación máxima
        record = Record(config, db)
        sprites_activos['record'] = record
        

        #
        # BUCLE DE EVENTOS
        #

        # El programa permanece funcionando hasta que se cierra la ventana
        # Cada iteración del bucle es un frame
        salir = False
        while not salir:

            # Averigua el tiempo (en milisegundos) transcurrido por cada frame
            # Además, al usar FRAMERATE en la llamada, se fija el número de frames por segundo
            # independientemente del hardware de la máquina
            tiempo = reloj.tick(config.framerate)

            # Obtiene y recorre la lista de eventos que están teniendo lugar
            for evento in pygame.event.get():

                # Si encuentra el evento QUIT termina la ejecución
                if evento.type == QUIT:
                    salir = True

                # La tecla ESC termina la ejecución
                elif evento.type == KEYDOWN:
                    if evento.key == K_ESCAPE:
                        salir = True

            #
            # CALCULO DEL MOVIMIENTO Y PUNTUACIÓN
            #

            jugador.mover(tiempo, sprites_activos)
            marcador.render_puntos(jugador.puntos)
            for enemigo in sprites_activos['enemigo']:
                enemigo.mover(tiempo, sprites_activos)

            #
            # ACTUALIZACIÓN DE POSICIONES EN PANTALLA
            #

            # Situa el fondo en el primer pixel de la ventana
            ventana.blit(fondo, (0, 0))

            # Actualiza la posición de los sprites
            for nombre in sprites_activos.keys():
                # Si se trata de una lista de sprites la recorre y
                # procesa cada elemento
                if isinstance(sprites_activos[nombre], list):
                    for elemento in sprites_activos[nombre]:

                        # Si el sprite es una gema sin vida la elimina de los sprites activos
                        if nombre == 'gema' and elemento.vida <= 0:
                            sprites_activos[nombre].remove(elemento)
                        else:
                            ventana.blit(elemento.imagen, elemento.rect)
                else:
                    ventana.blit(sprites_activos[nombre].imagen, sprites_activos[nombre].rect)

            #
            # ACTUALIZACIÓN DE LA PANTALLA
            #

            # Dibuja la escena
            pygame.display.flip()

            #
            # EVALUACIÓN DEL ESTADO DE LOS SPRITES
            #

            # Comprueba si el jugador sigue vivo
            if not jugador.vivo:
                # Si no sigue vivo sale del bucle
                salir = True

            else:

                # Si sigue vivo comprueba si es necesario generar una nueva gema

                # Las gemas se generan siempre que haya menos del máximo permitido y 
                # siempre después de pasado cierto tiempo (config.gema_respawn) desde la
                # desaparición de una gema o desde la generación de una nueva, lo que ocurra
                # antes. Es decir, mientras haya menos gemas de las permitidas se genera una
                # nueva cada 'config.gema_respawn' milisegundos

                # Si hay menos gemas activas del máximo permitido es necesario generar una nueva
                if len(sprites_activos['gema']) < config.gema_max_activas:

                    # Calcula el momento para la creación de la gema, pero sólo si dicho momento no 
                    # ha sido todavía calculado para evitar que a cada iteración del bucle (cada frame)
                    # se recalcule y la gema no llegue a generarse nunca
                    if proximo_respawn_gema == 0:

                        # La gema se generará después del momento actual más el tiempo de espera
                        # para la generación de gemas
                        proximo_respawn_gema = pygame.time.get_ticks() + config.gema_respawn

                    # Comprueba si ha pasado suficiente tiempo como para generar la gema
                    if proximo_respawn_gema <= pygame.time.get_ticks():

                        # Ya se puede crear la gema y añadirla a la lista de sprites activos
                        gema = Gema(config, 0, sprites_activos)
                        sprites_activos['gema'].append(gema)

                        # Resetea el momento para la creación de la siguiente gema
                        proximo_respawn_gema = 0

        #
        # FIN DE LA EJECUCIÓN
        #

        # Guarda la puntución
        db.guarda_puntuacion(jugador.puntos)

        # Informa al usuario
        print '\n'
        print u'Game Over ^_^'
        print u'Tu puntuación: ', jugador.puntos
        print '\n'

        # Cierra la conexión con la base de datos
        db.close()
        
        # Termina la ejecución
        sys.exit(0)

    except pygame.error, e:
        print '\n'
        print u'Error en Pygame: '
        print '\n\t' , e, '\n'

if __name__ == '__main__':

    pygame.init()

    # Empezando...
    main()
    try:
        
        # Inicializa Pygame
        pygame.init()

        # Empezando...
        main()
        
    except Exception, e:
        print '\n'
        print u'Error inesperado: '
        print '\n\t', e, '\n'
