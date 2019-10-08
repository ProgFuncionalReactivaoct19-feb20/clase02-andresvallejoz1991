"""
Ejemplo 3
andresvallejoz1991
"""

#Cada elemento se muestra en una dupla

datos = ((30,1.79), (25,1.60),(35,1.68))
#Se llama la poscion de la dupla mediante la funcion lambda
dato = lambda x: x[2]
#Impresion de la posicion 2 de la dupla
print(dato(datos))