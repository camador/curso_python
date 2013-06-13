#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Config():
    """
        Valores de configuración del juego
    """

    def __init__(self, db):
        """
            Establece los valores de configuración
        """

        try:

            # 
            # Toma los valores de la base de datos
            # 

            # Tamaño de la ventana
            self.ventana_ancho = int(db.get_config('VENTANA_ANCHO'))
            self.ventana_alto = int(db.get_config('VENTANA_ALTO'))

            # Ubicación de los ficheros
            self.dir_img = db.get_config('DIR_IMG')

            # Velocidad base para todos los sprites
            self.velocidad_base = int(db.get_config('VELOCIDAD_BASE'))

            # Número de frames por segundo
            self.framerate = int(db.get_config('FRAMERATE'))


            #
            # Gemas
            #

            # Número máximo de gemas activas
            self.gema_max_activas = int(db.get_config('GEMA_MAX_ACTIVAS'))

            # Tiempo necesario para el respawn de una nueva gema (en milisegundos)
            self.gema_respawn = int(db.get_config('GEMA_RESPAWN'))

            # Vida (en segundos) de las gemas
            self.gema_vida = int(db.get_config('GEMA_VIDA'))


            #
            # Gemas
            #

            # Tipos de enemigos
            self.enemigos = db.get_enemigos()
    

            # 
            # Otros valores no tomados de la base de datos
            # 

            # Nombre de los ejes
            self.eje_x = 'x'
            self.eje_y = 'y'

            # Puntos de spawn (las 4 esquinas)
            self.spawn_margen_x = self.ventana_ancho / 10
            self.spawn_margen_y = self.ventana_alto / 8
            self.spawn_points = [
                                    (self.spawn_margen_x, self.spawn_margen_y),
                                    (self.spawn_margen_x, self.ventana_alto - self.spawn_margen_y),
                                    (self.ventana_ancho - self.spawn_margen_x, self.spawn_margen_y),
                                    (self.ventana_ancho - self.spawn_margen_x, self.ventana_alto - self.spawn_margen_y)
                                ]

        except Exception, e:
            print '\n'
            print u'Error de Configuración: '
            print '\n\t', e, '\n'

if __name__ == '__main__':
    print u'Módulo no ejecutable.'
