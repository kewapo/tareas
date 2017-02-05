import os
import control_tareas


class FicheroTareas():
    manejador_fichero = None

    def abrir(self):
        try:
            self.manejador_fichero = open('todo.txt', 'r+')
        except FileNotFoundError:
            self.manejador_fichero = open('todo.txt', 'w+')
            self.manejador_fichero.close()
            self.manejador_fichero = open('todo.txt', 'r+')
        except:
           print('No puedo abrir el fichero de tareas')
           exit()

    def cerrar(self):
        self.manejador_fichero.close()
        print('Fichero cerrado')

    def anadir(self):
        self.manejador_fichero.seek(0, 2)
        tarea = input('texto de la tarea: ')
        self.manejador_fichero.write(tarea + '\n')

    def borrar(self):
        try:
            linea_a_borrar = int(input('que tarea quieres borrar: '))
        except:
            print('Debes introducir un número')
            return
        self.manejador_fichero.seek(0)
        contenido = self.manejador_fichero.readlines()
        self.manejador_fichero.seek(0)
        self.manejador_fichero.truncate(0)
        i = 0
        for linea in contenido:
            i += 1
            if i != linea_a_borrar:
                self.manejador_fichero.write(linea)

    def listar(self):
        os.system('cls')
        print('TAREAS DEL FICHERO')
        print('------------------')
        self.manejador_fichero.seek(0)
        i = 1
        for line in self.manejador_fichero:
            print(str(i), line.strip())
            lista_tarea = control_tareas.extrae(line.strip())
            print('    Prioridad: ' + str(lista_tarea[0]))
            print('    Tarea: ' + str(lista_tarea[1]))
            print('    Contexto: ' + str(lista_tarea[2]))
            print('    Persona: ' + str(lista_tarea[3]))
            print('    Proyecto: ' + str(lista_tarea[4]))
            print('    Responsabilidad: ' + str(lista_tarea[5]))
            print('    Fecha: ' + str(lista_tarea[6]))

            i += 1
        print()
        print()

    def modificar(self):
        try:
            linea_a_cambiar = int(input('que tarea quieres cambiar: '))
        except:
            print('Debes introducir un número')
            return
        cambio = input('Teclea lo que cambia: ')

        self.manejador_fichero.seek(0)
        contenido = self.manejador_fichero.readlines()
        self.manejador_fichero.seek(0)
        self.manejador_fichero.truncate(0)
        i = 0
        for linea in contenido:
            i += 1
            if i != linea_a_cambiar:
                self.manejador_fichero.write(linea)
            else:
                self.manejador_fichero.write(control_tareas.cambia(linea, cambio))


    def fin(self):
        print()
        print('Gracias por su visita')
        self.cerrar()
        exit()

    def lanzar(self, opcion):
        opcion()
