#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GTK
from gi.repository import Gtk

# Juego
from lib.db import DB

class GUI():
    """
        Herramienta de configuración
    """

    def __init__(self):
        
        # Instancia el constructor de la interfaz y lee el fichero
        # que la contiene
        self.builder = Gtk.Builder()
        self.builder.add_from_file('lib/gui.glade')

        # Manejador de señales
        handlers = {
                    'onWindowMainDestroy': self.window_main_destroy,
                    'onImagemenuitemSalirActivate': self.window_main_destroy,

                    'onSpinbuttonFPSValueChanged': self.limpia_statusbar,
                    'onSpinbuttonGemasMaxActivasValueChanged': self.limpia_statusbar,
                    'onSpinbuttonGemasRespawnValueChanged': self.limpia_statusbar,
                    'onSpinbuttonEnemigosRespawnValueChanged': self.limpia_statusbar,

                    'onComboboxResolucionesChanged': self.limpia_statusbar,

                    'onRadiobuttonJugador1Toggled': self.limpia_statusbar,
                    'onRadiobuttonJugador2Toggled': self.limpia_statusbar,
                    'onRadiobuttonJugador3Toggled': self.limpia_statusbar,
                    'onRadiobuttonJugador4Toggled': self.limpia_statusbar,
                    'onRadiobuttonJugador5Toggled': self.limpia_statusbar,

                    'onButtonGuardarClicked': self.on_guardar
                   }

        # Conecta las señales con las acciones (callbacks)
        self.builder.connect_signals(handlers)

        # Ventana principal
        self.window = self.builder.get_object('windowMain')

        # Resolución
        self.list_store_Resoluciones = self.builder.get_object('liststoreResoluciones')
        self.combo_box_Resoluciones = self.builder.get_object('comboboxResoluciones')

        # FPS
        self.spinbutton_fps = self.builder.get_object('spinbuttonFPS')

        # Jugador
        self.radiobutton_jugador = [
                                    self.builder.get_object('radiobuttonJugador1'),
                                    self.builder.get_object('radiobuttonJugador2'),
                                    self.builder.get_object('radiobuttonJugador3'),
                                    self.builder.get_object('radiobuttonJugador4'),
                                    self.builder.get_object('radiobuttonJugador5')
                                   ]

        # Gemas Máx. Activas
        self.spinbutton_gemas_max_activas = self.builder.get_object('spinbuttonGemasMaxActivas')

        # Gemas Respawn
        self.spinbutton_gemas_respawn = self.builder.get_object('spinbuttonGemasRespawn')

        # Enemigos Respawn
        self.spinbutton_enemigos_respawn = self.builder.get_object('spinbuttonEnemigosRespawn')

        # Barra de estado
        self.status = self.builder.get_object('statusBar')
        self.status_context_id = self.status.get_context_id('main')

        # Gestor de base de datos
        self.db = DB()

    ##
    ## MAIN
    ##
    def main(self):
        """
            Método de inicio
        """

        # Muestra la ventana principal
        self.window.show_all()

        #
        # Lee de la base de datos la información para cada widget
        #

        # Resoluciones
        resolucion_id = 0
        resoluciones = self.db.get_resoluciones()
        for resolucion in resoluciones:
            self.list_store_Resoluciones.append([resolucion['descripcion'], int(resolucion['id'])])

            # Comprueba si se trata de la resolución actual
            if resolucion['ancho'] == self.db.get_config('VENTANA_ANCHO') and resolucion['alto'] == self.db.get_config('VENTANA_ALTO'):
                resolucion_actual = resolucion_id

            resolucion_id += 1

        # Seleccion la resolución actual
        self.combo_box_Resoluciones.set_active(resolucion_actual) 

        # FPS
        framerate = int(self.db.get_config('FRAMERATE'))
        self.spinbutton_fps.set_value(framerate)

        # Jugador
        jugador_tipo = int(self.db.get_config('JUGADOR_TIPO'))
        self.radiobutton_jugador[jugador_tipo].set_active(True)

        # Gemas Máx. Activas 
        gemas_max_activas = int(self.db.get_config('GEMA_MAX_ACTIVAS'))
        self.spinbutton_gemas_max_activas.set_value(gemas_max_activas)

        # Gemas Respawn
        gemas_respawn = int(self.db.get_config('GEMA_RESPAWN'))
        self.spinbutton_gemas_respawn.set_value(gemas_respawn)

        # Enemigos Respawn
        enemigos_respawn = int(self.db.get_config('ENEMIGO_RESPAWN'))
        self.spinbutton_enemigos_respawn.set_value(enemigos_respawn)

        # A la espera de evento
        Gtk.main()
    
    ##
    ## VENTANA PRINCIPAL
    ##
    def window_main_destroy(self, *args):
        """
            Termina la ejecución del programa
        """

        # Cierra la conexión con la base de datos
        self.db.close()

        # Saliendo
        Gtk.main_quit()

    ##
    ## BARRA DE ESTADO
    ##
    def limpia_statusbar(self, *args):
        """
            Limpia de mensajes la barra de estado
        """

        self.status.remove_all(self.status_context_id)

    ##
    ## GUARDAR
    ##
    def on_guardar(self, *args):
        """
            Guarda en la base de datos los valores de los widgets
        """

        # 
        # Resoluciones
        # 

        # Resolución seleccionada
        item = self.combo_box_Resoluciones.get_active() 

        # Lista de resoluciones del combobox
        resoluciones = self.combo_box_Resoluciones.get_model()
        
        # Recupera el registro correspondiente a la resolución seleccionada
        resolucion = self.db.get_resolucion(resoluciones[item][0])

        # Actualiza la configuración
        self.db.set_config('VENTANA_ANCHO', resolucion['ancho'])
        self.db.set_config('VENTANA_ALTO', resolucion['alto'])

        # 
        # FPS
        # 
        self.db.set_config('FRAMERATE', self.spinbutton_fps.get_value_as_int())
    
        #
        # JUGADOR
        #

        # Recorre los radiobuttons para localizar el seleccionado
        jugador_seleccionado = 0
        for radio in self.radiobutton_jugador:

            # Cuando encuentra el activo sale del bucle
            if radio.get_active():
                break;
            
            # Si no es el activo incrementa el índice
            jugador_seleccionado += 1

        # Actualiza la base de datos
        self.db.set_config('JUGADOR_TIPO', jugador_seleccionado)

        #
        # GEMAS
        #

        # Gemas Máx. Activas 
        self.db.set_config('GEMA_MAX_ACTIVAS', self.spinbutton_gemas_max_activas.get_value_as_int())
        self.db.set_config('GEMA_RESPAWN', self.spinbutton_gemas_respawn.get_value_as_int())

        #
        # ENEMIGOS
        #
        self.db.set_config('ENEMIGO_RESPAWN', self.spinbutton_enemigos_respawn.get_value_as_int())


        # Informa al usuario
        self.status.push(self.status_context_id, 'Configuración actualizada')

        # Sale
        self.window_main_destroy()
    

if __name__ == '__main__':
    print u'Módulo no ejecutable.'
