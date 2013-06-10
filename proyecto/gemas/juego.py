#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Base de datos
from lib.db import DB

# Juego
from lib.config import Config

def main():

    # Gestor de base de datos
    db = DB()

    # Carga los valores de configuración
    config = Config(db)

    return 0

if __name__ == '__main__':
    main()
