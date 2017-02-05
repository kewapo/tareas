from fichero_tareas import FicheroTareas

mi_fichero = FicheroTareas()
menu = ['Listar tareas',
        'Añadir tarea',
        'Borrar tarea',
        'Modificar tarea',
        'Fin']
funciones = [mi_fichero.listar,
             mi_fichero.anadir,
             mi_fichero.borrar,
             mi_fichero.modificar,
             mi_fichero.fin]


def imprime_menu():
    print('Elige una opción')
    print('----------------')
    for item in menu:
        print(str(menu.index(item) + 1) + ' - ' + item)


def pregunta_opcion():
    try:
        i = int(input('opcion: '))
    except:
        return 1
    return i


def ejecuta_opcion(la_opcion):
    mi_fichero.lanzar(funciones[la_opcion - 1])


'''
---------------------------------------------------
Comienzo del programa
---------------------------------------------------
'''
mi_fichero.abrir()
mi_fichero.listar()

while True:
    imprime_menu()
    ejecuta_opcion(pregunta_opcion())
