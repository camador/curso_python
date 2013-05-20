#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk

class CRUD:
    """
        Gestión CRUD de una tabla en MySQL
    """

    def __init__(self):
        """
            Inicializa la interfaz gráfica de usuario (GUI)
        """

        # Instancia el constructor de la interfaz y lee el fichero
        # que la contiene
        self.builder = Gtk.Builder()
        self.builder.add_from_file("crud.glade")

        # Manejador de señales
        handlers = {
                    'mainWindowDestroy': self.main_window_destroy,
                    'ayudaAbout': self.ayuda_about
                   }

        # Conecta las señales con las acciones (callbacks)
        self.builder.connect_signals(handlers)


    def main(self):
        """
            Método de inicio
        """

        # Recupera la ventana principal y la muestra
        self.window = self.builder.get_object("mainWindow")
        self.window.show_all()

        # A la espera de evento
        Gtk.main()

    def main_window_destroy(self, window):
        """
            Termina la ejecución del programa
        """

        # Saliendo
        Gtk.main_quit()
    

    def ayuda_about(self, *args):
        """
            Muestra la ventana 'Acerca de'
        """
        about = self.builder.get_object('aboutdialog')
        about.show_all()

if __name__ == "__main__":

    # Instancia la clase para la GUI
    crud = CRUD()

    # Método de inicio
    crud.main()
