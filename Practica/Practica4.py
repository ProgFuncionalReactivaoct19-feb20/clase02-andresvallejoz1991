"""
Pratica 4
"""
#Lista de elementos
datos = [10,2,8,7,5,4,3,11,0, 1]
#Funcion para elevar todos los numeros de la lista al cubo
elevado = lambda x:x**3
#Impresion de un nuevo listado elevado al cubo
print(list(map(elevado,datos)))