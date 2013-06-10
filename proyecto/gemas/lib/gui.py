#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GTK
from gi.repository import Gtk

class GUI():
    """
        Herramienta de configuración
    """

    def __init__(self):
        
        # Instancia el constructor de la interfaz y lee el fichero
        # que la contiene
        self.builder = Gtk.Builder()
        self.builder.add_from_file("lib/gui.glade")

        # Manejador de señales
        handlers = {
                    'onWindowMainDestroy': self.window_main_destroy,
                    'onImagemenuitemSalirActivate': self.window_main_destroy
                   }

        # Conecta las señales con las acciones (callbacks)
        self.builder.connect_signals(handlers)

        # Ventana principal
        self.window = self.builder.get_object("windowMain")

    ##
    ## MAIN
    ##
    def main(self):
        """
            Método de inicio
        """

        # Muestra la ventana principal
        self.window.show_all()

        # A la espera de evento
        Gtk.main()
    
    ##
    ## VENTANA PRINCIPAL
    ##
    def window_main_destroy(self, window):
        """
            Termina la ejecución del programa
        """

        # Saliendo
        Gtk.main_quit()

if __name__ == '__main__':
    print u'Módulo no ejecutable.'
