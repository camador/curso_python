#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base de datos
from lib.db import DB

# Juego
from lib.config import Config

def main():

    try :

        # Gestor de base de datos
        db = DB()

        # Carga los valores de configuración
        config = Config(db)

        return 0

    except Exception, e:
        print '\n'
        print u'Error inesperado: '
        print '\n\t', e, '\n'

if __name__ == '__main__':
    main()
