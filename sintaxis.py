import re


def sin_nulos(elemento):
    if elemento is None:
        return ''
    else:
        return elemento.group(1)


def extrae_elementos(de_donde):
    a_devolver = []
    for tarea in de_donde:
        finalizada = sin_nulos(re.search(r'(\[X\])', tarea))
        prioridad = sin_nulos(re.search(r'(\([A-Z]\))', tarea))
        contexto = sin_nulos(re.search(r'(@\w+)', tarea))
        persona = sin_nulos(re.search(r'(\+\w+)', tarea))
        proyecto = sin_nulos(re.search(r' (#\S+)', tarea))
        responsabilidad = sin_nulos(re.search(r'(##\S+)', tarea))
        fecha = sin_nulos(re.search(r'(!(.+))', tarea))
        if prioridad != '':
            comienzo = r'\)'
        elif finalizada != '':
            comienzo = r'\]'
        else:
            comienzo = ''
        #patron = comienzo + r'([\w ]+)'
        patron = comienzo + r'(.+?)([@#+!]|$)'
        desc_tarea = sin_nulos(re.search(patron, tarea)).strip()
        a_devolver.append([finalizada, prioridad, desc_tarea, contexto, persona, proyecto, responsabilidad, fecha, tarea])
    return a_devolver

#Esta función no se usa. Está para hacer pruebas con las expresiones regulares.
def extrae_elemento(de_donde):
    finalizada = sin_nulos(re.search(r'(\[X\])', de_donde))
    prioridad = sin_nulos(re.search(r'(\([A-Z]\))', de_donde))
    contexto = sin_nulos(re.search(r'(@\w+)', de_donde))
    persona = sin_nulos(re.search(r'(\+\w+)', de_donde))
    proyecto = sin_nulos(re.search(r' (#\S+)', de_donde))
    responsabilidad = sin_nulos(re.search(r'(##\S+)', de_donde))
    fecha = sin_nulos(re.search(r'(!(.+))', de_donde))
    patron = r'(^\[X\]\s?\(.\)\s?|^\[X\]\s?|^\(.\)\s?|^)(.+?)([@#+!]|$)'
    print('--- ' + re.search(patron, de_donde).group(2))
    tarea = sin_nulos(re.search(patron, de_donde)).strip()
    a_devolver = [finalizada, prioridad, tarea, contexto, persona, proyecto, responsabilidad, fecha]
    return a_devolver
