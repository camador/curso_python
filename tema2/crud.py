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
                    'ayudaAbout': self.ayuda_about,
                    'onMenuitemDCrearActivate': self.on_crear,
                    'onToolbuttonDCrearClicked': self.on_crear,
                    'onMenuitemDObtenerActivate': self.on_obtener,
                    'onToolbuttonDObtenerClicked': self.on_obtener,
                    'onMenuitemDActualizarActivate': self.on_actualizar,
                    'onToolbuttonDActualizarClicked': self.on_actualizar,
                    'onMenuitemDBorrarActivate': self.on_borrar,
                    'onToolbuttonDBorrarClicked': self.on_borrar
                   }

        # Conecta las señales con las acciones (callbacks)
        self.builder.connect_signals(handlers)

        # Gestor de base de datos
        self.db = crudDB()


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

        # Recupera los IDs de la tabla
        registros = self.db.get_ids()

        # Llena el combobox con los IDs, si es que hay alguno
        if len(registros) > 0:

            # Informa al usuario del nº de registros encontrados 
            self.status.push(self.status_context_id, 'Leídos {0} registro/s'.format(len(registros)))

            list_store_IDs = self.builder.get_object('liststoreIDs')
            for registro in registros:
                list_store_IDs.append([registro['id']])

            # Limpia la selección de elementos
            combo_box_IDs = self.builder.get_object('comboboxIDs')
            combo_box_IDs.set_active(0)

        else:
            # La tabla no tiene registros
            # Informa al usuario
            self.status.push(self.status_context_id, 'La tabla está vacía')


        # A la espera de evento
        Gtk.main()


    def main_window_destroy(self, window):
        """
            Termina la ejecución del programa
        """

        # Cierra los objetos de la base de datos
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

    def on_crear(self, *args):
        self.status.push(self.status_context_id, 'Pulsado Crear')

    def on_obtener(self, *args):
        self.status.push(self.status_context_id, 'Pulsado Obtener')
    
    def on_actualizar(self, *args):
        self.status.push(self.status_context_id, 'Pulsado Actualizar')

    def on_borrar(self, *args):
        self.status.push(self.status_context_id, 'Pulsado Borrar')


class crudDB():
    """
        Se encarga de todas las operaciones con la base de datos 'crud_camador'

        Dicha base de datos ha de existir en localhost, tener el usuario 'crud_camador'
        con todos los permisos sobre ella y el password 'crud'.

        La única tabla se llama 'crud'
    """

    def __init__(self):
        """
            Conecta con la base de datos y crea un cursor
        """

        # Conexión a la base de datos
        self.db = MySQLdb.connect(host = 'localhost', user = 'crud_camador', passwd = 'crud', db = 'crud_camador')

        # Crea el cursor
        self.cursor = self.db.cursor(MySQLdb.cursors.DictCursor)

    def get_ids(self):
        """
            Recupera todos los IDs de la tabla        
        """

        # Recupera los IDs de la tabla
        self.cursor.execute('select id from crud order by id;')
        return(self.cursor.fetchall())

    def close(self):
        """
            Cierra el cursor y la conexión
        """

        # Cierra cursor y conexión de la base de datos
        self.cursor.close()
        self.db.close()
    
    

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

    except Exception, e:
        print '\n'
        print u'Error inesperado: '
        print '\n\t', e, '\n'
