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

                    'onButtonGuardarClicked': self.on_guardar
                   }

        # Conecta las señales con las acciones (callbacks)
        self.builder.connect_signals(handlers)

        # Ventana principal
        self.window = self.builder.get_object('windowMain')

        # FPS
        self.spinbutton_fps = self.builder.get_object('spinbuttonFPS')

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

        # FPS
        framerate = int(self.db.get_config('FRAMERATE'))
        self.spinbutton_fps.set_value(framerate)

        # Resoluciones
        #resoluciones = db.get_resoluciones()

        # A la espera de evento
        Gtk.main()
    
    ##
    ## VENTANA PRINCIPAL
    ##
    def window_main_destroy(self, *args):
        """
            Termina la ejecución del programa
        """

        # Saliendo
        Gtk.main_quit()

    ##
    ## GUARDAR
    ##
    def on_guardar(self, *args):
        """
            Guarda en la base de datos los valores de los widgets
        """
        
        # FPS
        self.db.set_config('FRAMERATE', self.spinbutton_fps.get_value_as_int())
    
        # Informa al usuario
        self.status.push(self.status_context_id, 'Configuración actualizada')

if __name__ == '__main__':
    print u'Módulo no ejecutable.'
