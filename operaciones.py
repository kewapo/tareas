import sys
import datetime
from colorconsole import terminal
import sintaxis

pantalla = terminal.get_terminal()


def crear_fichero():
    mi_fichero = open('todo.txt', 'w')
    mi_fichero.close()
    print('No existe el fichero. Se crea en blanco. Prueba de nuevo.')


def fija_color(tarea):
    try:
        if tarea[0] == '[X]':
            pantalla.set_color(terminal.colors['DGRAY'])
        elif tarea[1] == '(A)':
            pantalla.set_color(terminal.colors['LRED'])
        elif tarea[1] == '(B)':
            pantalla.set_color(terminal.colors['YELLOW'])
        elif tarea[1] == '(C)':
            pantalla.set_color(terminal.colors['LGREEN'])
        else:
            pantalla.set_color(terminal.colors['WHITE'])
    except:
        pantalla.set_color(terminal.colors['WHITE'])


def imprime_lista(lista):
    if len(lista) == 0: print('No hay tareas')
    for tarea in lista:
        fija_color(tarea)
        print(str(tarea[-1]) + '. ', end='')
        for elemento in tarea[:-2]:
            if elemento != '': print(elemento, end=' ')
        print()
    pantalla.set_color(terminal.colors['WHITE'])


def listar_tareas(que='hoy', criterio=''):
    todas_tareas = sintaxis.extrae_elementos([line.strip() for line in open('todo.txt')])
    for indice, elemento in enumerate(todas_tareas):
        elemento.append(indice+ 1)
    if que == 'hoy':
        hoy = '{0:%d/%m/%Y}'.format(datetime.date.today())
        tareas = [tarea for tarea in todas_tareas if hoy in tarea[7]]
        print("Tareas para hoy, " + hoy)
        print('-----------------------------------------------')
        imprime_lista(tareas)
    elif que == 'pendientes':
        print('Tareas pendientes')
        print('-----------------------------------------------')
        tareas = [tarea for tarea in todas_tareas if not tarea[0].startswith('[X]') and criterio in tarea[8]]
        imprime_lista(tareas)
    elif que == 'todas':
        print('Todas las tareas del fichero')
        print('-----------------------------------------------')
        todas_tareas.sort(key=lambda f: f[1])
        todas_tareas.sort(key=lambda f: f[0])
        imprime_lista(todas_tareas)
    elif que == 'completas':
        print('Tareas finalizadas')
        print('-----------------------------------------------')
        tareas = [tarea for tarea in todas_tareas if tarea[0].startswith('[X]') and criterio in tarea[8]]
        imprime_lista(tareas)


def aniade_tarea():
    try:
        tareas = [linea.strip() for linea in open('todo.txt')]
        fichero = open('todo.txt', 'w')
        for indice, tarea in enumerate(tareas):
            if '[X]' not in tarea: fichero.write(tarea + '\n')
        for argumento_tarea in sys.argv[2:]:
            fichero.write(argumento_tarea + "\n")
            print('tarea ' + argumento_tarea + ' añadida')
        for indice, tarea in enumerate(tareas):
            if '[X]' in tarea: fichero.write(tarea + '\n')
    except FileNotFoundError:
            crear_fichero()
    except:
        print('No he podido añadir la tarea, prueba de nuevo.')


def borra_tarea():
    try:
        tareas = [linea.strip() for linea in open('todo.txt')]
        fichero = open('todo.txt', 'w')
        borrar_lista = [int(arg) - 1 for arg in sys.argv[2:]]
        for indice, tarea in enumerate(tareas):
            if indice in borrar_lista:
                print('Tarea ' + tarea + ' borrada')
                continue
            fichero.write(tarea + '\n')
    except FileNotFoundError:
            crear_fichero()
    except:
        print('No he podido borrar la tarea')


def completar_tarea():
    try:
        tareas = [linea.strip() for linea in open('todo.txt')]
        fichero = open('todo.txt', 'w')
        completar_lista = [int(arg) - 1 for arg in sys.argv[2:]]
        for indice, tarea in enumerate(tareas):
            if (indice not in completar_lista) and ('[X]' not in tarea):
                fichero.write(tarea + '\n')
        for indice, tarea in enumerate(tareas):
            if indice in completar_lista:
                fichero.write('[X] ' + tarea + '\n')
                print('Completando la tarea ' + tarea)
            if '[X]' in tarea:
                fichero.write(tarea + '\n')
    except FileNotFoundError:
                crear_fichero()
    except:
        print('No he podido completar la tarea')


def cambiar_tarea(numero, que_cambia):
    try:
        todas_tareas = sintaxis.extrae_elementos([linea.strip() for linea in open('todo.txt')])
        fichero = open('todo.txt', 'w')
        for indice, tarea in enumerate(todas_tareas):
            if (int(numero) - 1) == indice:
                if que_cambia.startswith('('):
                    if len(que_cambia) == 1:
                        tarea[1] = ''
                    else:
                        tarea[1] = que_cambia
                elif que_cambia.startswith('@'):
                    if len(que_cambia) == 1:
                        tarea[3] = ''
                    else:
                        tarea[3] = que_cambia
                elif que_cambia.startswith('##'):
                    if len(que_cambia) == 2:
                        tarea[6] = ''
                    else:
                        tarea[6] = que_cambia
                elif que_cambia.startswith('#'):
                    if len(que_cambia) == 1:
                        tarea[5] = ''
                    else:
                        tarea[5] = que_cambia
                elif que_cambia.startswith('+'):
                    if len(que_cambia) == 1:
                        tarea[4] = ''
                    else:
                        tarea[4] = que_cambia
                elif que_cambia.startswith('!'):
                    if len(que_cambia) == 1:
                        tarea[7] = ''
                    else:
                        tarea[7] = que_cambia
                else:
                    if len(que_cambia) == 1:
                        tarea[2] = ''
                    else:
                        tarea[2] = que_cambia
                print(tarea)
            for elemento in tarea[:-1]:
                if elemento == '': continue
                fichero.write(elemento + ' ')
            fichero.write('\n')
    except:
        print('No puedo cambiar la tarea')
