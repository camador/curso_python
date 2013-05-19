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

        # Recupera la ventana principal y la muestra
        self.window = self.builder.get_object("mainWindow")
        self.window.show_all()

def main():
    app = CRUD()
    Gtk.main()

if __name__ == "__main__":
    main()
