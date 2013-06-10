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

if __name__ == '__main__':
    print u'Módulo no ejecutable.'
