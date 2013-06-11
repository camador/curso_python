#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

class DB():
    """
        Gestiona las operaciones con la base de datos
    """

    # Datos de conexión
    SERVIDOR = 'localhost'
    USUARIO = 'gemas'
    PASSWORD = 'gemas'
    BASEDATOS = 'gemas_camador'

    def __init__(self):
        """
            Crea la conexión con la base de datos y el cursor para operar con ella.
        """

        try:

            # Conexión a la base de datos
            self.db = MySQLdb.connect(host = self.SERVIDOR, user = self.USUARIO, passwd = self.PASSWORD, db = self.BASEDATOS)

            # Creación del cursor
            self.cursor = self.db.cursor(MySQLdb.cursors.DictCursor)

        except MySQLdb.OperationalError, e:
            print '\n'
            print u'Error de base de datos: '
            print '\n\t', e, '\n'

    ##
    ## CONFIG
    ##
    def get_config(self, clave):
        """
            Devuelve el valor de configuración correspondiente a la clave recibida por parámetros
        """

        consulta = 'select valor from config where clave = "{0}";'.format(clave)

        self.cursor.execute(consulta)
        registro = self.cursor.fetchone()
        
        return registro['valor']

    def set_config(self, clave, valor):
        """
            Actualiza el valor de configuración de la clave recibida por parámetros
        """

        update = 'update config set valor = "{0}" where clave = "{1}";'.format(valor, clave)
    
        self.cursor.execute(update)
        self.db.commit()

    ##
    ## RESOLUCIONES
    ##


if __name__ == '__main__':
    print u'Módulo no ejecutable.'
