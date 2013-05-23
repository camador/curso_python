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
                    'onMainWindowDestroy': self.main_window_destroy,
                    'onImagemenuitemSalirActivate': self.main_window_destroy,
                    'onToolbuttonSalirClicked': self.main_window_destroy,

                    'onImagemenuitemAboutActivate': self.ayuda_about,
                    'onToolbuttonAboutClicked': self.ayuda_about,

                    'onImagemenuitemDCrearActivate': self.on_crear,
                    'onToolbuttonDCrearClicked': self.on_crear,

                    'onImagemenuitemDObtenerActivate': self.on_obtener,
                    'onToolbuttonDObtenerClicked': self.on_obtener,

                    'onImagemenuitemDActualizarActivate': self.on_actualizar,
                    'onToolbuttonDActualizarClicked': self.on_actualizar,

                    'onImagemenuitemDBorrarActivate': self.on_borrar,
                    'onToolbuttonDBorrarClicked': self.on_borrar
                   }

        # Conecta las señales con las acciones (callbacks)
        self.builder.connect_signals(handlers)

        # Ventana principal
        self.window = self.builder.get_object("mainWindow")

        # Barra de estado
        self.status = self.builder.get_object('mainStatusBar')
        self.status_context_id = self.status.get_context_id('main')

        # Selección de ID
        self.list_store_IDs = self.builder.get_object('liststoreIDs')
        self.combo_box_IDs = self.builder.get_object('comboboxIDs')

        # Campos de edición
        self.entryCampo1 = self.builder.get_object('entryCampo1')
        self.entryCampo2 = self.builder.get_object('entryCampo2')
        self.entryCampo3 = self.builder.get_object('entryCampo3')
        self.entryCampo4 = self.builder.get_object('entryCampo4')
        self.entryCampo5 = self.builder.get_object('entryCampo5')

        # Gestor de base de datos
        self.db = crudDB()


    def main(self):
        """
            Método de inicio
        """

        # Muestra la ventana principal
        self.window.show_all()

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

    def rellena_comboboxIDs(self):
        """
            Rellena el combobox para las IDs
        """

        # Limpia el liststore
        self.limpia_comboboxIDs()

        # Recupera los IDs de la tabla
        registros = self.db.get_ids()

        # Llena el combobox con los IDs, si es que hay alguno
        if len(registros) > 0:

            for registro in registros:
                self.list_store_IDs.append([registro['id']])

            # Limpia la selección de elementos
            self.combo_box_IDs.set_active(0)

        else:
            # La tabla no tiene registros
            # Informa al usuario
            self.status.push(self.status_context_id, 'La tabla está vacía')

    def limpia_comboboxIDs(self):
        """
            Vacía el combobox para las IDs     
        """

        # Limpia el listsotre
        self.list_store_IDs.clear()

    def on_crear(self, *args):
        """
            Prepara la creación de un nuevo registro
        """
        # Limpia combobox de las IDs
        self.limpia_comboboxIDs()

        # Situa el foco en el primer campo
        self.entryCampo1.grab_focus()
        
        # Instrucciones para el usuario
        self.status.push(self.status_context_id, 'Introduzca los datos para el nuevo registro')

    def on_obtener(self, *args):
        self.rellena_comboboxIDs()
        self.combo_box_IDs.grab_focus()

        self.status.push(self.status_context_id, 'Pulsado Obtener')
    
    def on_actualizar(self, *args):
        self.rellena_comboboxIDs()
        self.combo_box_IDs.grab_focus()

        self.status.push(self.status_context_id, 'Pulsado Actualizar')

    def on_borrar(self, *args):
        self.rellena_comboboxIDs()
        self.combo_box_IDs.grab_focus()

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
