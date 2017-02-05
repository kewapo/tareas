import sys
print(sys.platform)
mi_dic = dict()
mi_dic['nombre'] = 'Luis Javier'
print(mi_dic['nombre'])
print('Plataforma: {0.platform} Agente: {1[nombre]}'.format(sys, mi_dic))