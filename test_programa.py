import unittest

import sintaxis


class Regular_Expresions_Test(unittest.TestCase):

    def test_pruebas(self):
        self.assertEqual(4 + 5, 9)

    def setUp(self):
        self.completa = 'X (B) Esta es la descripcion de la tarea @oficina #Responsabilidad ##Proyecto +Persona !01/01/2017 11:00'
        self.activa = '(B) Esta es la descripcion de la tarea @oficina #Responsabilidad ##Proyecto +Persona !01/01/2017 11:00'
        self.sin_prioridad = 'Esta es la descripcion de la tarea @oficina #Responsabilidad ##Proyecto +Persona !01/01/2017 11:00'
        self.completa_sin_prioridad = 'X Esta es la descripcion de la tarea @oficina #Responsabilidad ##Proyecto +Persona !01/01/2017 11:00'
        self.solo_descripcion = 'Esta es la descripcion de la tarea'
        self.sin_contexto = '(B) Esta es la descripcion de la tarea #Responsabilidad ##Proyecto +Persona !01/01/2017 11:00'
        self.sin_resonsabilidad = '(B) Esta es la descripcion de la tarea @oficina ##Proyecto +Persona !01/01/2017 11:00'
        self.sin_proyecto = '(B) Esta es la descripcion de la tarea @oficina #Responsabilidad +Persona !01/01/2017 11:00'
        self.sin_persona = '(B) Esta es la descripcion de la tarea @oficina #Responsabilidad ##Proyecto!01/01/2017 11:00'
        self.sin_fecha = '(B) Esta es la descripcion de la tarea  @oficina #Responsabilidad ##Proyecto +Persona'
        self.sin_hora = '(B) Esta es la descripcion de la tarea @oficina #Responsabilidad ##Proyecto +Persona !01/01/2017'
        self.descripcion_raros = 'X (B) Esta es la descripcion?.-  De la tarea @oficina #Responsabilidad ##Proyecto +Persona !01/01/2017 11:00'

    def test_completa(self):
        self.assertEqual(sintaxis.extrae_elemento(self.completa)[0], 'X')
        self.assertEqual(sintaxis.extrae_elemento(self.activa)[0], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_prioridad)[0], '')
        self.assertEqual(sintaxis.extrae_elemento(self.completa_sin_prioridad)[0], 'X')
        self.assertEqual(sintaxis.extrae_elemento(self.solo_descripcion)[0], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_contexto)[0], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_resonsabilidad)[0], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_proyecto)[0], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_persona)[0], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_fecha)[0], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_hora)[0], '')
        self.assertEqual(sintaxis.extrae_elemento(self.descripcion_raros)[0], 'X')

    def test_prioridad(self):
        self.assertEqual(sintaxis.extrae_elemento(self.completa)[1], '(B)')
        self.assertEqual(sintaxis.extrae_elemento(self.activa)[1], '(B)')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_prioridad)[1], '')
        self.assertEqual(sintaxis.extrae_elemento(self.completa_sin_prioridad)[1], '')
        self.assertEqual(sintaxis.extrae_elemento(self.solo_descripcion)[1], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_contexto)[1], '(B)')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_resonsabilidad)[1], '(B)')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_proyecto)[1], '(B)')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_persona)[1], '(B)')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_fecha)[1], '(B)')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_hora)[1], '(B)')
        self.assertEqual(sintaxis.extrae_elemento(self.descripcion_raros)[1], '(B)')

    def test_descripcion(self):
        self.assertEqual(sintaxis.extrae_elemento(self.completa)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.activa)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_prioridad)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.completa_sin_prioridad)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.solo_descripcion)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_contexto)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_resonsabilidad)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_proyecto)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_persona)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_fecha)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_hora)[2], 'Esta es la descripcion de la tarea')
        self.assertEqual(sintaxis.extrae_elemento(self.descripcion_raros)[2], 'Esta es la descripcion?.-  De la tarea')


    def test_contexto(self):
        self.assertEqual(sintaxis.extrae_elemento(self.completa)[3], '@oficina')
        self.assertEqual(sintaxis.extrae_elemento(self.activa)[3], '@oficina')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_prioridad)[3], '@oficina')
        self.assertEqual(sintaxis.extrae_elemento(self.completa_sin_prioridad)[3], '@oficina')
        self.assertEqual(sintaxis.extrae_elemento(self.solo_descripcion)[3], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_contexto)[3], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_resonsabilidad)[3], '@oficina')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_proyecto)[3], '@oficina')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_persona)[3], '@oficina')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_fecha)[3], '@oficina')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_hora)[3], '@oficina')
        self.assertEqual(sintaxis.extrae_elemento(self.descripcion_raros)[3], '@oficina')

    def test_persona(self):
        self.assertEqual(sintaxis.extrae_elemento(self.completa)[4], '+Persona')
        self.assertEqual(sintaxis.extrae_elemento(self.activa)[4], '+Persona')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_prioridad)[4], '+Persona')
        self.assertEqual(sintaxis.extrae_elemento(self.completa_sin_prioridad)[4], '+Persona')
        self.assertEqual(sintaxis.extrae_elemento(self.solo_descripcion)[4], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_contexto)[4], '+Persona')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_resonsabilidad)[4], '+Persona')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_proyecto)[4], '+Persona')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_persona)[4], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_fecha)[4], '+Persona')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_hora)[4], '+Persona')
        self.assertEqual(sintaxis.extrae_elemento(self.descripcion_raros)[4], '+Persona')

    def test_proyecto(self):
        self.assertEqual(sintaxis.extrae_elemento(self.completa)[5], '##Proyecto')
        self.assertEqual(sintaxis.extrae_elemento(self.activa)[5], '##Proyecto')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_prioridad)[5], '##Proyecto')
        self.assertEqual(sintaxis.extrae_elemento(self.completa_sin_prioridad)[5], '##Proyecto')
        self.assertEqual(sintaxis.extrae_elemento(self.solo_descripcion)[5], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_contexto)[5], '##Proyecto')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_resonsabilidad)[5], '##Proyecto')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_proyecto)[5], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_persona)[5], '##Proyecto')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_fecha)[5], '##Proyecto')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_hora)[5], '##Proyecto')
        self.assertEqual(sintaxis.extrae_elemento(self.descripcion_raros)[5], '##Proyecto')

    def test_responsabilidad(self):
        self.assertEqual(sintaxis.extrae_elemento(self.completa)[6], '#Responsabilidad')
        self.assertEqual(sintaxis.extrae_elemento(self.activa)[6], '#Responsabilidad')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_prioridad)[6], '#Responsabilidad')
        self.assertEqual(sintaxis.extrae_elemento(self.completa_sin_prioridad)[6], '#Responsabilidad')
        self.assertEqual(sintaxis.extrae_elemento(self.solo_descripcion)[6], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_contexto)[6], '#Responsabilidad')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_resonsabilidad)[6], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_proyecto)[6], '#Responsabilidad')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_persona)[6], '#Responsabilidad')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_fecha)[6], '#Responsabilidad')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_hora)[6], '#Responsabilidad')
        self.assertEqual(sintaxis.extrae_elemento(self.descripcion_raros)[6], '#Responsabilidad')

    def test_fecha(self):
        self.assertEqual(sintaxis.extrae_elemento(self.completa)[7], '01/01/2017 11:00')
        self.assertEqual(sintaxis.extrae_elemento(self.activa)[7], '01/01/2017 11:00')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_prioridad)[7], '01/01/2017 11:00')
        self.assertEqual(sintaxis.extrae_elemento(self.completa_sin_prioridad)[7], '01/01/2017 11:00')
        self.assertEqual(sintaxis.extrae_elemento(self.solo_descripcion)[7], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_contexto)[7], '01/01/2017 11:00')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_resonsabilidad)[7], '01/01/2017 11:00')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_proyecto)[7], '01/01/2017 11:00')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_persona)[7], '01/01/2017 11:00')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_fecha)[7], '')
        self.assertEqual(sintaxis.extrae_elemento(self.sin_hora)[7], '01/01/2017')
        self.assertEqual(sintaxis.extrae_elemento(self.descripcion_raros)[7], '01/01/2017 11:00')

if __name__ ==  '__main__':
    unittest.main()
