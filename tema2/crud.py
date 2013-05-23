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
                    'onToolbuttonDBorrarClicked': self.on_borrar,

                    'onButtonConfirmacionCrearActivate': self.on_crear_confirmacion,
                    'onButtonConfirmacionActualizarActivate': self.on_actualizar_confirmacion,
                    'onButtonConfirmacionBorrarActivate': self.on_borrar_confirmacion
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

        # Identificador de la señal 'changed' del combobox (inicialmente a None)
        self.combo_box_IDs_changed_signal = None

        # Campos de edición
        self.entry_ID = self.builder.get_object('entryID')
        self.entry_campo1 = self.builder.get_object('entryCampo1')
        self.entry_campo2 = self.builder.get_object('entryCampo2')
        self.entry_campo3 = self.builder.get_object('entryCampo3')
        self.entry_campo4 = self.builder.get_object('entryCampo4')
        self.entry_campo5 = self.builder.get_object('entryCampo5')

        # Botones de confirmación
        self.button_confirmacion_Crear = self.builder.get_object('buttonConfirmacionCrear')
        self.button_confirmacion_Actualizar = self.builder.get_object('buttonConfirmacionActualizar')
        self.button_confirmacion_Borrar = self.builder.get_object('buttonConfirmacionBorrar')

        # Gestor de base de datos
        self.db = crudDB()

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
    def main_window_destroy(self, window):
        """
            Termina la ejecución del programa
        """

        # Cierra los objetos de la base de datos
        self.db.close()

        # Saliendo
        Gtk.main_quit()
    

    ##
    ## ACERCA DE
    ##
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

    ##
    ## COMBOBOX
    ##
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

            # Primer elemento no válido para poder detectar la selección del primer ID
            # con la señal 'changed'
            self.list_store_IDs.append(['--'])

            for registro in registros:
                self.list_store_IDs.append([str(registro['id'])])

            # Establece el primer elemento como activo
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

    def get_id_seleccionado(self):
        """
            Devuelve el ID seleccionado por el usuario mediante el comboboxIDs
        """
    
        # Elemento seleccionado
        item = self.combo_box_IDs.get_active() 

        # Lista de IDs del combobox
        lista_ids = self.combo_box_IDs.get_model()
        
        # Devuelve el ID asociado al elemento seleccionado
        return(lista_ids[item][0])

    ##
    ## BOTONES DE CONFIRMACIÓN
    ##
    def oculta_botones_confirmacion(self):
        """
            Oculta todos los botones de confirmación
        """
        self.button_confirmacion_Actualizar.hide()
        self.button_confirmacion_Borrar.hide()
        self.button_confirmacion_Crear.hide()

    ##
    ## ENTRYBOXES 
    ##
    def rellena_campos(self, registro):
        """
            Rellena los entryboxes con los datos del registro recibido como parámetro
        """
        self.entry_ID.set_text(str(registro['id']))
        self.entry_campo1.set_text(registro['campo1'])
        self.entry_campo2.set_text(registro['campo2'])
        self.entry_campo3.set_text(registro['campo3'])
        self.entry_campo4.set_text(registro['campo4'])
        self.entry_campo5.set_text(str(registro['campo5']))

    def limpia_campos(self):
        """
            Limpia los entryboxes para los datos
        """
        self.entry_ID.set_text('')
        self.entry_campo1.set_text('')
        self.entry_campo2.set_text('')
        self.entry_campo3.set_text('')
        self.entry_campo4.set_text('')
        self.entry_campo5.set_text('')

    ##
    ## CREAR
    ##
    def on_crear(self, *args):
        """
            Prepara la creación de un nuevo registro
        """
        # Limpia combobox de las IDs
        self.limpia_comboboxIDs()

        # Situa el foco en el primer campo
        self.entry_campo1.grab_focus()

        # Oculta los botones de confirmación y muestra el correspondiente a esta acción 
        self.button_confirmacion_Actualizar.hide()
        self.button_confirmacion_Borrar.hide()
        self.button_confirmacion_Crear.show()
        
        # Instrucciones para el usuario
        self.status.push(self.status_context_id, 'Introduzca los datos para el nuevo registro')

    ##
    ## OBTENER
    ##
    def on_obtener(self, *args):
        """
            Prepara la obtención de un registro
        """

        # Desconecta la señal changed previamente asignada, si había alguna
        if self.combo_box_IDs_changed_signal is not None:
            self.combo_box_IDs.disconnect(self.combo_box_IDs_changed_signal)

        # Carga los IDs de la tabla en el combobox y fija el foco en él
        self.rellena_comboboxIDs()
        self.combo_box_IDs.grab_focus()

        # Oculta los botones de confirmación porque en esta acción no hay nada que confirmar
        self.oculta_botones_confirmacion()

        # Establece la acción a realizar tras la selección del ID
        self.combo_box_IDs_changed_signal = self.combo_box_IDs.connect('changed', self.on_obtener_registro)

        # Instrucciones para el usuario
        self.status.push(self.status_context_id, 'Seleccione el registro a mostrar')

    def on_obtener_registro(self, combo):
        """
            Recupera el registro seleccionado por el usuario y rellena los entryboxes
            con él
        """

        # Recupera el ID
        id = self.get_id_seleccionado() 

        # Si es un ID válido lo recupera y rellena los campos con él
        if id != '--':

            registro = self.db.get_registro(id)
            self.rellena_campos(registro)

            # Limpia la barra de estado
            self.status.push(self.status_context_id, '')
            
        else:
            # El ID no es válido

            # Limpia los campos
            self.limpia_campos()

            # Informa al usuario
            self.status.push(self.status_context_id, 'Por favor, seleccione un ID válido')
    
    ##
    ## ACTUALIZAR
    ##
    def on_actualizar(self, *args):
        """
            Prepara la actualización de un registro
        """
        # Desconecta la señal changed previamente asignada, si había alguna
        if self.combo_box_IDs_changed_signal is not None:
            self.combo_box_IDs.disconnect(self.combo_box_IDs_changed_signal)

        # Carga los IDs de la tabla en el combobox y fija el foco en él
        self.rellena_comboboxIDs()
        self.combo_box_IDs.grab_focus()

        # Oculta los botones de confirmación
        self.oculta_botones_confirmacion()

        # Establece la acción a realizar tras la selección del ID
        self.combo_box_IDs_changed_signal = self.combo_box_IDs.connect('changed', self.on_actualizar_registro)

        # Instrucciones para el usuario
        self.status.push(self.status_context_id, 'Seleccione el registro a actualizar')

    def on_actualizar_registro(self, combo):
        """
            Recupera el registro seleccionado por el usuario, rellena los entryboxes
            con él y muestra el botón 'Actualizar'
        """

        # Recupera el ID
        id = self.get_id_seleccionado() 

        # Si es un ID válido lo recupera y rellena los campos con él
        if id != '--':

            registro = self.db.get_registro(id)
            self.rellena_campos(registro)
            
            # Muestra el botón de confirmación
            self.button_confirmacion_Actualizar.show()

            # Limpia la barra de estado
            self.status.push(self.status_context_id, 'Pulse Actualizar para guardar los cambios')
            
        else:
            # El ID no es válido

            # Limpia los campos
            self.limpia_campos()

            # Informa al usuario
            self.status.push(self.status_context_id, 'Por favor, seleccione un ID válido')

    ##
    ## BORRAR
    ##
    def on_borrar(self, *args):
        """
            Prepara la eliminación de un registro
        """

        # Desconecta la señal changed previamente asignada, si había alguna
        if self.combo_box_IDs_changed_signal is not None:
            self.combo_box_IDs.disconnect(self.combo_box_IDs_changed_signal)

        # Carga los IDs de la tabla en el combobox y fija el foco en él
        self.rellena_comboboxIDs()
        self.combo_box_IDs.grab_focus()

        # Oculta los botones de confirmación
        self.oculta_botones_confirmacion()

        # Establece la acción a realizar tras la selección del ID
        self.combo_box_IDs.connect('changed', self.on_borrar_registro)

        # Instrucciones para el usuario
        self.status.push(self.status_context_id, 'Seleccione el registro a eliminar')

    def on_borrar_registro(self, combo):
        """
            Recupera el registro seleccionado por el usuario, rellena los entryboxes
            con él y muestra el botón 'Borrar'
        """

        # Recupera el ID
        id = self.get_id_seleccionado() 

        # Si es un ID válido lo recupera y rellena los campos con él
        if id != '--':

            registro = self.db.get_registro(id)
            self.rellena_campos(registro)
            
            # Muestra el botón de confirmación
            self.button_confirmacion_Borrar.show()

            # Limpia la barra de estado
            self.status.push(self.status_context_id, 'Pulse Borrar para eliminar el registro')
            
        else:
            # El ID no es válido

            # Limpia los campos
            self.limpia_campos()

            # Informa al usuario
            self.status.push(self.status_context_id, 'Por favor, seleccione un ID válido')

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
    
    def get_registro(self, id):
        """
            Recupera y devuelve el registro con el id recibido como parámetro
        """

        self.cursor.execute('select * from crud where id = {0};'.format(id)) 
        return(self.cursor.fetchone())
    

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
