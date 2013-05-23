#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Construye un patrón que coincida con una fecha con la siguiente estructura:
#
# Granada 5/Ago/2012 2:23 AM
#
# Algunas aclaraciones:
#
#   - El patrón debe reconocer Granada, San Sebastián o cualquier otra posible 
#     ciudad (No usaremos signos de puntuación ni guiones en los nombres de ciudad, pero sí espacios)
#   - El día, la hora o los minutos pueden tener uno o dos caracteres
#   - El mes se representa por sus tres primeras letras.
#   - No debe reconocer meses que no existan.
#   - El año debe ser de cuatro dígitos y mayor o igual que 2000.
#   - Tras la hora irá indicado AM o PM 
#

import re

cadenas = [
           'Granada 5/Ago/2012 2:23 AM',
           'San Sebastian 5/Ago/2012 2:23 AM',
           'San Saltarin del Monte 5/Ago/2012 2:23 AM',

           '1Granada 5/Ago/2012 2:23 AM',
           'San .Sebastian 5/Ago/2012 2:23 AM',
           'San Saltarin del Monte1 5/Ago/2012 2:23 AM',

           'Granada 05/Ago/2012 2:23 AM',
           'Granada 005/Ago/2012 2:23 AM',
           'San Sebastian 05/Ago/2012 2:23 AM',
           'San Sebastian a05/Ago/2012 2:23 AM',

           'Granada 5/Ago/2012 02:23 AM',
           'Granada 5/Ago/2012 2:3 AM',
           'San Sebastian 5/Ago/2012 002:23 AM',
           'San Sebastian 05/Ago/2012 : AM',
           'San Sebastian 05/Ago/2012 0: AM',
           'San Sebastian 05/Ago/2012 :0 AM',

           'Granada 5/ago/2012 2:23 AM',
           'Granada 5/AGO/2012 2:23 AM',
           'Granada 5/AGo/2012 2:23 AM',
           'Granada 5/Agoo/2012 2:23 AM',
           'Granada 5/1Ago/2012 2:23 AM',
           'Granada 5/Ago1/2012 2:23 AM',
           'Granada 5/ Ago/2012 2:23 AM',
           'Granada 5/Ago /2012 2:23 AM',

           'Granada 5/ene/2012 2:23 AM',
           'Granada 5/Ene/2012 2:23 AM',
           'Granada 5/ENE/2012 2:23 AM',
           'Granada 5/eNE/2012 2:23 AM',
           'Granada 5/enE/2012 2:23 AM',
           'Granada 5/EnE/2012 2:23 AM',
           'Granada 5/eNe/2012 2:23 AM',
           'Granada 5/feb/2012 2:23 AM',
           'Granada 5/mar/2012 2:23 AM',
           'Granada 5/may/2012 2:23 AM',
           'Granada 5/jun/2012 2:23 AM',
           'Granada 5/jul/2012 2:23 AM',
           'Granada 5/ago/2012 2:23 AM',
           'Granada 5/sep/2012 2:23 AM',
           'Granada 5/oct/2012 2:23 AM',
           'Granada 5/nov/2012 2:23 AM',
           'Granada 5/dic/2012 2:23 AM',
           'Granada 5/otr/2012 2:23 AM',
           
           'Granada 5/Ago/199 2:23 AM',
           'Granada 5/Ago/200 2:23 AM',
           'Granada 5/Ago/1999 2:23 AM',
           'Granada 5/Ago/2000 2:23 AM',
           'Granada 5/Ago/2001 2:23 AM',
           'Granada 5/Ago/3000 2:23 AM',
           'Granada 5/Ago/9999 2:23 AM',
           'Granada 5/Ago/10000 2:23 AM',
           'Granada 5/Ago/20000 2:23 AM',

           'Granada 5/Ago/2012 2:23 AM',
           'Granada 5/Ago/2012 2:23 PM',
           'Granada 5/Ago/2012 2:23 am',
           'Granada 5/Ago/2012 2:23 pm',
           'Granada 5/Ago/2012 2:23 Pm',
           'Granada 5/Ago/2012 2:23 pM',
           'Granada 5/Ago/2012 2:23 ',
           'Granada 5/Ago/2012 2:23 a',
           'Granada 5/Ago/2012 2:23 p',
           'Granada 5/Ago/2012 2:23 m',
           'Granada 5/Ago/2012 2:23 mm',
           'Granada 5/Ago/2012 2:23 mp',
           'Granada 5/Ago/2012 2:23 bm',
          ]

patron = '^[a-zA-Z ]+ \d{1,2}/(([eE]ne|ENE)|([fB]eb|FEB)|([mM]a[ry]|MA[RY])|([aA]br|ABR)|([jJ]u[nl]|JU[NL])|([aA]go|AGO)|([sS]ep|SEP)|([oO]ct|OCT)|([nN]ov|NOV)|([dD]ic|DIC))/[2-9]\d{3} \d{1,2}:\d{1,2} (AM|PM|am|pm)$'

# Comprueba todas las cadenas
for cadena in cadenas:

  print 'Probando {0:.<45}'.format(cadena),

  if re.search(patron, cadena):
    print 'OK'
  else:
    print 'Fallo'
