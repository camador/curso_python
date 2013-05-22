#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import  MySQLdb

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

        # Barra de estado
        self.status = self.builder.get_object('mainStatusBar')
        self.status_context_id = self.status.get_context_id('main')

        # Conexión a la base de datos
        # Se asume la existencia de la base de datos 'crud_camador' en localhost,
        # con permisos para el usuario 'crud_camador' con password 'crud'
        # La tabla esperada se llama 'crud'
        self.db = MySQLdb.connect(host = 'localhost', user = 'crud_camador', passwd = 'crud', db = 'crud_camador')

        # Crea el cursor
        self.cursor = self.db.cursor(MySQLdb.cursors.DictCursor)

        # Probando status bar
        self.status.push(self.status_context_id, 'Éxito al conectar!')



        # Recupera los IDs de la tabla
        self.cursor.execute('select id from crud;')
        registros = self.cursor.fetchall()

        # Llena el combobox con los IDs
        list_store_IDs = self.builder.get_object('liststoreIDs')
        for registro in registros:
            print registro['id']
            list_store_IDs.append([registro['id']])

        # Limpia la selección de elementos
        combo_box_IDs = self.builder.get_object('comboboxIDs')
        combo_box_IDs.set_active(0)


        # A la espera de evento
        Gtk.main()


    def main_window_destroy(self, window):
        """
            Termina la ejecución del programa
        """

        # Cierra cursor y conexión de la base de datos
        self.cursor.close()
        self.db.close()

        # Saliendo
        Gtk.main_quit()
    

    def ayuda_about(self, *args):
        """
            Muestra la ventana 'Acerca de'
        """
        # Recupera la ventana
        about = self.builder.get_object('aboutdialog')

        # La muestra mientras no se cierre mediante el botón Cerrar o 
        # pulsando sobre la 'x' de la ventana (se activa un bucle while)
        about.run()

        # Oculta la ventana tras la orden de cierre que finaliza el bucle while
        about.hide()

if __name__ == "__main__":

    try:

        # Instancia la clase para la GUI
        crud = CRUD()

        # Método de inicio
        crud.main()

    except MySQLdb.OperationalError, e:
        print '\n'
        print u'Error de base de datos: '
        print '\n\t', e, '\n'

#    except Exception, e:
#        print '\n'
#        print u'Error inesperado: '
#        print '\n\t', e, '\n'
