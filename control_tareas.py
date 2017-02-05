import re


def elemento_extrae(elemento):
    if elemento is None:
        return None
    else:
        return elemento.group(1)


def extrae(de_donde):
    prioridad = elemento_extrae(re.search(r'\((A)\)', de_donde))
    contexto = elemento_extrae(re.search(r'(@\w+)', de_donde))
    persona = elemento_extrae(re.search(r'(\+\w+)', de_donde))
    proyecto = elemento_extrae(re.search(r' (#\w+)', de_donde))
    responsabilidad = elemento_extrae(re.search(r'(##\w+)', de_donde))
    fecha = elemento_extrae(re.search(r'!((.+))', de_donde))
    if prioridad != None:
        comienzo = r'\)'
    else:
        comienzo = ''
    patron = comienzo + r'([\w ]+)'
    tarea = elemento_extrae(re.search(patron, de_donde)).strip()

    return [prioridad, tarea, contexto, persona, proyecto, responsabilidad, fecha]


def cambia(tarea, cambio):
    return str.strip(tarea) + " - " + cambio


tarea = '(A) Recoger a los niños @casa +Javi  #niños ##familia !01/01/2017 11:00'
print(extrae(tarea))
