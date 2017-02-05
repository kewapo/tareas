'''
Operaciones sobre tareas.
Comandos disponibles:
    sin argumentos: lista las tareas de hoy.
    A "mi tarea1" "mi tarea2".- Añade las tareas con el texto indicado.
    B n1 n2 n3.- Borrar las tarea números n1, n2, n3...
    L.- Listar las tareas pendientes.
    L criterio.- Listar las tareas que contengan "criterio".
    LT.- Listar todas.
    LX.- Listar completadas.
    C n1 n2 n3.- Completar las tareas número n1 n2, n3...
    X n que_cambia.- Modificar el elemento correspondiente((P), @, +, #, ##, !) de la tarea n
También funciona con los comandos "Listar", "Añadir" "Completar" y "Borrar"
'''

import sys
import operaciones

if len(sys.argv) > 2:
    criterio = sys.argv[2]
else:
    criterio = ''

if len(sys.argv) == 1:
    operaciones.listar_tareas(que='hoy')
else:
    if sys.argv[1].upper() == 'LX': #Listar completas + con filtro
        operaciones.listar_tareas(que='completas', criterio=criterio)
    elif sys.argv[1].upper() == 'LT': #Listar todas ordenadas por prioridad
        operaciones.listar_tareas(que='todas')
    elif sys.argv[1][0].upper() == 'L':  # Listar pendientes + con filtro
        operaciones.listar_tareas(que='pendientes', criterio=criterio)
    elif sys.argv[1][0].upper() == 'A': #Añadir
        operaciones.aniade_tarea()
    elif sys.argv[1][0].upper() == 'B': #Borrar
        operaciones.borra_tarea()
    elif sys.argv[1][0].upper() == 'C': #Completar
        operaciones.completar_tarea()
    elif sys.argv[1].upper() == 'X' and len(sys.argv) > 3: #Cambiar
        operaciones.cambiar_tarea(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
