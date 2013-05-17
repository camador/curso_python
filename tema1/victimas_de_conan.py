#!/bin/env python
# -*- coding: utf-8 -*-


# Descripción del ejercicio:
#
# Escribe un programa que, basándose en los datos del ejemplo anterior, rellene automáticamente una base 
# de datos de víctimas de Conan con 10 ejemplos y, además, permita introducir un nuevo registro y mostrar
# los que ya hay.
# 
# Para no dar ventaja a ningún alumno, no deben usare más características de SQL que las aquí vistas.
#
# Al iniciar el programa, este creará 10 registros automáticamente
#
# Después, irá pidiendo datos al usuario: Nombre, Profesion y Muerte (salvo id, que deberá ser generado 
# automáticamente)
#
# El valor del campo id no debe repetirse (y esto debe controlarlo Python, no por medio de las 
# características de MySQL)
# No es necesario que se pueda introducir más de un registro en cada ejecución del programa, pero se 
# valorará que lo haga.
#
# Si se introduce un valor en blanco para cualquier campo, no se efectuará el insert y se enviará al 
# usuario un aviso advirtiendo que no se ha hecho
#
# Se introduzca o nó un nuevo valor, al final se mostrará una tabla con los datos actualmente almacenados
#
# Por último, el programa NO debe borrar la tabla ni ningún dato. 


class gestorDB:
    """
        Gestión de la base de datos
    """

    # Interfaz MySQL
    import MySQLdb

    # Datos iniciales para la tabla
    registros_iniciales = [
                            {'Nombre': 'Ejercito de Zombies', 'Profesion': 'Muertos Vivientes', 'Muerte': 'Desmembramiento a espada'},
                            {'Nombre': 'Vampiro feo', 'Profesion': 'Muertos Vivientes', 'Muerte': 'Estaca de madera'},
                            {'Nombre': 'Bestia del Pantano', 'Profesion': 'Monstruo', 'Muerte': 'Destripado'},
                            {'Nombre': 'Serpiente', 'Profesion': 'Monstruo', 'Muerte': 'Destripado'},
                            {'Nombre': 'Sacerdote maligno', 'Profesion': 'Monstruo', 'Muerte': 'Desmembramiento a espada'},
                            {'Nombre': 'Abisario infernal', 'Profesion': 'Monstruo', 'Muerte': 'Estaca de madera'},
                            {'Nombre': 'Ocelote corrupto', 'Profesion': 'Monstruo', 'Muerte': 'Destripado'},
                            {'Nombre': 'Marea zergling', 'Profesion': 'Ejercito Zerg', 'Muerte': 'Desmembramiento a espada'},
                            {'Nombre': 'Invocador temerario', 'Profesion': 'Mago oscuro', 'Muerte': 'Destripado'},
                            {'Nombre': 'Jefe de proyecto', 'Profesion': 'Mago oscuro', 'Muerte': 'Estaca de madera'},
                        ]
    
    # Último ID calculado de la tabla 'Victimas'
    ultimo_id = 0

    def __init__(self):
        """
            Crea la conexión con la base de datos y el cursor para operar con ella. 
            
            Además, inserta los diez registros iniciales en la tabla 'Victimas'
        """

        # Conexión a la base de datos
        self.db = self.MySQLdb.connect(host='localhost', user='conan', passwd='crom', db='DBdeConan')

        # Creación del cursor
        self.cursor = self.db.cursor(self.MySQLdb.cursors.DictCursor)

        # Inserta los datos iniciales
        for registro in self.registros_iniciales:
            self.insert(registro)

    def insert(self, registro):
        """
            Inserta los valores recibidos en el parámetro 'registro' en la tabla 'Victimas'

            @param registro: dict - Valores para los campos 'Nombre', 'Profesion' y 'Muerte'
        """
        
        # El parámetro recibido ha de ser un diccionario
        if not isinstance(registro, dict):
            raise Exception('Error en gestorDB.insert(): Parámetro no válido: Se esperaba un diccionario.')

        # Los campos 'Nombre', 'Profesion' y 'Muerte' han de estar presentes y no estar vacíos
        campos_vacios = []
        if 'Nombre' not in registro or not registro['Nombre']:
            campos_vacios.append('Nombre')
            
        if 'Profesion' not in registro or not registro['Profesion']:
            campos_vacios.append('Profesion')

        if 'Muerte' not in registro or not registro['Muerte']:
            campos_vacios.append('Muerte')

        if len(campos_vacios) > 0:
            mensaje = 'Se encontraron campos obligatorios vacios: %s' % ', '.join(campos_vacios)
            raise InsertError(mensaje)
            
        # Realiza la inserción
        nuevo_id = self.__get_nuevo_id()
        insert = 'insert into Victimas values (%i, "%s", "%s", "%s");' % (nuevo_id, registro['Nombre'], registro['Profesion'], registro['Muerte'])
        self.cursor.execute(insert) 

        # Confirma la inserción
        self.db.commit()

    def get_list(self):
        """
            Devuelve todos los registros de la tabla 'Victimas'
        """

        self.cursor.execute('select * from Victimas')
        return(self.cursor.fetchall())

    #
    # Métodos privados
    #
    def __get_nuevo_id(self):
        """
            Devuelve el siguiente ID para la tabla 'Victimas'    

            El método de comprobación es muy rudimentario porque no se puede usar más SQL
            que el aprendido en el curso hasta el momento. Consiste en incrementar un contador
            hasta que encuentre un valor no existente en la tabla.
        """

        # Si el ultimo_id es 0 calcula el número de registros de la tabla para no hacer 
        # demasiado ineficiente el cálculo del siguiente ID en caso de que la tabla no esté
        # vacía
        if self.ultimo_id == 0:
            self.ultimo_id = self.cursor.execute('select id from Victimas;')

        #
        # Calcula el nuevo ID
        #

        # El siguiente ID es el último calculado más uno
        nuevo_id = self.ultimo_id + 1

        # Recalcula el ID hasta que encuentra uno válido
        encontrado = False 
        while not encontrado:

            # El nuevo ID no puede existir en la tabla
            if self.cursor.execute('select id from Victimas where id = ' + str(nuevo_id) + ';') == 0:
                # ID válido encontrado
                encontrado = True

            else:
                # Nuevo incremento
                nuevo_id += 1


        # Guarda el nuevo ID como el último utilizado
        self.ultimo_id = nuevo_id

        return(nuevo_id)


class InsertError(Exception):
    """
        Errores producidos en la inserción
    """

    def __init__(self, mensaje):
        self.mensaje = mensaje 

    def __str__(self):
        return(self.mensaje)

#############
#############
#############

# Menú de opciones
menu = ['1 - Nuevo registro', '2 - Listar registros', '0 - Salir']
opciones_validas = ['0', '1', '2']

print '\n'
print u'VÍCTIMAS DE CONAN'

# Opción del menú elegida por el usuario
opcion = ''

# Acaba cuando se pulsa la opción de salida
while opcion != '0':

    try:

        # En la primera iteración se instancia el gestor de la base de datos, lo que 
        # generará diez nuevas filas en la tabla 'Victimas'
        if opcion == '':
            db = gestorDB()

        # Imprime el menú
        print '\n'
        print u' Menú: '
        print u'-------'
        for elemento in menu:
            print elemento

        # Pide al usuario la operación a realizar 
        opcion = raw_input('\nSeleccione una opcion: ')
        print('\n')

        # Ejecuta la opción introducida por el usuario
        if opcion == '0':
            # Saliendo...
            print 'Hasta pronto ;-)\n'

        else:

            # Tanto la opción 1 como la 2 imprimen siempre la lista de registros, la única diferencia
            # es la inserción de la opción 1

            if opcion == '1':

                # Nuevo registro
                nuevo_registro = {}

                # Pide los datos al usuario
                print 'Por favor, introduzca los datos para el nuevo registro:'
                nuevo_registro['Nombre'] = raw_input('Nombre: ')
                nuevo_registro['Profesion'] = raw_input('Profesion: ')
                nuevo_registro['Muerte'] = raw_input('Muerte: ')

                # Realiza la inserción
                db.insert(nuevo_registro) 

                # Confirmación para el usuario
                print '\n'
                print 'Registro insertado correctamente'


            # Recupera los registros de la tabla 
            registros = db.get_list() 

            # La tabla tiene al menos diez registros (introducidos al instanciar gestorDB), así que
            # no es necesario comprobar el número de registros devueltos
            print '\n'
            print 'LISTADO DE REGISTROS'
            print '\n'
            print u'  id | Nombre               | Profesión            | Muerte'
            print u'-----+----------------------+----------------------+----------------------'

            # Imprime el listado con el siguiente formato:
            #   - id: alineación a la derecha con relleno de espacios, con un tamaño mínimo de 4 
            #   - resto de campos: tamaño mínimo de 20
            for registro in registros:
                # Para que la tabla no se descuadre hay que limitar el tamaño de los registros
                for campo in registro.keys():
                    if campo != 'id' and len(registro[campo]) > 20:
                        registro[campo] = registro[campo][0:17] + '...'

                print '{0[id]:> 4} | {0[Nombre]:20} | {0[Profesion]:20} | {0[Muerte]:20}'.format(registro)

            print u'-----+----------------------+----------------------+----------------------'

    
    except InsertError, e:
        print '\n'
        print u'Error al insertar: '
        print '\n\t' , e, '\n'

    except Exception, e:
        print '\n'
        print u'Error inesperado: '
        print '\n\t' , e, '\n'
        
        # Termina la ejecución del programa
        opcion = '0'
